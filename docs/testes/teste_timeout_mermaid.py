#!/usr/bin/env python3
"""
Script para testar os timeouts corrigidos do Mermaid
"""

import asyncio
import sys
import os
from pathlib import Path

# Adicionar o diretório src ao PYTHONPATH
project_root = Path(__file__).parent.parent.parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))

from parser.mermaid_processor import MermaidProcessor
from generator.pdf_generator import PDFGenerator
from generator.html_generator import HTMLGenerator
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_mermaid_timeout():
    """
    Testa se os timeouts do Mermaid foram corrigidos
    """
    print("🚀 Testando timeouts do Mermaid...")
    
    # Diagrama complexo para testar timeout
    complex_diagram = {
        'id': 'complex-test',
        'content': '''graph TD
    A[Início] --> B{Decisão}
    B -->|Sim| C[Processo A]
    B -->|Não| D[Processo B]
    C --> E[Subprocesso 1]
    C --> F[Subprocesso 2]
    D --> G[Subprocesso 3]
    D --> H[Subprocesso 4]
    E --> I[Resultado A]
    F --> J[Resultado B]
    G --> K[Resultado C]
    H --> L[Resultado D]
    I --> M[Consolidação]
    J --> M
    K --> M
    L --> M
    M --> N[Fim]
    
    style A fill:#e1f5fe
    style N fill:#f3e5f5
    style M fill:#fff3e0'''
    }
    
    # Teste 1: MermaidProcessor com timeout aumentado
    print("\n📝 Teste 1: MermaidProcessor (timeout 60s)")
    try:
        processor = MermaidProcessor()
        print(f"   Timeout configurado: {processor.timeout}ms")
        
        result = await processor.render_diagram(
            complex_diagram['id'], 
            complex_diagram['content']
        )
        
        if result:
            print("   ✅ Diagrama renderizado com sucesso!")
            print(f"   📏 Tamanho do SVG: {len(result)} caracteres")
        else:
            print("   ❌ Falha na renderização")
            
    except Exception as e:
        print(f"   ❌ Erro: {e}")
    
    # Teste 2: HTML Generator com SVG
    print("\n📝 Teste 2: HTML Generator com SVG")
    try:
        html_gen = HTMLGenerator()
        
        # Dados mockados
        parsed_data = {
            'html': '<h1>Teste</h1><div id="complex-test" class="mermaid-placeholder"></div>',
            'toc': '',
            'metadata': {'title': 'Teste Timeout'},
            'mermaid_diagrams': [complex_diagram],
            'stats': {'words': 100, 'lines': 10, 'chars': 500, 'mermaid_count': 1}
        }
        
        # Renderizar diagrama
        processor = MermaidProcessor()
        mermaid_svgs = await processor.process_diagrams([complex_diagram])
        
        # Gerar HTML
        html_content = html_gen.generate_html(parsed_data, mermaid_svgs)
        
        if 'mermaid-diagram' in html_content:
            print("   ✅ SVG inserido no HTML com sucesso!")
        else:
            print("   ❌ SVG não encontrado no HTML")
            
    except Exception as e:
        print(f"   ❌ Erro: {e}")
    
    print("\n🎉 Teste concluído!")

if __name__ == "__main__":
    asyncio.run(test_mermaid_timeout()) 