---
title: "Teste Mermaid"
subtitle: "Verificação de Diagramas"
author: "Sistema de Teste"
description: "Teste para verificar se os diagramas Mermaid estão sendo gerados corretamente"
---

# Teste Mermaid

## Diagrama Simples

```mermaid
graph TD
    A[Início] --> B[Processo]
    B --> C[Fim]
```

## Outro Diagrama

```mermaid
sequenceDiagram
    participant A as Cliente
    participant B as Servidor
    
    A->>B: Requisição
    B-->>A: Resposta
``` 