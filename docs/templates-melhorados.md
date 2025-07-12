# 🎨 Templates Melhorados - Guia Completo

## 🚀 Visão Geral

Os templates de cabeçalho e rodapé foram completamente melhorados para resolver problemas de alinhamento e distribuição de elementos.

### ❌ Problemas Antigos
- Elementos todos alinhados à direita
- Conflitos entre `text-align: center` e `display: flex`
- Texto sendo cortado em títulos longos
- Distribuição desigual dos elementos

### ✅ Soluções Implementadas
- **Distribuição equilibrada**: Cada elemento ocupa 1/3 da largura
- **Flexbox otimizado**: Uso correto de `flex: 1` para cada seção
- **Texto inteligente**: Overflow com `text-overflow: ellipsis`
- **Alinhamento preciso**: Esquerda, centro, direita bem definidos

## 🎯 Templates Disponíveis

### 1. **Template Padrão (default)**

**Uso:**
```yaml
---
title: "Meu Documento"
author: "João Silva"
subtitle: "Subtítulo"
---
```

**Resultado:**
- **Cabeçalho**: Título | Autor | Data
- **Rodapé**: Gerador v1.0 | Subtítulo | Página X de Y

### 2. **Template Corporativo (corporate)**

**Uso:**
```yaml
---
title: "Relatório Empresarial"
author: "Equipe SoundLink"
template: "corporate"
---
```

**Resultado:**
- **Cabeçalho**: 🏢 Título | Autor | Data
- **Rodapé**: Autor | Subtítulo • Copyright | Página X/Y

### 3. **Template Acadêmico (academic)**

**Uso:**
```yaml
---
title: "Dissertação"
subtitle: "Subtítulo da Pesquisa"
author: "Estudante"
template: "academic"
---
```

**Resultado:**
- **Cabeçalho**: Título (centralizado) com subtítulo
- **Rodapé**: Autor | Gerador | Página X

### 4. **Template Minimalista (minimal)**

**Uso:**
```yaml
---
title: "Documento Simples"
template: "minimal"
---
```

**Resultado:**
- **Cabeçalho**: Desabilitado
- **Rodapé**: Apenas "Página X"

## 🔧 Templates Personalizados

### Template Moderno
```yaml
---
title: "Documento Moderno"
author: "Designer"
template: "custom"

header:
  enabled: true
  template: |
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 11px; color: #333; background: linear-gradient(90deg, #f8f9fa, #e9ecef); border-bottom: 3px solid #3498db; box-sizing: border-box; height: 100%;">
      <div style="flex: 1; text-align: left; overflow: hidden;">
        <span style="font-weight: 700; color: #3498db;">📄 {{document.title}}</span>
      </div>
      <div style="flex: 1; text-align: center; overflow: hidden;">
        <span style="font-weight: 500;">{{document.author}}</span>
      </div>
      <div style="flex: 1; text-align: right; overflow: hidden;">
        <span style="color: #666;">{{date.formatted}}</span>
      </div>
    </div>

footer:
  enabled: true
  template: |
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #666; background: #f8f9fa; border-top: 1px solid #dee2e6; box-sizing: border-box; height: 100%;">
      <div style="flex: 1; text-align: left; overflow: hidden;">
        <span>{{generator.name}}</span>
      </div>
      <div style="flex: 1; text-align: center; overflow: hidden;">
        <span>{{document.subtitle}}</span>
      </div>
      <div style="flex: 1; text-align: right; overflow: hidden;">
        <span style="font-weight: 600;">{{page.current}}/{{page.total}}</span>
      </div>
    </div>
---
```

### Template Técnico
```yaml
---
title: "Manual Técnico"
author: "Equipe Dev"
template: "technical"

header:
  enabled: true
  template: |
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 10px; color: #333; border-bottom: 2px solid #28a745; box-sizing: border-box; height: 100%; font-family: 'JetBrains Mono', monospace;">
      <div style="flex: 1; text-align: left; overflow: hidden;">
        <span style="font-weight: 600; color: #28a745;">⚙️ {{document.title}}</span>
      </div>
      <div style="flex: 1; text-align: center; overflow: hidden;">
        <span style="background: #f8f9fa; padding: 2px 6px; border-radius: 3px;">{{document.author}}</span>
      </div>
      <div style="flex: 1; text-align: right; overflow: hidden;">
        <span style="color: #666; font-size: 9px;">v{{document.version}} | {{date.formatted}}</span>
      </div>
    </div>

footer:
  enabled: true
  template: |
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 9px; color: #666; border-top: 1px solid #28a745; box-sizing: border-box; height: 100%; font-family: 'JetBrains Mono', monospace;">
      <div style="flex: 1; text-align: left; overflow: hidden;">
        <span>{{stats.words}} palavras</span>
      </div>
      <div style="flex: 1; text-align: center; overflow: hidden;">
        <span>{{document.subtitle}}</span>
      </div>
      <div style="flex: 1; text-align: right; overflow: hidden;">
        <span style="background: #28a745; color: white; padding: 1px 4px; border-radius: 2px;">{{page.current}}/{{page.total}}</span>
      </div>
    </div>
---
```

## 📐 Estrutura CSS Otimizada

### Base Structure
```css
/* Container principal - usando table para melhor compatibilidade */
display: table;
table-layout: fixed;
width: 100%;
height: 15mm;
line-height: 15mm;

/* Cada seção (esquerda, centro, direita) */
display: table-cell;
width: 33.33%;
vertical-align: middle;
overflow: hidden;
white-space: nowrap;
text-overflow: ellipsis;

/* Alinhamento específico */
text-align: left;   /* ou center, right */
padding-left: 10px;  /* só para esquerda */
padding-right: 10px; /* só para direita */
```

### Benefícios da Nova Estrutura
- **Distribuição perfeita**: 33.33% para cada seção
- **Largura total**: 100% da página sem margens laterais
- **Compatibilidade**: `display: table` funciona melhor em PDFs
- **Texto inteligente**: Corta textos longos com "..."
- **Sem quebras**: `white-space: nowrap` evita quebras indesejadas

## 🎨 Personalização Avançada

### Cores e Estilos
```yaml
# Cores personalizadas
header:
  template: |
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 10px; color: #333; border-bottom: 2px solid #custom-color; box-sizing: border-box; height: 100%;">
      <div style="flex: 1; text-align: left; overflow: hidden;">
        <span style="color: #primary-color; font-weight: 600;">{{document.title}}</span>
      </div>
      <div style="flex: 1; text-align: center; overflow: hidden;">
        <span style="background: #secondary-color; color: white; padding: 2px 6px; border-radius: 3px;">{{document.author}}</span>
      </div>
      <div style="flex: 1; text-align: right; overflow: hidden;">
        <span style="color: #muted-color;">{{date.formatted}}</span>
      </div>
    </div>
```

### Fontes Personalizadas
```css
/* Cabeçalho com fonte personalizada */
font-family: 'Inter', 'Helvetica', sans-serif;
font-family: 'JetBrains Mono', monospace; /* Para documentos técnicos */
font-family: 'Georgia', serif; /* Para documentos acadêmicos */
```

## 🧪 Testes e Validação

### Arquivo de Teste
```yaml
---
title: "Teste de Template com Título Muito Longo Que Deve Ser Cortado"
subtitle: "Subtítulo também longo para testar o overflow"
author: "Nome Completo do Autor Para Teste"
template: "corporate"
---
```

### Comandos de Teste
```bash
# Testar template padrão
python3 src/main.py docs/testes/teste-templates-melhorados.md

# Testar template corporativo
python3 src/main.py docs/testes/teste-templates-melhorados.md -t corporate

# Gerar HTML para debug
python3 src/main.py docs/testes/teste-templates-melhorados.md --html
```

## 🔗 Variáveis Disponíveis

### Documento
- `{{document.title}}` - Título do documento
- `{{document.subtitle}}` - Subtítulo
- `{{document.author}}` - Autor
- `{{document.version}}` - Versão
- `{{document.description}}` - Descrição

### Data e Hora
- `{{date.formatted}}` - 15/01/2024
- `{{date.current}}` - 2024-01-15
- `{{date.long}}` - 15 de Janeiro de 2024
- `{{date.year}}` - 2024

### Páginas
- `{{page.current}}` - Página atual
- `{{page.total}}` - Total de páginas
- `{{page.roman}}` - Numeração romana

### Gerador
- `{{generator.name}}` - Nome do gerador
- `{{generator.version}}` - Versão do gerador

### Estatísticas
- `{{stats.words}}` - Total de palavras
- `{{stats.lines}}` - Total de linhas
- `{{stats.mermaid_count}}` - Número de diagramas

## 🎯 Casos de Uso

### 1. Relatório Empresarial
```yaml
template: "corporate"
# Ideal para: relatórios, propostas, documentos corporativos
```

### 2. Trabalho Acadêmico
```yaml
template: "academic"
# Ideal para: dissertações, teses, artigos acadêmicos
```

### 3. Manual Técnico
```yaml
template: "technical"
# Ideal para: documentação de APIs, manuais, guias técnicos
```

### 4. Documento Simples
```yaml
template: "minimal"
# Ideal para: documentos pessoais, rascunhos, documentos simples
```

## 📊 Comparativo

| Template | Cabeçalho | Rodapé | Melhor Para |
|----------|-----------|--------|-------------|
| **Default** | Título \| Autor \| Data | Gerador \| Subtítulo \| Página | Documentos gerais |
| **Corporate** | 🏢 Título \| Autor \| Data | Autor \| Subtítulo • Copyright \| Página | Relatórios empresariais |
| **Academic** | Título centralizado | Autor \| Gerador \| Página | Trabalhos acadêmicos |
| **Minimal** | - | Página X | Documentos simples |

## 🚀 Migração

### Para Usuários Existentes
Os templates antigos continuam funcionando, mas recomendamos migrar para os novos templates melhorados:

```bash
# Backup dos documentos antigos
cp documento.md documento-backup.md

# Teste com novo template
python3 src/main.py documento.md --template corporate

# Comparar resultados
diff documento.pdf documento-novo.pdf
```

### Atualizações Automáticas
Os templates padrão foram automaticamente atualizados para usar a nova estrutura melhorada.

---

**Templates melhorados e prontos para uso!** 🎉 