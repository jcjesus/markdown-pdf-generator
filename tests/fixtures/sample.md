---
title: "Exemplo de Documento PDF"
subtitle: "Demonstração completa de recursos"
author: "SoundLink Team"
date: "2024-01-15"
description: "Documento de exemplo para testar geração de PDF com emojis e Mermaid"
---

# 🚀 Documento de Teste

Este é um documento de exemplo para testar a geração de PDF com **emojis** e **diagramas Mermaid**! 😊

## 📋 Índice de Recursos

- ✅ Emojis nativos
- 🎨 Diagramas Mermaid
- 📊 Tabelas
- 💻 Código
- 🔗 Links
- 📝 Listas

## 🎯 Seção 1: Emojis

Vamos testar vários emojis:

- 😀 😃 😄 😁 😆 😅 😂 🤣
- 🚀 🌟 ⭐ 💫 ✨ 🌈 🔥 💎
- 📱 💻 🖥️ ⌨️ 🖱️ 🖨️ 📡 🔌
- 🎵 🎶 🎤 🎧 🎸 🥁 🎹 🎺

## 🎨 Seção 2: Diagramas Mermaid

### Fluxograma Simples

```mermaid
graph TD
    A[Início] --> B{Decisão}
    B -->|Sim| C[Ação 1]
    B -->|Não| D[Ação 2]
    C --> E[Fim]
    D --> E
```

### Diagrama de Sequência

```mermaid
sequenceDiagram
    participant U as Usuário
    participant A as Aplicação
    participant D as Banco de Dados
    
    U->>A: Faz Login
    A->>D: Valida Credenciais
    D-->>A: Retorna Resultado
    A-->>U: Resposta do Login
```

### Gráfico de Gantt

```mermaid
gantt
    title Cronograma do Projeto
    dateFormat  YYYY-MM-DD
    section Planejamento
    Análise           :done, des1, 2024-01-01, 2024-01-05
    Design            :done, des2, 2024-01-06, 2024-01-10
    section Desenvolvimento
    Backend           :active, dev1, 2024-01-11, 2024-01-20
    Frontend          :dev2, 2024-01-21, 2024-01-30
    section Testes
    Testes Unitários  :test1, after dev2, 5d
    Testes Integração :test2, after test1, 3d
```

## 📊 Seção 3: Tabelas

| Recurso | Status | Prioridade | Emoji |
|---------|--------|------------|-------|
| Emojis | ✅ Funcionando | Alta | 😊 |
| Mermaid | ✅ Funcionando | Alta | 🎨 |
| Tabelas | ✅ Funcionando | Média | 📊 |
| Código | ✅ Funcionando | Média | 💻 |
| Links | ✅ Funcionando | Baixa | 🔗 |

## 💻 Seção 4: Código

### Python
```python
def generate_pdf(markdown_content: str) -> bool:
    """
    Gera PDF a partir de conteúdo Markdown
    """
    try:
        # Processar markdown
        parser = MarkdownParser()
        data = parser.parse(markdown_content)
        
        # Gerar PDF
        generator = PDFGenerator()
        return generator.create_pdf(data)
    except Exception as e:
        print(f"Erro: {e}")
        return False
```

### JavaScript
```javascript
const generatePDF = async (markdown) => {
    try {
        const response = await fetch('/api/generate-pdf', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ markdown })
        });
        
        return await response.blob();
    } catch (error) {
        console.error('Erro ao gerar PDF:', error);
        return null;
    }
};
```

## 🔗 Seção 5: Links e Referências

- [SoundLink Website](https://soundlink.com.br) 🌐
- [GitHub Repository](https://github.com/soundlink/markdown-pdf-generator) 📂
- [Documentation](https://docs.soundlink.com.br) 📚

## 📝 Seção 6: Listas

### Lista Ordenada
1. 🥇 Primeiro item
2. 🥈 Segundo item
3. 🥉 Terceiro item

### Lista Não Ordenada
- 🔸 Item A
- 🔹 Item B
- 🔺 Item C

### Lista de Tarefas
- [x] ✅ Tarefa concluída
- [x] ✅ Outra tarefa concluída
- [ ] ⏳ Tarefa pendente
- [ ] ⏳ Mais uma tarefa pendente

## 📋 Seção 7: Blockquotes

> 💡 **Dica Importante**: Este é um exemplo de blockquote com emoji!
> 
> Blockquotes são úteis para destacar informações importantes ou citações.

> 🚨 **Aviso**: Sempre teste seus documentos antes de finalizar!

## 🌟 Seção 8: Outros Elementos

### Texto Formatado
- **Negrito com emoji** 💪
- *Itálico com emoji* 🤌
- ~~Tachado com emoji~~ ❌
- `código inline` 💻

### Linha Horizontal
---

### Emojis Complexos
👨‍💻 👩‍💻 👨‍🎨 👩‍🎨 👨‍🔬 👩‍🔬 👨‍🚀 👩‍🚀

## 🎯 Conclusão

Este documento demonstra todos os recursos principais:

1. ✅ **Emojis**: Funcionando perfeitamente
2. ✅ **Mermaid**: Diagramas renderizados
3. ✅ **Tabelas**: Formatação profissional
4. ✅ **Código**: Syntax highlighting
5. ✅ **Links**: Funcionais
6. ✅ **Listas**: Todos os tipos
7. ✅ **Formatação**: Completa

🎉 **Sucesso!** O gerador de PDF está funcionando perfeitamente! 🚀

---

*Gerado por SoundLink Markdown PDF Generator* 📄✨ 