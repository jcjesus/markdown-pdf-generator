#!/usr/bin/env python3
"""
Exemplo de uso do sistema de configuração avançada
"""

import sys
import asyncio
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from config import ConfigManager, TemplateVariables
from generator import PDFGenerator
from parser import MarkdownParser


async def exemplo_basico():
    """Exemplo básico com configuração padrão"""
    print("🔧 Exemplo 1: Configuração Padrão")
    
    # Inicializar com configuração padrão
    config_manager = ConfigManager()
    
    # Simular metadados do documento
    metadata = {
        'title': 'Exemplo Básico',
        'author': 'João Silva',
        'date': '2024-01-15'
    }
    
    stats = {
        'words': 1250,
        'lines': 45,
        'chars': 8500,
        'mermaid_count': 2
    }
    
    # Criar variáveis de template
    template_vars = TemplateVariables(metadata, stats)
    variables = template_vars.get_variables()
    
    print(f"📄 Título: {variables['document']['title']}")
    print(f"👤 Autor: {variables['document']['author']}")
    print(f"📊 Estatísticas: {variables['stats']['words']} palavras")
    print(f"📅 Data: {variables['date']['formatted']}")
    print()


async def exemplo_template_corporativo():
    """Exemplo com template corporativo"""
    print("🏢 Exemplo 2: Template Corporativo")
    
    config_manager = ConfigManager()
    
    # Metadados para template corporativo
    metadata = {
        'title': 'Relatório de Performance Q4',
        'subtitle': 'Análise Trimestral',
        'author': 'Equipe Analytics',
        'template': 'corporate',  # Usar template corporativo
        'format': 'A4',
        'orientation': 'portrait'
    }
    
    # Obter opções de PDF
    pdf_options = config_manager.get_pdf_options(metadata)
    
    print(f"📐 Formato: {pdf_options['format']}")
    print(f"🔄 Orientação: {'Paisagem' if pdf_options['landscape'] else 'Retrato'}")
    print(f"📏 Margens: {pdf_options['margin']}")
    print(f"🎨 Cabeçalho/Rodapé: {'Sim' if pdf_options['display_header_footer'] else 'Não'}")
    print()


async def exemplo_template_personalizado():
    """Exemplo com template personalizado via YAML metadata"""
    print("🎨 Exemplo 3: Template Personalizado")
    
    # Markdown com configuração inline
    markdown_content = """---
title: "Manual do Usuário"
author: "Equipe Técnica"
template: "academic"
header:
  enabled: true
  template: |
    <div style="text-align: center; font-size: 12px; padding: 10px; border-bottom: 2px solid #3498db;">
      <strong>{{document.title}} - {{document.author}}</strong>
    </div>
footer:
  enabled: true
  template: |
    <div style="display: flex; justify-content: space-between; font-size: 10px; padding: 0 20px;">
      <span>Confidencial</span>
      <span>Página {{page.current}}/{{page.total}}</span>
      <span>{{date.formatted}}</span>
    </div>
---

# Manual do Usuário

Este é um exemplo de documento com configuração personalizada.
"""
    
    # Parse do markdown
    parser = MarkdownParser()
    parsed_data = parser.parse(markdown_content)
    
    print(f"📄 Título: {parsed_data['metadata']['title']}")
    print(f"🎭 Template: {parsed_data['metadata']['template']}")
    print(f"📊 Estatísticas: {parsed_data['stats']}")
    print()


async def exemplo_configuracao_completa():
    """Exemplo de configuração completa via arquivo"""
    print("⚙️  Exemplo 4: Configuração Completa")
    
    # Criar configuração personalizada
    config_personalizada = {
        'page': {
            'format': 'A3',
            'orientation': 'landscape',
            'margins': {
                'top': '30mm',
                'right': '25mm',
                'bottom': '30mm',
                'left': '25mm'
            }
        },
        'header': {
            'enabled': True,
            'template': '''
            <div style="display: flex; justify-content: space-between; font-size: 11px; padding: 0 30px; color: #2c3e50;">
                <strong>🚀 {{document.title}}</strong>
                <span>{{date.formatted}}</span>
            </div>
            '''
        },
        'footer': {
            'enabled': True,
            'template': '''
            <div style="text-align: center; font-size: 10px; color: #7f8c8d;">
                {{document.author}} | Página {{page.current}} de {{page.total}} | {{generator.name}}
            </div>
            '''
        },
        'text_alignment': {
            'paragraphs': 'justify',
            'headers': 'center',
            'tables': 'center',
            'images': 'center'
        }
    }
    
    config_manager = ConfigManager()
    
    # Atualizar configuração
    config_manager.update_config(config_personalizada)
    
    metadata = {
        'title': 'Relatório Técnico Detalhado',
        'author': 'Equipe de Engenharia'
    }
    
    # Obter configuração final
    pdf_options = config_manager.get_pdf_options(metadata)
    css_alignment = config_manager.get_text_alignment_css()
    
    print(f"📐 Formato: {pdf_options['format']}")
    print(f"🔄 Orientação: {'Paisagem' if pdf_options['landscape'] else 'Retrato'}")
    print(f"📏 Margens: {pdf_options['margin']}")
    print("🎨 CSS de Alinhamento:")
    for line in css_alignment.split('\n'):
        if line.strip():
            print(f"   {line.strip()}")
    print()


async def exemplo_geracao_pdf():
    """Exemplo completo de geração de PDF"""
    print("📄 Exemplo 5: Geração de PDF Completa")
    
    try:
        # Configurar gerador de PDF
        pdf_generator = PDFGenerator()
        
        # Metadados do documento
        metadata = {
            'title': 'Exemplo de Configuração Avançada',
            'subtitle': 'Demonstração do Sistema',
            'author': 'SoundLink Team',
            'template': 'corporate'
        }
        
        stats = {
            'words': 850,
            'lines': 32,
            'chars': 5200,
            'mermaid_count': 1
        }
        
        print(f"📄 Documento: {metadata['title']}")
        print(f"👤 Autor: {metadata['author']}")
        print(f"🎭 Template: {metadata['template']}")
        print(f"📊 {stats['words']} palavras, {stats['mermaid_count']} diagrama")
        print("✅ Configuração aplicada com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro: {e}")
    
    print()


async def exemplo_validacao():
    """Exemplo de validação de configuração"""
    print("🔍 Exemplo 6: Validação de Configuração")
    
    config_manager = ConfigManager()
    warnings = config_manager.validate_config()
    
    if warnings:
        print("⚠️  Avisos de configuração:")
        for warning in warnings:
            print(f"   • {warning}")
    else:
        print("✅ Configuração válida!")
    
    # Listar templates disponíveis
    templates = config_manager.list_templates()
    print(f"🎭 Templates disponíveis: {', '.join(templates) if templates else 'Nenhum'}")
    print()


async def main():
    """Executar todos os exemplos"""
    print("🚀 Sistema de Configuração Avançada - Exemplos")
    print("=" * 60)
    print()
    
    await exemplo_basico()
    await exemplo_template_corporativo()
    await exemplo_template_personalizado()
    await exemplo_configuracao_completa()
    await exemplo_geracao_pdf()
    await exemplo_validacao()
    
    print("🎉 Todos os exemplos executados com sucesso!")
    print()
    
    print("📚 Para usar na prática:")
    print("1. Copie os exemplos que interessam")
    print("2. Adapte para seus metadados específicos")
    print("3. Execute com: python3 docs/exemplo-configuracao.py")
    print("4. Integre no seu fluxo de trabalho")


if __name__ == "__main__":
    asyncio.run(main()) 