# 📋 Configuração de Variáveis para PDF

## 🎯 Visão Geral

O **Markdown PDF Generator** permite configurar variáveis dinâmicas que são automaticamente impressas no cabeçalho e rodapé do PDF. Essas variáveis podem ser definidas através de:

1. **YAML Front Matter** no arquivo Markdown
2. **Arquivo config.yaml** (configuração global)
3. **Argumentos da linha de comando** (sobrescrevem as outras)

## 🔧 YAML Front Matter

### Formato Básico
No início do seu arquivo Markdown, adicione um bloco YAML entre `---`:

```yaml
---
title: "Título do Documento"
subtitle: "Subtítulo do Documento"
author: "Nome do Autor"
description: "Descrição do documento"
keywords: "palavras, chave, separadas, vírgula"
version: "1.0"
date: "2024-01-15"
template: "corporate"
format: "A4"
orientation: "portrait"
---
```

### Variáveis Disponíveis

#### 📄 **Documento (`document.*`)**
```yaml
title: "Relatório Mensal"           # {{document.title}}
subtitle: "Janeiro 2024"           # {{document.subtitle}}
author: "João Silva"               # {{document.author}}
description: "Relatório de vendas" # {{document.description}}
keywords: "vendas, relatório"      # {{document.keywords}}
version: "2.1"                     # {{document.version}}
```

#### 📅 **Data (`date.*`)**
```yaml
date: "2024-01-15"                 # Data personalizada
# Se não especificar, usa a data atual
```

Variáveis de data disponíveis:
- `{{date.current}}` - Data atual (YYYY-MM-DD)
- `{{date.formatted}}` - Data formatada (DD/MM/YYYY)
- `{{date.long}}` - Data por extenso
- `{{date.iso}}` - Data no formato ISO
- `{{date.year}}` - Ano atual
- `{{date.month}}` - Mês atual
- `{{date.day}}` - Dia atual

#### 📄 **Página (`page.*`)**
Controladas automaticamente pelo sistema:
- `{{page.current}}` - Página atual
- `{{page.total}}` - Total de páginas
- `{{page.roman}}` - Página em romano (i, ii, iii)
- `{{page.alpha}}` - Página em letras (a, b, c)

#### 🚀 **Gerador (`generator.*`)**
Informações do sistema:
- `{{generator.name}}` - Nome do gerador
- `{{generator.version}}` - Versão do gerador
- `{{generator.url}}` - URL do projeto

#### 📊 **Estatísticas (`stats.*`)**
Calculadas automaticamente:
- `{{stats.words}}` - Total de palavras
- `{{stats.lines}}` - Total de linhas
- `{{stats.chars}}` - Total de caracteres
- `{{stats.mermaid_count}}` - Número de diagramas Mermaid

## 🎨 Templates Disponíveis

### 1. **Template Padrão (default)**
```yaml
---
template: "default"
---
```

**Cabeçalho:** Título | Autor | Data  
**Rodapé:** Gerador | Subtítulo | Página X de Y

### 2. **Template Corporativo (corporate)**
```yaml
---
template: "corporate"
---
```

**Cabeçalho:** Logo | Título | Data  
**Rodapé:** Confidencial | Copyright | Autor | Página

### 3. **Template Acadêmico (academic)**
```yaml
---
template: "academic"
---
```

**Cabeçalho:** Título centralizado  
**Rodapé:** Autor | Página

### 4. **Template Minimalista (minimal)**
```yaml
---
template: "minimal"
---
```

**Cabeçalho:** Desabilitado  
**Rodapé:** Apenas número da página

## 📝 Exemplos Práticos

### 1. **Relatório Empresarial**
```yaml
---
title: "Relatório Trimestral"
subtitle: "Q1 2024"
author: "Equipe Comercial"
description: "Análise de vendas e performance"
keywords: "vendas, performance, relatório"
version: "1.0"
template: "corporate"
format: "A4"
orientation: "portrait"
---
```

### 2. **Documento Acadêmico**
```yaml
---
title: "Análise de Algoritmos"
subtitle: "Complexidade Computacional"
author: "Maria Santos"
description: "Estudo sobre algoritmos de ordenação"
keywords: "algoritmos, complexidade, ordenação"
version: "2.0"
template: "academic"
format: "A4"
---
```

### 3. **Manual Técnico**
```yaml
---
title: "Manual de Instalação"
subtitle: "Sistema XYZ v3.0"
author: "Equipe de Desenvolvimento"
description: "Guia completo de instalação"
version: "3.0"
template: "default"
format: "A4"
orientation: "portrait"
---
```

## 🎯 Personalização Avançada

### 1. **Modificar Templates no config.yaml**
```yaml
templates:
  custom:
    header:
      template: |
        <div style="text-align: center; font-size: 12px; color: #333;">
          <strong>{{document.title}}</strong> - {{document.version}}
        </div>
    footer:
      template: |
        <div style="display: flex; justify-content: space-between; font-size: 10px;">
          <span>{{document.author}}</span>
          <span>{{date.formatted}}</span>
          <span>{{page.current}}/{{page.total}}</span>
        </div>
```

### 2. **Usar Template Customizado**
```yaml
---
title: "Meu Documento"
template: "custom"
---
```

## 🔍 Verificação de Variáveis

### Como Verificar se as Variáveis Estão Funcionando

1. **Gerar HTML para debug:**
```bash
python3 src/main.py documento.md --html
```

2. **Verificar logs detalhados:**
```bash
python3 src/main.py documento.md --verbose
```

3. **Testar com arquivo de exemplo:**
```bash
python3 src/main.py examples/exemplo-completo.md -o teste.pdf
```

## ⚠️ Problemas Comuns

### 1. **Variável não aparece no PDF**
```yaml
# ❌ Errado
title: Sem aspas pode causar problemas

# ✅ Correto
title: "Título com aspas"
```

### 2. **Caracteres especiais**
```yaml
# ✅ Use caracteres UTF-8 normalmente
title: "Relatório com acentos: análise"
author: "João da Silva"
```

### 3. **Datas inválidas**
```yaml
# ❌ Formato inválido
date: "15/01/2024"

# ✅ Formato correto
date: "2024-01-15"
```

### 4. **Template não encontrado**
```yaml
# ❌ Template inexistente
template: "inexistente"

# ✅ Templates disponíveis
template: "default"    # ou "corporate", "academic", "minimal"
```

## 🎨 Exemplo Completo

```yaml
---
title: "Relatório de Vendas Q1 2024"
subtitle: "Análise Trimestral de Performance"
author: "João Silva - Gerente Comercial"
description: "Relatório detalhado das vendas do primeiro trimestre"
keywords: "vendas, performance, análise, Q1, 2024"
version: "2.1"
date: "2024-03-31"
template: "corporate"
format: "A4"
orientation: "portrait"
---

# Conteúdo do seu documento aqui...
```

**Resultado no PDF:**
- **Cabeçalho:** Logo | Relatório de Vendas Q1 2024 | 31/03/2024
- **Rodapé:** Confidencial | SoundLink © 2024 | João Silva | 1/5

## 🚀 Dicas Avançadas

### 1. **Variáveis Condicionais**
```yaml
# Se não especificar author, usa "SoundLink" como padrão
author: ""  # Deixa vazio para usar padrão
```

### 2. **Múltiplas Palavras-chave**
```yaml
keywords: "vendas, performance, análise, trimestre, 2024"
```

### 3. **Versioning Semântico**
```yaml
version: "1.0.0"  # Major.Minor.Patch
```

### 4. **Datas Personalizadas**
```yaml
date: "2024-01-15"  # Usa esta data em vez da atual
```

---

**💡 Dica:** Use o arquivo `examples/exemplo-completo.md` como base para seus documentos! 