# 🔧 Como Configurar Variáveis no PDF

## 📋 Resumo Rápido

Para que suas informações apareçam no **cabeçalho** e **rodapé** do PDF, adicione um bloco YAML no início do seu arquivo Markdown:

```yaml
---
title: "Título do Documento"
subtitle: "Subtítulo"
author: "Seu Nome"
description: "Descrição do documento"
version: "1.0"
---
```

## 🎯 Onde Aparece Cada Variável

### 📄 **Cabeçalho (topo da página)**
```
Título do Documento  |  Seu Nome  |  15/01/2024
```

### 📄 **Rodapé (parte inferior)**
```
SoundLink PDF Generator v1.0.0  |  Subtítulo  |  Página 1 de 3
```

## 🚀 Exemplo Prático

### 1. **Crie um arquivo `meu-documento.md`:**
```markdown
---
title: "Relatório de Vendas"
subtitle: "Janeiro 2024"
author: "João Silva"
description: "Relatório mensal de vendas"
version: "1.0"
---

# Relatório de Vendas

Conteúdo do seu relatório aqui...
```

### 2. **Gere o PDF:**
```bash
python3 src/main.py meu-documento.md
```

### 3. **Resultado:**
- **Cabeçalho:** `Relatório de Vendas | João Silva | 15/01/2024`
- **Rodapé:** `SoundLink PDF Generator v1.0.0 | Janeiro 2024 | Página 1 de 1`

## 📝 Variáveis Mais Usadas

| Variável | Onde Aparece | Exemplo |
|----------|--------------|---------|
| `title` | Cabeçalho (esquerda) | "Relatório de Vendas" |
| `subtitle` | Rodapé (centro) | "Janeiro 2024" |
| `author` | Cabeçalho (centro) | "João Silva" |
| `description` | Metadados do PDF | "Relatório mensal..." |
| `version` | Versão do documento | "1.0" |
| `date` | Data personalizada | "2024-01-15" |

## 🎨 Templates Disponíveis

### **Template Padrão (recomendado)**
```yaml
---
title: "Meu Documento"
author: "Meu Nome"
# Não precisa especificar template
---
```

### **Template Corporativo**
```yaml
---
title: "Relatório Corporativo"
author: "Equipe Comercial"
template: "corporate"
---
```

### **Template Minimalista**
```yaml
---
title: "Documento Simples"
template: "minimal"
---
```

## ⚠️ Dicas Importantes

### ✅ **Faça Assim:**
```yaml
---
title: "Título com aspas"
author: "Nome completo"
version: "1.0"
---
```

### ❌ **Evite:**
```yaml
---
title: Título sem aspas
author: 
version: 
---
```

## 📂 Arquivos de Exemplo

### 1. **Exemplo Simples**
```bash
# Copie e edite este arquivo
cp examples/exemplo-simples.md meu-documento.md
```

### 2. **Exemplo Completo**
```bash
# Para documentos mais complexos
cp examples/exemplo-completo.md meu-relatorio.md
```

## 🛠️ Comandos Úteis

### **Gerar PDF básico:**
```bash
python3 src/main.py documento.md
```

### **Gerar com nome específico:**
```bash
python3 src/main.py documento.md -o meu-relatorio.pdf
```

### **Gerar HTML para debug:**
```bash
python3 src/main.py documento.md --html
```

### **Ver logs detalhados:**
```bash
python3 src/main.py documento.md --verbose
```

## 🔍 Verificação Rápida

### Como saber se está funcionando:

1. **Gere o HTML primeiro:**
```bash
python3 src/main.py documento.md --html
```

2. **Abra o arquivo `.html` gerado no navegador**

3. **Verifique se as informações estão corretas**

4. **Depois gere o PDF:**
```bash
python3 src/main.py documento.md
```

## 🆘 Problemas Comuns

### **Variável não aparece no PDF:**
- Verifique se está usando aspas no YAML
- Confirme que o bloco YAML está no início do arquivo
- Use `--verbose` para ver mensagens de erro

### **Caracteres especiais:**
- Use UTF-8 normalmente: `"João"`, `"análise"`
- Emojis funcionam: `"Relatório 📊"`

### **Data não está certa:**
- Para usar data atual: não inclua `date`
- Para data específica: `date: "2024-01-15"`

## 🎯 Próximos Passos

1. **Teste com exemplo simples:**
```bash
python3 src/main.py examples/exemplo-simples.md
```

2. **Copie e edite para seu uso:**
```bash
cp examples/exemplo-simples.md meu-documento.md
# Edite meu-documento.md
python3 src/main.py meu-documento.md
```

3. **Explore templates mais avançados:**
```bash
python3 src/main.py examples/exemplo-completo.md
```

## 📚 Documentação Completa

Para configurações avançadas, consulte:
- `docs/configuracao-variaveis.md` - Documentação completa
- `config.yaml` - Configurações globais
- `examples/` - Mais exemplos práticos

---

**🚀 Pronto para começar? Use o exemplo simples e personalize!** 