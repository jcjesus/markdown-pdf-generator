#!/usr/bin/env python3
"""
Professional HTML Generator with templates and styling
"""

import os
import tempfile
from typing import Dict, Optional
from jinja2 import Template
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class HTMLGenerator:
    """
    Generate professional HTML from parsed markdown with embedded styles
    """
    
    def __init__(self, custom_css: Optional[str] = None):
        """
        Initialize HTML generator
        
        Args:
            custom_css: Optional custom CSS to override default styles
        """
        self.custom_css = custom_css
        self.html_template = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="{{ metadata.get('author', 'SoundLink') }}">
    <meta name="description" content="{{ metadata.get('description', 'Professional PDF Document') }}">
    <title>{{ metadata.get('title', 'Document') }}</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet">
    
    <!-- Mermaid -->
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10.6.1/dist/mermaid.min.js"></script>
    
    <style>
        {{ css_content }}
    </style>
</head>
<body>
    <div class="document-container">
        {% if metadata.get('title') %}
        <header class="document-header">
            <h1 class="document-title">{{ metadata.title }}</h1>
            {% if metadata.get('subtitle') %}
            <p class="document-subtitle">{{ metadata.subtitle }}</p>
            {% endif %}
            {% if metadata.get('author') %}
            <p class="document-author">{{ metadata.author }}</p>
            {% endif %}
            {% if metadata.get('date') %}
            <p class="document-date">{{ metadata.date }}</p>
            {% endif %}
        </header>
        {% endif %}
        
        {% if toc %}
        <nav class="table-of-contents">
            <h2>Índice</h2>
            {{ toc_formatted|safe }}
        </nav>
        {% endif %}
        
        <main class="document-content">
            {{ content|safe }}
        </main>
        
        {% if stats %}
        <footer class="document-footer">
            <div class="stats">
                <span>{{ stats.words }} palavras</span>
                <span>{{ stats.lines }} linhas</span>
                {% if stats.mermaid_count > 0 %}
                <span>{{ stats.mermaid_count }} diagramas</span>
                {% endif %}
            </div>
            <div class="generated-by">
                <p>Gerado por <strong>SoundLink PDF Generator</strong></p>
            </div>
        </footer>
        {% endif %}
    </div>
    
    <!-- Mermaid initialization -->
    <script>
        mermaid.initialize({
            startOnLoad: true,
            theme: 'default',
            themeVariables: {
                primaryColor: '#3498db',
                primaryTextColor: '#2c3e50',
                primaryBorderColor: '#2980b9',
                lineColor: '#34495e',
                sectionBkgColor: '#ecf0f1',
                altSectionBkgColor: '#bdc3c7',
                gridColor: '#95a5a6',
                secondaryColor: '#e74c3c',
                tertiaryColor: '#f39c12'
            },
            flowchart: {
                useMaxWidth: true,
                htmlLabels: true,
                curve: 'basis'
            }
        });
    </script>
</body>
</html>
        """
    
    def get_default_css(self) -> str:
        """
        Get default professional CSS styles
        
        Returns:
            CSS content as string
        """
        return """
/* Reset and Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    color: #2c3e50;
    background: #ffffff;
    font-size: 12px;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* Document Container */
.document-container {
    max-width: 210mm;
    margin: 0 auto;
    padding: 20mm;
    background: white;
    box-shadow: 0 0 20px rgba(0,0,0,0.1);
    min-height: 297mm;
}

/* Document Header */
.document-header {
    text-align: center;
    margin-bottom: 3rem;
    padding-bottom: 2rem;
    border-bottom: 3px solid #3498db;
}

.document-title {
    font-size: 1.8rem;
    font-weight: 700;
    color: #2c3e50;
    margin-bottom: 1rem;
    background: linear-gradient(135deg, #3498db, #2980b9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.document-subtitle {
    font-size: 1.2rem;
    color: #7f8c8d;
    margin-bottom: 1rem;
    font-weight: 400;
}

.document-author {
    font-size: 1.1rem;
    color: #34495e;
    font-weight: 500;
}

.document-date {
    font-size: 0.9rem;
    color: #95a5a6;
    margin-top: 0.5rem;
}

/* Table of Contents */
.table-of-contents {
    background: #f8f9fa;
    border: 1px solid #dee2e6;
    padding: 1.5rem;
    margin: 2rem 0;
    border-radius: 8px;
    page-break-after: always;
}

.table-of-contents h2 {
    color: #2c3e50;
    margin-bottom: 1.5rem;
    font-size: 1.2rem;
    text-align: center;
    border-bottom: 2px solid #3498db;
    padding-bottom: 0.5rem;
}

.table-of-contents ul {
    list-style: none;
    padding-left: 0;
}

.table-of-contents li {
    margin: 0.3rem 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.2rem 0;
    border-bottom: 1px dotted #ccc;
}

.table-of-contents li:last-child {
    border-bottom: none;
}

.table-of-contents a {
    color: #2c3e50;
    text-decoration: none;
    transition: color 0.2s;
    flex: 1;
    font-size: 0.9rem;
}

.table-of-contents a:hover {
    color: #3498db;
}

/* TOC indentation for different levels */
.table-of-contents .toc-h1 { padding-left: 0; font-weight: 600; }
.table-of-contents .toc-h2 { padding-left: 1rem; }
.table-of-contents .toc-h3 { padding-left: 2rem; font-size: 0.85rem; }
.table-of-contents .toc-h4 { padding-left: 3rem; font-size: 0.8rem; }
.table-of-contents .toc-h5 { padding-left: 4rem; font-size: 0.75rem; }
.table-of-contents .toc-h6 { padding-left: 5rem; font-size: 0.7rem; }

/* TOC page numbers */
.toc-page-number {
    color: #7f8c8d;
    font-size: 0.8rem;
    margin-left: 1rem;
    min-width: 2rem;
    text-align: right;
}

/* Content Styles */
.document-content {
    margin: 2rem 0;
}

/* Headers */
h1, h2, h3, h4, h5, h6 {
    color: #2c3e50;
    margin: 2rem 0 1rem 0;
    font-weight: 600;
    line-height: 1.2;
}

h1 { font-size: 1.4rem; border-bottom: 2px solid #3498db; padding-bottom: 0.5rem; }
h2 { font-size: 1.2rem; border-bottom: 1px solid #bdc3c7; padding-bottom: 0.3rem; }
h3 { font-size: 1.1rem; color: #34495e; }
h4 { font-size: 1rem; color: #34495e; }
h5 { font-size: 0.95rem; color: #7f8c8d; }
h6 { font-size: 0.9rem; color: #7f8c8d; }

/* Paragraphs */
p {
    margin: 1rem 0;
    text-align: justify;
    hyphens: auto;
}

/* Lists */
ul, ol {
    margin: 1rem 0;
    padding-left: 2rem;
}

li {
    margin: 0.5rem 0;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1.5rem 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    border-radius: 8px;
    overflow: hidden;
}

th, td {
    padding: 0.75rem;
    text-align: left;
    border-bottom: 1px solid #ecf0f1;
}

th {
    background: linear-gradient(135deg, #3498db, #2980b9);
    color: white;
    font-weight: 600;
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

tr:hover {
    background: #f8f9fa;
}

/* Code Blocks */
pre {
    background: #2c3e50;
    color: #ecf0f1;
    padding: 1.5rem;
    border-radius: 8px;
    overflow-x: auto;
    margin: 1.5rem 0;
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
    font-size: 0.9rem;
    line-height: 1.4;
}

code {
    background: #ecf0f1;
    color: #e74c3c;
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
    font-size: 0.9rem;
}

pre code {
    background: none;
    color: inherit;
    padding: 0;
}

/* Blockquotes */
blockquote {
    border-left: 4px solid #3498db;
    padding-left: 1.5rem;
    margin: 1.5rem 0;
    color: #7f8c8d;
    font-style: italic;
    background: #f8f9fa;
    padding: 1rem 1.5rem;
    border-radius: 0 8px 8px 0;
}

/* Links */
a {
    color: #3498db;
    text-decoration: none;
    transition: color 0.2s;
}

a:hover {
    color: #2980b9;
    text-decoration: underline;
}

/* Hide permalink symbols */
.headerlink, .anchorlink {
    display: none !important;
}

/* Hide permalink symbols in headings */
h1 .headerlink, h2 .headerlink, h3 .headerlink, 
h4 .headerlink, h5 .headerlink, h6 .headerlink {
    display: none !important;
}

/* Images */
img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    margin: 1rem 0;
}

/* Mermaid Diagrams */
.mermaid {
    text-align: center;
    margin: 2rem 0;
    background: #f8f9fa;
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid #ecf0f1;
}

.mermaid svg {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0 auto;
}

.mermaid-diagram {
    text-align: center;
    margin: 2rem 0;
    background: #f8f9fa;
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid #ecf0f1;
    page-break-inside: avoid;
}

.mermaid-diagram svg {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0 auto;
}

.mermaid-placeholder {
    text-align: center;
    margin: 2rem 0;
    background: #f8f9fa;
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid #ecf0f1;
    min-height: 100px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #7f8c8d;
    font-style: italic;
}

.mermaid-placeholder::before {
    content: "🎨 Carregando diagrama...";
}

/* Horizontal Rules */
hr {
    border: none;
    height: 2px;
    background: linear-gradient(to right, #3498db, #2980b9);
    margin: 2rem 0;
    border-radius: 1px;
}

/* Strong and Emphasis */
strong, b {
    font-weight: 600;
    color: #2c3e50;
}

em, i {
    font-style: italic;
    color: #34495e;
}

/* Document Footer */
.document-footer {
    margin-top: 3rem;
    padding-top: 2rem;
    border-top: 1px solid #ecf0f1;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.9rem;
    color: #7f8c8d;
}

.stats span {
    margin-right: 1rem;
}

.generated-by {
    font-size: 0.8rem;
}

/* Print Styles */
@media print {
    body {
        background: white !important;
        color: #000 !important;
        font-size: 10pt;
        line-height: 1.4;
    }
    
    .document-container {
        max-width: none;
        margin: 0;
        padding: 0;
        box-shadow: none;
        min-height: auto;
    }
    
    .document-header {
        page-break-after: avoid;
    }
    
    h1, h2, h3, h4, h5, h6 {
        page-break-after: avoid;
    }
    
    pre, blockquote, table {
        page-break-inside: avoid;
    }
    
    .table-of-contents {
        page-break-after: always;
    }
    
    .document-footer {
        page-break-before: avoid;
        margin-top: 2rem;
    }
    
    a {
        color: #000 !important;
        text-decoration: none !important;
    }
    
    .mermaid {
        page-break-inside: avoid;
    }
}

/* Responsive Design */
@media (max-width: 768px) {
    .document-container {
        padding: 1rem;
    }
    
    .document-title {
        font-size: 2rem;
    }
    
    h1 { font-size: 1.8rem; }
    h2 { font-size: 1.5rem; }
    h3 { font-size: 1.3rem; }
    
    .document-footer {
        flex-direction: column;
        align-items: flex-start;
    }
    
    .stats {
        margin-bottom: 1rem;
    }
}
        """
    
    def inject_mermaid_svgs(self, html_content: str, mermaid_svgs: Dict[str, str]) -> str:
        """
        Inject rendered Mermaid SVGs into HTML placeholders
        
        Args:
            html_content: HTML content with mermaid placeholders
            mermaid_svgs: Dictionary mapping diagram IDs to SVG content
            
        Returns:
            HTML with SVGs injected
        """
        for diagram_id, svg_content in mermaid_svgs.items():
            placeholder = f'<div id="{diagram_id}" class="mermaid-placeholder"></div>'
            replacement = f'<div class="mermaid-diagram" id="{diagram_id}">{svg_content}</div>'
            html_content = html_content.replace(placeholder, replacement)
        
        return html_content
    
    def format_toc_with_page_numbers(self, toc_html: str) -> str:
        """
        Format TOC HTML to include page numbers and better styling
        
        Args:
            toc_html: Original TOC HTML from markdown parser
            
        Returns:
            Formatted TOC HTML with page numbers and styling
        """
        if not toc_html:
            return ""
        
        import re
        from bs4 import BeautifulSoup
        
        try:
            # Parse the TOC HTML
            soup = BeautifulSoup(toc_html, 'html.parser')
            
            # Find all list items
            for li in soup.find_all('li'):
                # Add CSS classes based on heading level
                link = li.find('a')
                if link and link.get('href'):
                    # Extract heading level from href (e.g., #heading-1)
                    href = link.get('href', '')
                    
                    # Determine level based on nesting
                    level = len(li.find_parents('ul')) + 1
                    li['class'] = li.get('class', []) + [f'toc-h{level}']
                    
                    # Add page number placeholder (will be calculated during PDF generation)
                    page_span = soup.new_tag('span', **{'class': 'toc-page-number'})
                    page_span.string = '•'  # Placeholder, PDF generator will replace
                    li.append(page_span)
            
            return str(soup)
            
        except Exception as e:
            logger.warning(f"Failed to format TOC: {e}")
            return toc_html
    
    def generate_html(self, parsed_data: Dict, mermaid_svgs: Optional[Dict[str, str]] = None) -> str:
        """
        Generate complete HTML document from parsed markdown data
        
        Args:
            parsed_data: Parsed markdown data from MarkdownParser
            mermaid_svgs: Optional dictionary of rendered Mermaid SVGs
            
        Returns:
            Complete HTML document as string
        """
        logger.info("Generating HTML document...")
        
        # Prepare template data
        template_data = {
            'content': parsed_data['html'],
            'toc': parsed_data['toc'],
            'toc_formatted': self.format_toc_with_page_numbers(parsed_data['toc']),
            'metadata': parsed_data['metadata'],
            'stats': parsed_data['stats'],
            'css_content': self.custom_css or self.get_default_css()
        }
        
        # Render HTML template
        template = Template(self.html_template)
        html_content = template.render(**template_data)
        
        # Inject Mermaid SVGs if provided
        if mermaid_svgs:
            html_content = self.inject_mermaid_svgs(html_content, mermaid_svgs)
        
        logger.info("HTML generation complete")
        return html_content
    
    def create_temp_html_file(self, html_content: str) -> str:
        """
        Create temporary HTML file
        
        Args:
            html_content: Complete HTML content
            
        Returns:
            Path to temporary HTML file
        """
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as f:
            f.write(html_content)
            return f.name
    
    def validate_html(self, html_content: str) -> bool:
        """
        Basic HTML validation
        
        Args:
            html_content: HTML content to validate
            
        Returns:
            True if valid, False otherwise
        """
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')
            return soup.title is not None
        except Exception as e:
            logger.error(f"HTML validation failed: {e}")
            return False 