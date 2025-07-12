# 📚 Documentação - Markdown PDF Generator

## 🎯 Guias Rápidos

### 🚀 **Começar Agora**
- [**Como Configurar Variáveis (INÍCIO AQUI)**](README-variaveis.md) - Guia prático e simples
- [**Configuração Completa de Variáveis**](configuracao-variaveis.md) - Documentação detalhada

## 📋 Conteúdo da Documentação

### 🔧 **Configuração Básica**
1. **[README-variaveis.md](README-variaveis.md)** - Guia prático para iniciantes
   - Como configurar variáveis no PDF
   - Exemplos práticos
   - Comandos básicos
   - Solução de problemas

2. **[configuracao-variaveis.md](configuracao-variaveis.md)** - Documentação completa
   - Todas as variáveis disponíveis
   - Templates avançados
   - Personalização completa
   - Configurações avançadas

## 🎨 Templates Disponíveis

| Template | Uso | Descrição |
|----------|-----|-----------|
| `default` | Documentos gerais | Cabeçalho e rodapé padrão |
| `corporate` | Relatórios empresariais | Layout corporativo |
| `academic` | Documentos acadêmicos | Estilo acadêmico |
| `minimal` | Documentos simples | Apenas numeração |

## 📂 Arquivos de Exemplo

### 🎯 **Para Iniciantes**
```bash
# Exemplo básico - copie e edite
cp examples/exemplo-simples.md meu-documento.md
```

### 🚀 **Para Uso Avançado**
```bash
# Exemplo completo com todos os recursos
cp examples/exemplo-completo.md meu-relatorio.md
```

## 🛠️ Comandos Essenciais

### **Gerar PDF:**
```bash
python3 src/main.py documento.md
```

### **Debug (gerar HTML):**
```bash
python3 src/main.py documento.md --html
```

### **Logs detalhados:**
```bash
python3 src/main.py documento.md --verbose
```

## 🔍 Estrutura do Projeto

```
docs/
├── README.md                    # Este arquivo
├── README-variaveis.md          # Guia prático ⭐
├── configuracao-variaveis.md    # Documentação completa
└── ...

examples/
├── exemplo-simples.md           # Exemplo básico ⭐
├── exemplo-completo.md          # Exemplo avançado
└── ...

config.yaml                      # Configurações globais
```

## 🆘 Precisa de Ajuda?

### **Problemas Comuns:**
1. **Variável não aparece** → Verifique aspas no YAML
2. **Erro de sintaxe** → Use `--verbose` para debug
3. **Arquivo não encontrado** → Verifique o caminho

### **Ordem de Leitura Recomendada:**
1. 📖 [README-variaveis.md](README-variaveis.md) - **COMECE AQUI**
2. 🧪 Teste com `examples/exemplo-simples.md`
3. 📚 [configuracao-variaveis.md](configuracao-variaveis.md) - Para usar avançado
4. 🚀 Explore `examples/exemplo-completo.md`

## 🎯 Próximos Passos

1. **Leia o guia prático:** [README-variaveis.md](README-variaveis.md)
2. **Teste o exemplo simples:** `examples/exemplo-simples.md`
3. **Crie seu primeiro documento**
4. **Explore recursos avançados quando precisar**

---

**💡 Dica:** Se é sua primeira vez, comece com [README-variaveis.md](README-variaveis.md) - é o guia mais prático! 🚀 