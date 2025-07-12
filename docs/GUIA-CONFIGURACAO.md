# 🚀 **Guia Rápido - Sistema de Configuração Avançada**

## ⚡ **Uso Imediato**

### **1. Configuração Básica via Metadata YAML**
```yaml
---
title: "Meu Relatório"
author: "João Silva"
template: "corporate"
format: "A4"
orientation: "portrait"

# Cabeçalho personalizado
header:
  enabled: true
  template: |
    <div style="text-align: center; font-size: 12px; padding: 10px; border-bottom: 2px solid #3498db;">
      <strong>{{document.title}} - {{document.author}}</strong>
    </div>

# Rodapé personalizado  
footer:
  enabled: true
  template: |
    <div style="display: flex; justify-content: space-between; font-size: 10px; padding: 0 20px;">
      <span>{{date.formatted}}</span>
      <span>Página {{page.current}} de {{page.total}}</span>
      <span>Confidencial</span>
    </div>

# Alinhamento de texto
text_alignment:
  paragraphs: "justify"
  headers: "center"
  tables: "center"
---

# Conteúdo do documento...
```

### **2. Comandos Rápidos**
```bash
# Gerar PDF básico
make run FILE=documento.md

# Gerar com template corporativo
make template FILE=documento.md TEMPLATE=corporate

# Gerar em formato A3 paisagem
make run FILE=documento.md ARGS="--format A3 --landscape"

# Validar configuração
make config-validate

# Ver exemplos de configuração
make config-example

# Listar templates disponíveis
make config-templates
```

## 🎯 **Variáveis Mais Usadas**

### **Documento**
- `{{document.title}}` - Título
- `{{document.author}}` - Autor  
- `{{document.subtitle}}` - Subtítulo

### **Data e Hora**
- `{{date.formatted}}` - 15/01/2024
- `{{date.current}}` - 2024-01-15
- `{{date.long}}` - 15 de Janeiro de 2024

### **Páginas**
- `{{page.current}}` - Página atual
- `{{page.total}}` - Total de páginas
- `{{page.roman}}` - Numeração romana

### **Estatísticas**
- `{{stats.words}}` - Total de palavras
- `{{stats.mermaid_count}}` - Número de diagramas

## 🎨 **Templates Prontos**

### **Minimal** - Limpo e simples
```yaml
template: "minimal"
# ✅ Sem cabeçalho
# ✅ Rodapé apenas com numeração
# ✅ Layout minimalista
```

### **Corporate** - Profissional
```yaml
template: "corporate" 
# ✅ Cabeçalho com logo
# ✅ Rodapé com copyright
# ✅ Cores corporativas
# ✅ Layout executivo
```

### **Academic** - Acadêmico
```yaml
template: "academic"
# ✅ Cabeçalho com título
# ✅ Rodapé com autor
# ✅ Formatação acadêmica
# ✅ Espaçamento otimizado
```

## 📐 **Configurações Comuns**

### **Margens Personalizadas**
```yaml
margins:
  top: "25mm"      # Mais espaço no topo
  right: "20mm"    # Margens laterais
  bottom: "25mm"   # Espaço para rodapé
  left: "20mm"     # Margem esquerda
```

### **Orientação e Formato**
```yaml
format: "A4"           # A4, A3, Letter, Legal
orientation: "portrait" # portrait, landscape
```

### **Numeração de Páginas**
```yaml
page_numbers:
  enabled: true
  position: "footer-right"  # footer-left, footer-center, footer-right
  format: "Página {current} de {total}"
```

## 🔧 **Exemplos de Cabeçalhos**

### **Cabeçalho Simples**
```html
<div style="text-align: center; font-size: 11px; color: #333;">
  {{document.title}}
</div>
```

### **Cabeçalho com 3 Colunas**
```html
<div style="display: flex; justify-content: space-between; font-size: 10px; padding: 0 20px;">
  <span>{{document.author}}</span>
  <span><strong>{{document.title}}</strong></span>
  <span>{{date.formatted}}</span>
</div>
```

### **Cabeçalho com Logo**
```html
<div style="display: flex; align-items: center; justify-content: space-between; padding: 0 20px;">
  <img src="logo.png" style="height: 20px;">
  <span style="font-weight: bold;">{{document.title}}</span>
  <span style="font-size: 10px;">v{{document.version}}</span>
</div>
```

## 🔧 **Exemplos de Rodapés**

### **Rodapé Básico**
```html
<div style="text-align: center; font-size: 10px; color: #666;">
  Página {{page.current}} de {{page.total}}
</div>
```

### **Rodapé Corporativo**
```html
<div style="display: flex; justify-content: space-between; font-size: 9px; padding: 0 20px;">
  <span>© 2024 SoundLink</span>
  <span>{{document.author}}</span>
  <span>{{page.current}}/{{page.total}}</span>
</div>
```

### **Rodapé com Estatísticas**
```html
<div style="display: flex; justify-content: space-between; font-size: 9px; padding: 0 20px;">
  <span>{{stats.words}} palavras</span>
  <span>{{page.current}}/{{page.total}}</span>
  <span>{{generator.name}}</span>
</div>
```

## 📋 **Checklist de Configuração**

### **✅ Antes de Gerar o PDF**
- [ ] Definir título e autor no metadata
- [ ] Escolher template apropriado
- [ ] Configurar formato e orientação
- [ ] Ajustar margens se necessário
- [ ] Testar cabeçalho e rodapé
- [ ] Verificar alinhamento de texto
- [ ] Validar configuração

### **✅ Após Gerar o PDF**
- [ ] Verificar cabeçalho em todas as páginas
- [ ] Confirmar numeração de páginas
- [ ] Checar alinhamento de elementos
- [ ] Validar margens e espaçamento
- [ ] Testar qualidade de impressão

## 🚀 **Comandos Úteis**

```bash
# Configuração
make config-help          # Ver comandos de configuração
make config-validate       # Validar config.yaml
make config-templates      # Listar templates
make config-example        # Executar exemplos
make config-edit          # Editar configuração

# Geração de PDF
make run FILE=doc.md                                    # Básico
make template FILE=doc.md TEMPLATE=corporate           # Com template
make run FILE=doc.md ARGS="--format A3 --landscape"    # Formato personalizado
make run FILE=doc.md ARGS="--margin '30,25,30,25'"     # Margens personalizadas

# Desenvolvimento
make test                 # Executar testes
make lint                 # Verificar código
make clean               # Limpar temporários
```

## 🎯 **Casos de Uso Comuns**

### **📊 Relatório Executivo**
```yaml
---
title: "Relatório Executivo Q4 2024"
author: "CEO - João Silva"
template: "corporate"
format: "A4"
orientation: "portrait"
margins:
  top: "25mm"
  bottom: "25mm"
text_alignment:
  paragraphs: "justify"
  headers: "center"
---
```

### **📚 Manual Técnico**
```yaml
---
title: "Manual do Desenvolvedor"
author: "Equipe Técnica"
template: "academic"
format: "A4"
header:
  template: |
    <div style="border-bottom: 1px solid #ccc; padding: 8px; text-align: center;">
      <strong>{{document.title}}</strong>
    </div>
---
```

### **📝 Documentação de API**
```yaml
---
title: "SoundLink API v2.0"
author: "Equipe Backend"
template: "minimal"
format: "A4"
text_alignment:
  paragraphs: "left"
  code_blocks: "left"
  tables: "left"
---
```

### **📋 Proposta Comercial**
```yaml
---
title: "Proposta SoundLink Enterprise"
subtitle: "Solução Completa para Empresas"
author: "Equipe Comercial"
template: "corporate"
format: "A4"
margins:
  top: "30mm"
  bottom: "30mm"
header:
  template: |
    <div style="background: linear-gradient(90deg, #3498db, #2980b9); color: white; padding: 10px 20px; text-align: center;">
      <strong>{{document.title}}</strong>
    </div>
---
```

## 🔗 **Links Úteis**

- 📚 [Documentação Completa](README.md)
- ⚙️ [Configuração Avançada](docs/CONFIGURACAO.md)
- 🎨 [Exemplos](examples/)
- 🔧 [Troubleshooting](docs/TROUBLESHOOTING.md)

---

**Pronto para criar PDFs profissionais!** 🚀

*Para suporte: config@soundlink.com.br* 