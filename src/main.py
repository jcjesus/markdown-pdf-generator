#!/usr/bin/env python3
"""
Main CLI interface for Markdown PDF Generator
"""

import argparse
import asyncio
import os
import sys
import logging
from typing import Optional
from pathlib import Path

# Import project modules
from parser import MarkdownParser, MermaidProcessor
from generator import HTMLGenerator, PDFGenerator

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def setup_argument_parser() -> argparse.ArgumentParser:
    """
    Setup command line argument parser
    
    Returns:
        Configured ArgumentParser
    """
    parser = argparse.ArgumentParser(
        description='🚀 SoundLink Markdown PDF Generator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  %(prog)s documento.md                     # Gera PDF do documento
  %(prog)s documento.md -o relatorio.pdf    # Especifica nome do arquivo
  %(prog)s documento.md --html             # Gera apenas HTML
  %(prog)s documento.md --format A3        # Usa formato A3
  %(prog)s documento.md --landscape        # Orientação paisagem
  %(prog)s documento.md --no-mermaid       # Ignora diagramas Mermaid
  %(prog)s documento.md --css custom.css   # CSS customizado
  %(prog)s documento.md --verbose          # Logs detalhados

Formatos suportados: A4, A3, A2, A1, A0, Letter, Legal, Tabloid
Recursos: Markdown, Emojis, Tabelas, Código, Mermaid, TOC, Metadados
        """
    )
    
    # Required arguments
    parser.add_argument(
        'input_file',
        help='Arquivo Markdown de entrada (.md)'
    )
    
    # Optional arguments
    parser.add_argument(
        '-o', '--output',
        help='Arquivo de saída (padrão: mesmo nome com extensão .pdf)'
    )
    
    parser.add_argument(
        '--html',
        action='store_true',
        help='Gerar apenas HTML (não gera PDF)'
    )
    
    parser.add_argument(
        '--format',
        choices=['A4', 'A3', 'A2', 'A1', 'A0', 'Letter', 'Legal', 'Tabloid'],
        default='A4',
        help='Formato do papel (padrão: A4)'
    )
    
    parser.add_argument(
        '--landscape',
        action='store_true',
        help='Orientação paisagem (padrão: retrato)'
    )
    
    parser.add_argument(
        '--no-mermaid',
        action='store_true',
        help='Ignorar diagramas Mermaid'
    )
    
    parser.add_argument(
        '--css',
        help='Arquivo CSS customizado'
    )
    
    parser.add_argument(
        '--no-toc',
        action='store_true',
        help='Não gerar índice (TOC)'
    )
    
    parser.add_argument(
        '--margin',
        help='Margens do PDF (formato: "top,right,bottom,left" em mm)'
    )
    
    parser.add_argument(
        '--scale',
        type=float,
        default=1.0,
        help='Fator de escala para renderização (padrão: 1.0)'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Logs detalhados'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0.0'
    )
    
    return parser


def validate_input_file(file_path: str) -> bool:
    """
    Validate input markdown file
    
    Args:
        file_path: Path to markdown file
        
    Returns:
        True if valid, False otherwise
    """
    if not os.path.exists(file_path):
        logger.error(f"Arquivo não encontrado: {file_path}")
        return False
    
    if not file_path.lower().endswith('.md'):
        logger.error(f"Arquivo deve ter extensão .md: {file_path}")
        return False
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content.strip():
                logger.error(f"Arquivo vazio: {file_path}")
                return False
    except Exception as e:
        logger.error(f"Erro ao ler arquivo: {e}")
        return False
    
    return True


def parse_margins(margin_str: str) -> dict:
    """
    Parse margin string into dictionary
    
    Args:
        margin_str: Margin string in format "top,right,bottom,left"
        
    Returns:
        Dictionary with margin values
    """
    try:
        margins = margin_str.split(',')
        if len(margins) != 4:
            raise ValueError("Formato inválido")
        
        return {
            'top': f"{margins[0].strip()}mm",
            'right': f"{margins[1].strip()}mm",
            'bottom': f"{margins[2].strip()}mm",
            'left': f"{margins[3].strip()}mm"
        }
    except Exception as e:
        logger.error(f"Erro ao parsear margens: {e}")
        return None


def load_custom_css(css_path: str) -> Optional[str]:
    """
    Load custom CSS file
    
    Args:
        css_path: Path to CSS file
        
    Returns:
        CSS content or None if failed
    """
    try:
        with open(css_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        logger.error(f"Erro ao carregar CSS: {e}")
        return None


async def generate_pdf(input_file: str, output_file: str, args) -> bool:
    """
    Main PDF generation function
    
    Args:
        input_file: Input markdown file path
        output_file: Output PDF file path
        args: Command line arguments
        
    Returns:
        True if successful, False otherwise
    """
    try:
        # 1. Read markdown file
        logger.info(f"📖 Lendo arquivo: {input_file}")
        with open(input_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # 2. Initialize parser
        parser = MarkdownParser()
        
        # 3. Parse markdown
        logger.info("🔍 Parseando Markdown...")
        parsed_data = parser.parse(markdown_content)
        
        # 4. Process Mermaid diagrams if enabled
        mermaid_svgs = {}
        if not args.no_mermaid and parsed_data['mermaid_diagrams']:
            logger.info("🎨 Processando diagramas Mermaid...")
            mermaid_processor = MermaidProcessor()
            mermaid_svgs = await mermaid_processor.process_diagrams(
                parsed_data['mermaid_diagrams']
            )
        
        # 5. Load custom CSS if provided
        custom_css = None
        if args.css:
            custom_css = load_custom_css(args.css)
        
        # 6. Generate HTML
        logger.info("🌐 Gerando HTML...")
        html_generator = HTMLGenerator(custom_css=custom_css)
        html_content = html_generator.generate_html(parsed_data, mermaid_svgs)
        
        # 7. Generate HTML only if requested
        if args.html:
            html_output = output_file.replace('.pdf', '.html')
            with open(html_output, 'w', encoding='utf-8') as f:
                f.write(html_content)
            logger.info(f"✅ HTML gerado: {html_output}")
            return True
        
        # 8. Setup PDF generator
        margins = None
        if args.margin:
            margins = parse_margins(args.margin)
        
        pdf_generator = PDFGenerator(
            format=args.format,
            margin=margins,
            landscape=args.landscape,
            scale=args.scale
        )
        
        # 9. Generate PDF
        logger.info("📄 Gerando PDF...")
        success = await pdf_generator.generate_pdf_from_html_content(
            html_content, 
            output_file,
            parsed_data['metadata']
        )
        
        if success:
            # Get file size
            file_size = os.path.getsize(output_file)
            logger.info(f"✅ PDF gerado com sucesso: {output_file} ({file_size:,} bytes)")
            
            # Print statistics
            stats = parsed_data['stats']
            logger.info(f"📊 Estatísticas: {stats['words']} palavras, {stats['lines']} linhas, {stats['mermaid_count']} diagramas")
            
            return True
        else:
            logger.error("❌ Falha na geração do PDF")
            return False
        
    except Exception as e:
        logger.error(f"❌ Erro durante a geração: {e}")
        return False


def main():
    """
    Main entry point
    """
    # Parse arguments
    parser = setup_argument_parser()
    args = parser.parse_args()
    
    # Setup logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Validate input file
    if not validate_input_file(args.input_file):
        sys.exit(1)
    
    # Determine output file
    if args.output:
        output_file = args.output
    else:
        input_path = Path(args.input_file)
        if args.html:
            output_file = str(input_path.with_suffix('.html'))
        else:
            output_file = str(input_path.with_suffix('.pdf'))
    
    # Print banner
    print("🚀 SoundLink Markdown PDF Generator v1.0.0")
    print(f"📝 Entrada: {args.input_file}")
    print(f"📄 Saída: {output_file}")
    print(f"📐 Formato: {args.format}")
    print(f"🔧 Orientação: {'Paisagem' if args.landscape else 'Retrato'}")
    print(f"🎨 Mermaid: {'Desabilitado' if args.no_mermaid else 'Habilitado'}")
    print("-" * 50)
    
    # Run generation
    try:
        success = asyncio.run(generate_pdf(args.input_file, output_file, args))
        if success:
            print("✅ Conversão concluída com sucesso!")
            sys.exit(0)
        else:
            print("❌ Falha na conversão!")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n⏹️  Operação cancelada pelo usuário")
        sys.exit(1)
    except Exception as e:
        logger.error(f"❌ Erro inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 