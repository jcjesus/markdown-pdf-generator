# ⚙️ **Sistema de Configuração Avançada**

Este documento detalha como configurar **cabeçalhos**, **rodapés**, **alinhamento de texto** e **numeração de páginas** no SoundLink Markdown PDF Generator.

## 🎯 **Métodos de Configuração**

### **1. Arquivo config.yaml (Global)**
```yaml
# Configurações aplicadas a todos os documentos
page:
  format: "A4"
  orientation: "portrait"
  margins:
    top: "20mm"
    right: "15mm" 
    bottom: "20mm"
    left: "15mm"
```

### **2. Metadata YAML (Por Documento)**
```yaml
---
title: "Meu Documento"
author: "João Silva"
template: "corporate"
format: "A3"
orientation: "landscape"
---
```

### **3. Parâmetros CLI (Temporário)**
```bash
python3 src/main.py documento.md --format A3 --landscape
```

## 📄 **Configuração de Cabeçalhos**

### **Cabeçalho Simples**
```yaml
header:
  enabled: true
  template: |
    <div style="text-align: center; font-size: 11px; color: #333;">
      {{document.title}}
    </div>
```

### **Cabeçalho Completo (3 Colunas)**
```yaml
header:
  enabled: true
  template: |
    <div style="display: flex; justify-content: space-between; font-size: 10px; padding: 0 20px; color: #666;">
      <span>{{document.author}}</span>
      <span>{{document.title}}</span>
      <span>{{date.formatted}}</span>
    </div>
```

### **Cabeçalho com Logo**
```yaml
header:
  enabled: true
  template: |
    <div style="display: flex; align-items: center; justify-content: space-between; padding: 0 20px;">
      <img src="logo.png" style="height: 20px;" alt="Logo">
      <span style="font-size: 12px; font-weight: bold;">{{document.title}}</span>
      <span style="font-size: 10px; color: #999;">{{date.formatted}}</span>
    </div>
```

## 📄 **Configuração de Rodapés**

### **Rodapé com Numeração**
```yaml
footer:
  enabled: true
  template: |
    <div style="text-align: center; font-size: 10px; color: #666;">
      Página {{page.current}} de {{page.total}}
    </div>
```

### **Rodapé Corporativo**
```yaml
footer:
  enabled: true
  template: |
    <div style="display: flex; justify-content: space-between; font-size: 9px; padding: 0 20px; color: #777;">
      <span>© 2024 SoundLink</span>
      <span>{{document.author}}</span>
      <span>{{page.current}}/{{page.total}}</span>
    </div>
```

### **Rodapé com Estatísticas**
```yaml
footer:
  enabled: true
  template: |
    <div style="display: flex; justify-content: space-between; font-size: 9px; padding: 0 20px;">
      <span>{{stats.words}} palavras</span>
      <span>Página {{page.current}} de {{page.total}}</span>
      <span>{{generator.name}}</span>
    </div>
```

## 🔢 **Numeração de Páginas**

### **Posições Disponíveis**
- `header-left`, `header-center`, `header-right`
- `footer-left`, `footer-center`, `footer-right`

### **Formatos de Numeração**
```yaml
page_numbers:
  enabled: true
  position: "footer-right"
  format: "Página {current} de {total}"  # Padrão
  # format: "{current}/{total}"          # Compacto
  # format: "{roman} de {total}"         # Romano
  # format: "Pág. {current}"             # Simples
  start_from: 1
```

### **Numeração Personalizada**
```yaml
page_numbers:
  enabled: true
  position: "footer-center"
  format: "📄 {current} de {total} páginas"
  styles:
    font_family: "Inter, sans-serif"
    font_size: "10px"
    color: "#666666"
```

## 📐 **Alinhamento de Texto**

### **Configuração Global**
```yaml
text_alignment:
  paragraphs: "justify"     # left, center, right, justify
  headers: "left"           # left, center, right
  tables: "center"          # left, center, right
  code_blocks: "left"       # left, center, right
  blockquotes: "left"       # left, center, right
  images: "center"          # left, center, right
```

### **Alinhamento por Elemento**
```yaml
text_alignment:
  paragraphs: "justify"     # Texto justificado
  headers: "center"         # Títulos centralizados
  tables: "center"          # Tabelas centralizadas
  images: "center"          # Imagens centralizadas
  code_blocks: "left"       # Código alinhado à esquerda
```

## 🎨 **Templates Pré-definidos**

### **Template Minimal**
```yaml
template: "minimal"
# - Sem cabeçalho
# - Rodapé apenas com número da página
# - Estilo limpo e minimalista
```

### **Template Corporate**
```yaml
template: "corporate"
# - Cabeçalho com logo e título
# - Rodapé com copyright e numeração
# - Cores corporativas
# - Layout profissional
```

### **Template Academic**
```yaml
template: "academic"
# - Cabeçalho com título do documento
# - Rodapé com autor e numeração
# - Formatação acadêmica
# - Espaçamento adequado
```

## 🎯 **Variáveis Disponíveis**

### **Variáveis de Documento**
```yaml
{{document.title}}          # Título do documento
{{document.subtitle}}       # Subtítulo
{{document.author}}         # Autor
{{document.description}}    # Descrição
{{document.version}}        # Versão
```

### **Variáveis de Data**
```yaml
{{date.current}}           # 2024-01-15
{{date.formatted}}         # 15/01/2024
{{date.long}}              # 15 de Janeiro de 2024
{{date.year}}              # 2024
{{date.month}}             # 1
{{date.day}}               # 15
```

### **Variáveis de Página**
```yaml
{{page.current}}           # Página atual
{{page.total}}             # Total de páginas
{{page.roman}}             # Página em romano (i, ii, iii)
{{page.alpha}}             # Página em letras (a, b, c)
```

### **Variáveis de Estatísticas**
```yaml
{{stats.words}}            # Total de palavras
{{stats.lines}}            # Total de linhas
{{stats.chars}}            # Total de caracteres
{{stats.mermaid_count}}    # Número de diagramas
```

### **Variáveis do Gerador**
```yaml
{{generator.name}}         # Nome do gerador
{{generator.version}}      # Versão do gerador
{{generator.url}}          # URL do projeto
```

## 📏 **Configuração de Margens**

### **Margens Padrão**
```yaml
margins:
  top: "20mm"
  right: "15mm"
  bottom: "20mm"
  left: "15mm"
```

### **Margens Personalizadas**
```yaml
margins:
  top: "30mm"      # Mais espaço no topo
  right: "25mm"    # Margens laterais maiores
  bottom: "30mm"   # Espaço para rodapé
  left: "25mm"     # Margem esquerda
```

### **Margens via CLI**
```bash
# Formato: "top,right,bottom,left" em mm
python3 src/main.py documento.md --margin "25,20,25,20"
```

## 🎨 **Estilos CSS Avançados**

### **Cabeçalho com Gradiente**
```yaml
header:
  template: |
    <div style="
      background: linear-gradient(90deg, #3498db, #2980b9);
      color: white;
      padding: 10px 20px;
      font-size: 11px;
      font-weight: bold;
    ">
      {{document.title}}
    </div>
```

### **Rodapé com Bordas**
```yaml
footer:
  template: |
    <div style="
      border-top: 2px solid #3498db;
      padding: 5px 20px;
      font-size: 9px;
      color: #666;
      display: flex;
      justify-content: space-between;
    ">
      <span>{{document.author}}</span>
      <span>Página {{page.current}} de {{page.total}}</span>
    </div>
```

## 🔧 **Exemplos Práticos**

### **Documento Corporativo Completo**
```yaml
---
title: "Relatório Anual 2024"
subtitle: "Análise de Performance"
author: "Equipe Executiva"
template: "corporate"
format: "A4"
orientation: "portrait"

header:
  enabled: true
  template: |
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 0 20px; border-bottom: 2px solid #3498db;">
      <img src="logo.png" style="height: 25px;" alt="Logo">
      <div style="text-align: center;">
        <strong style="font-size: 12px;">{{document.title}}</strong><br>
        <small style="color: #666;">{{document.subtitle}}</small>
      </div>
      <span style="font-size: 10px; color: #999;">{{date.formatted}}</span>
    </div>

footer:
  enabled: true
  template: |
    <div style="display: flex; justify-content: space-between; padding: 0 20px; font-size: 9px; color: #666; border-top: 1px solid #ddd;">
      <span>{{document.author}}</span>
      <span>Confidencial - Uso Interno</span>
      <span>{{page.current}}/{{page.total}}</span>
    </div>

text_alignment:
  paragraphs: "justify"
  headers: "left"
  tables: "center"
  images: "center"
---
```

### **Manual Técnico**
```yaml
---
title: "Manual do Desenvolvedor"
author: "Equipe Técnica"
template: "academic"
format: "A4"

header:
  enabled: true
  template: |
    <div style="text-align: center; padding: 8px; border-bottom: 1px solid #ccc;">
      <strong>{{document.title}}</strong> - {{document.author}}
    </div>

footer:
  enabled: true
  template: |
    <div style="text-align: center; font-size: 9px; color: #777;">
      {{page.current}} | {{stats.words}} palavras | Versão {{document.version}}
    </div>

page_numbers:
  enabled: false  # Numeração customizada no rodapé
---
```

## 🚀 **Uso Programático**

### **Python API**
```python
from config import ConfigManager, TemplateVariables
from generator import PDFGenerator

# Configurar gerador
config_manager = ConfigManager('custom-config.yaml')
pdf_generator = PDFGenerator(config_path='custom-config.yaml')

# Metadados do documento
metadata = {
    'title': 'Meu Documento',
    'author': 'João Silva',
    'template': 'corporate'
}

# Gerar PDF com configuração
await pdf_generator.generate_pdf(
    html_file_path='documento.html',
    output_path='documento.pdf',
    metadata=metadata
)
```

### **CLI Avançado**
```bash
# Template específico
python3 src/main.py doc.md --template corporate

# Configuração personalizada
python3 src/main.py doc.md --config custom-config.yaml

# Override de configurações
python3 src/main.py doc.md --format A3 --landscape --margin "30,25,30,25"
```

## ✅ **Validação e Debugging**

### **Validar Configuração**
```python
config_manager = ConfigManager()
warnings = config_manager.validate_config()
for warning in warnings:
    print(f"⚠️  {warning}")
```

### **Listar Templates**
```python
templates = config_manager.list_templates()
print(f"Templates: {', '.join(templates)}")
```

### **Visualizar Variáveis**
```python
template_vars = TemplateVariables(metadata, stats)
variables = template_vars.get_variables()
print(json.dumps(variables, indent=2))
```

## 🎯 **Dicas e Melhores Práticas**

### **✅ Boas Práticas**
- Use templates para consistência
- Configure margens adequadas (mín. 15mm)
- Teste com documentos de tamanhos diferentes
- Use variáveis ao invés de texto fixo
- Mantenha cabeçalhos/rodapés simples

### **❌ Evite**
- Cabeçalhos/rodapés muito altos
- Muitas variáveis em templates simples
- Cores muito claras (podem não imprimir)
- Fontes não padronizadas
- Layouts muito complexos

### **🔧 Troubleshooting**
- **Cabeçalho não aparece**: Verifique `enabled: true`
- **Variáveis não funcionam**: Sintaxe `{{variable}}`
- **Layout quebrado**: Teste CSS isoladamente
- **Margens incorretas**: Use unidades (mm, px)
- **Fonte não carrega**: Use fontes web-safe

---

## 📞 **Suporte**

Para dúvidas sobre configuração:
- 📧 config@soundlink.com.br
- 📚 [Documentação Completa](../README.md)
- 🔧 [Exemplos](../examples/)

**Criado com ❤️ pela equipe SoundLink** 🚀 