---
title: "Meu Primeiro Documento"
subtitle: "Exemplo Básico"
author: "Seu Nome"
description: "Exemplo simples de configuração de variáveis"
version: "1.0"
---

# 📄 Meu Primeiro Documento

Este é um exemplo simples de como configurar variáveis para serem impressas no PDF.

## 🎯 O que vai aparecer no PDF

Com as configurações do cabeçalho YAML acima, o PDF será gerado com:

### 📋 Cabeçalho
- **Esquerda:** Meu Primeiro Documento
- **Centro:** Seu Nome  
- **Direita:** Data atual (ex: 15/01/2024)

### 📋 Rodapé
- **Esquerda:** SoundLink PDF Generator v1.0.0
- **Centro:** Exemplo Básico
- **Direita:** Página 1 de 2

## 🔧 Configuração Básica

```yaml
---
title: "Meu Primeiro Documento"     # Aparece no cabeçalho esquerdo
subtitle: "Exemplo Básico"         # Aparece no rodapé centro
author: "Seu Nome"                 # Aparece no cabeçalho centro
description: "Exemplo simples..."  # Usado nos metadados do PDF
version: "1.0"                     # Versão do documento
---
```

## 😊 Teste com Emojis

Os emojis funcionam perfeitamente: 🚀 📊 💡 ✅ 🎯

## 📊 Teste com Tabela

| Item | Valor | Status |
|------|-------|--------|
| A    | 100   | ✅     |
| B    | 200   | ⏳     |
| C    | 300   | ❌     |

## 💻 Teste com Código

```python
def hello_world():
    print("Olá, mundo! 🌍")
    return "PDF gerado com sucesso!"
```

## 📝 Para Testar

1. Salve este arquivo como `exemplo-simples.md`
2. Execute: `python3 src/main.py exemplo-simples.md`
3. Veja o PDF gerado com suas variáveis!

---

**Gerado com SoundLink PDF Generator** 🚀 