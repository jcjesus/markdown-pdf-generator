---
# Teste dos Templates Melhorados
title: "Teste de Templates Melhorados"
subtitle: "Demonstração da Nova Diagramação"
author: "SoundLink PDF Generator"
description: "Teste dos templates com melhor distribuição de elementos"
version: "2.0"
date: "2024-01-15"
template: "corporate"
format: "A4"
orientation: "portrait"

# Margens personalizadas
margins:
  top: "25mm"
  right: "20mm"
  bottom: "25mm"
  left: "20mm"

# Teste do cabeçalho melhorado
header:
  enabled: true
  template: |
    <div style="font-size: 10px; color: #333; width: 100%; display: table; table-layout: fixed; border-bottom: 2px solid #3498db; height: 15mm; line-height: 15mm;">
      <div style="display: table-cell; width: 33.33%; text-align: left; vertical-align: middle; padding-left: 10px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
        <span style="font-weight: 600; color: #3498db;">🚀 {{document.title}}</span>
      </div>
      <div style="display: table-cell; width: 33.33%; text-align: center; vertical-align: middle; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
        <span style="font-weight: 500;">{{document.author}}</span>
      </div>
      <div style="display: table-cell; width: 33.33%; text-align: right; vertical-align: middle; padding-right: 10px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
        <span style="color: #666;">{{date.formatted}}</span>
      </div>
    </div>

# Teste do rodapé melhorado
footer:
  enabled: true
  template: |
    <div style="font-size: 9px; color: #666; width: 100%; display: table; table-layout: fixed; border-top: 1px solid #ddd; height: 15mm; line-height: 15mm;">
      <div style="display: table-cell; width: 33.33%; text-align: left; vertical-align: middle; padding-left: 10px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
        <span>v{{document.version}}</span>
      </div>
      <div style="display: table-cell; width: 33.33%; text-align: center; vertical-align: middle; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
        <span>{{document.subtitle}}</span>
      </div>
      <div style="display: table-cell; width: 33.33%; text-align: right; vertical-align: middle; padding-right: 10px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
        <span style="font-weight: 500;">Página {{page.current}} de {{page.total}}</span>
      </div>
    </div>

# Alinhamento de texto
text_alignment:
  paragraphs: "justify"
  headers: "left"
  tables: "center"
  images: "center"
---

# 🚀 Teste dos Templates Melhorados

Este documento demonstra as melhorias implementadas nos templates de cabeçalho e rodapé do **SoundLink Markdown PDF Generator**.

## 🎯 Problemas Corrigidos

### ❌ Antes (Problemas)
- Elementos todos alinhados à direita
- Conflitos entre `text-align: center` e `display: flex`
- Texto sendo cortado em títulos longos
- Distribuição desigual dos elementos

### ✅ Agora (Soluções)
- **Distribuição equilibrada**: Cada elemento ocupa 1/3 da largura
- **Flexbox otimizado**: Uso correto de `flex: 1` para cada seção
- **Texto inteligente**: Overflow com `text-overflow: ellipsis`
- **Alinhamento preciso**: Esquerda, centro, direita bem definidos

## 🎨 Templates Disponíveis

### 1. **Template Padrão (default)**
```yaml
template: "default"
```
- **Cabeçalho**: Título | Autor | Data
- **Rodapé**: Gerador | Subtítulo | Página X de Y

### 2. **Template Corporativo (corporate)**
```yaml
template: "corporate"
```
- **Cabeçalho**: 🚀 Título | Autor | Data
- **Rodapé**: Autor | Subtítulo • Copyright | Página X/Y

### 3. **Template Acadêmico (academic)**
```yaml
template: "academic"
```
- **Cabeçalho**: Título centralizado (com subtítulo)
- **Rodapé**: Autor | Gerador | Página X

### 4. **Template Minimalista (minimal)**
```yaml
template: "minimal"
```
- **Cabeçalho**: Desabilitado
- **Rodapé**: Apenas "Página X"

## 🔧 Melhorias Técnicas

### CSS Otimizado
```css
/* Estrutura melhorada */
display: flex;
justify-content: space-between;
align-items: center;
box-sizing: border-box;

/* Cada seção ocupa 1/3 da largura */
flex: 1;
text-align: left; /* ou center, right */
overflow: hidden;
white-space: nowrap;
text-overflow: ellipsis;
```

### Benefícios
- ✅ **Distribuição perfeita**: 33% esquerda, 33% centro, 33% direita
- ✅ **Texto responsivo**: Títulos longos são cortados com "..."
- ✅ **Alinhamento consistente**: Sem conflitos de CSS
- ✅ **Altura adequada**: Elementos centralizados verticalmente

## 📊 Exemplo de Dados

| Elemento | Posição | Conteúdo |
|----------|---------|----------|
| Cabeçalho Esquerda | 33% | Título do documento |
| Cabeçalho Centro | 33% | Nome do autor |
| Cabeçalho Direita | 33% | Data formatada |
| Rodapé Esquerda | 33% | Gerador + versão |
| Rodapé Centro | 33% | Subtítulo |
| Rodapé Direita | 33% | Numeração de página |

## 📝 Como Usar

### 1. **Usar template padrão melhorado**
```yaml
---
title: "Meu Documento"
author: "João Silva"
subtitle: "Teste dos Templates"
---
```

### 2. **Template corporativo**
```yaml
---
title: "Relatório Empresarial"
author: "Equipe SoundLink"
template: "corporate"
---
```

### 3. **Template personalizado**
```yaml
---
title: "Documento Personalizado"
header:
  enabled: true
  template: |
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 0 20px; font-size: 10px; color: #333; border-bottom: 1px solid #ddd; box-sizing: border-box; height: 100%;">
      <div style="flex: 1; text-align: left;">
        <span>{{document.title}}</span>
      </div>
      <div style="flex: 1; text-align: center;">
        <span>{{document.author}}</span>
      </div>
      <div style="flex: 1; text-align: right;">
        <span>{{date.formatted}}</span>
      </div>
    </div>
---
```

## 🎉 Resultado Final

Com essas melhorias, os templates agora apresentam:
- **Distribuição equilibrada** dos elementos
- **Alinhamento consistente** em todos os templates
- **Texto inteligente** que se adapta ao espaço disponível
- **Aparência profissional** em todos os formatos

---

**Teste realizado com sucesso!** ✅ 