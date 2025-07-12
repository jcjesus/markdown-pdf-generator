#!/usr/bin/env python3
"""
Configuration Manager for PDF generation settings
"""

import os
import yaml
from typing import Dict, Any, Optional
from datetime import datetime
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class TemplateVariables:
    """
    Manages dynamic variables for header/footer templates
    """
    
    def __init__(self, document_metadata: Dict, stats: Dict):
        self.document = document_metadata
        self.stats = stats
        self._current_page = 1
        self._total_pages = 1
        
    def set_page_info(self, current: int, total: int):
        """Set current page and total pages"""
        self._current_page = current
        self._total_pages = total
    
    def get_variables(self) -> Dict[str, Any]:
        """
        Get all available template variables
        
        Returns:
            Dictionary with all template variables
        """
        now = datetime.now()
        
        return {
            'document': {
                'title': self.document.get('title', 'Documento'),
                'subtitle': self.document.get('subtitle', ''),
                'author': self.document.get('author', 'SoundLink'),
                'description': self.document.get('description', ''),
                'keywords': self.document.get('keywords', ''),
                'version': self.document.get('version', '1.0'),
            },
            'date': {
                'current': now.strftime('%Y-%m-%d'),
                'formatted': now.strftime('%d/%m/%Y'),
                'long': now.strftime('%d de %B de %Y'),
                'iso': now.isoformat(),
                'year': now.year,
                'month': now.month,
                'day': now.day,
            },
            'page': {
                'current': self._current_page,
                'total': self._total_pages,
                'roman': self._to_roman(self._current_page),
                'alpha': self._to_alpha(self._current_page),
            },
            'generator': {
                'name': 'SoundLink PDF Generator',
                'version': '1.0.0',
                'url': 'https://github.com/soundlink/markdown-pdf-generator',
            },
            'stats': {
                'words': self.stats.get('words', 0),
                'lines': self.stats.get('lines', 0),
                'chars': self.stats.get('chars', 0),
                'mermaid_count': self.stats.get('mermaid_count', 0),
            }
        }
    
    def _to_roman(self, num: int) -> str:
        """Convert number to roman numerals"""
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syms[i]
                num -= val[i]
            i += 1
        return roman_num.lower()
    
    def _to_alpha(self, num: int) -> str:
        """Convert number to alphabetic (a, b, c, ...)"""
        if num <= 0:
            return 'a'
        result = ''
        while num > 0:
            result = chr(ord('a') + (num - 1) % 26) + result
            num = (num - 1) // 26
        return result


class ConfigManager:
    """
    Manages PDF generation configuration from YAML files and metadata
    """
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize configuration manager
        
        Args:
            config_path: Path to config.yaml file
        """
        self.config_path = config_path or self._find_config_file()
        self.config = self._load_config()
        
    def _find_config_file(self) -> str:
        """Find config.yaml in project directory"""
        project_root = Path(__file__).parent.parent.parent
        config_file = project_root / "config.yaml"
        return str(config_file)
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    config = yaml.safe_load(f)
                logger.info(f"Configuration loaded from {self.config_path}")
                return config
            else:
                logger.warning(f"Config file not found: {self.config_path}")
                return self._get_default_config()
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Get default configuration"""
        return {
            'page': {
                'format': 'A4',
                'orientation': 'portrait',
                'margins': {
                    'top': '20mm',
                    'right': '15mm',
                    'bottom': '20mm',
                    'left': '15mm'
                },
                'scale': 1.0,
                'print_background': True
            },
            'header': {
                'enabled': True,
                'height': '15mm',
                'template': self._get_default_header_template()
            },
            'footer': {
                'enabled': True,
                'height': '15mm', 
                'template': self._get_default_footer_template()
            },
            'page_numbers': {
                'enabled': True,
                'position': 'footer-right',
                'format': 'Página {current} de {total}',
                'start_from': 1
            },
            'text_alignment': {
                'paragraphs': 'justify',
                'headers': 'left',
                'tables': 'left',
                'code_blocks': 'left',
                'images': 'center'
            }
        }
    
    def _get_default_header_template(self) -> str:
        """Get default header template"""
        return '''
<div style="font-size: 10px; color: #666; width: 100%; padding: 0 20px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #eee;">
    <span class="header-left">{{document.title}}</span>
    <span class="header-center">{{document.author}}</span>
    <span class="header-right">{{date.formatted}}</span>
</div>
        '''.strip()
    
    def _get_default_footer_template(self) -> str:
        """Get default footer template"""
        return '''
<div style="font-size: 10px; color: #666; width: 100%; padding: 0 20px; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #eee;">
    <span class="footer-left">{{generator.name}}</span>
    <span class="footer-center">{{document.subtitle}}</span>
    <span class="footer-right">Página {{page.current}} de {{page.total}}</span>
</div>
        '''.strip()
    
    def get_page_config(self, document_metadata: Dict = None) -> Dict[str, Any]:
        """
        Get page configuration merged with document metadata
        
        Args:
            document_metadata: Document-specific metadata
            
        Returns:
            Page configuration dictionary
        """
        config = self.config['page'].copy()
        
        # Override with document metadata if provided
        if document_metadata:
            if 'format' in document_metadata:
                config['format'] = document_metadata['format']
            if 'orientation' in document_metadata:
                config['orientation'] = document_metadata['orientation']
            if 'margins' in document_metadata:
                config['margins'].update(document_metadata['margins'])
        
        return config
    
    def get_header_template(self, template_name: str = None) -> str:
        """
        Get header template by name or default
        
        Args:
            template_name: Name of template (minimal, corporate, academic)
            
        Returns:
            Header template string
        """
        if template_name and 'templates' in self.config:
            template_config = self.config['templates'].get(template_name, {})
            if 'header' in template_config:
                return template_config['header'].get('template', self.config['header']['template'])
        
        return self.config['header']['template']
    
    def get_footer_template(self, template_name: str = None) -> str:
        """
        Get footer template by name or default
        
        Args:
            template_name: Name of template (minimal, corporate, academic)
            
        Returns:
            Footer template string
        """
        if template_name and 'templates' in self.config:
            template_config = self.config['templates'].get(template_name, {})
            if 'footer' in template_config:
                return template_config['footer'].get('template', self.config['footer']['template'])
        
        return self.config['footer']['template']
    
    def render_template(self, template: str, variables: TemplateVariables) -> str:
        """
        Render template with variables
        
        Args:
            template: Template string with {{variable}} placeholders
            variables: TemplateVariables instance
            
        Returns:
            Rendered template string
        """
        from jinja2 import Template
        
        try:
            jinja_template = Template(template)
            return jinja_template.render(**variables.get_variables())
        except Exception as e:
            logger.error(f"Error rendering template: {e}")
            return template
    
    def get_pdf_options(self, document_metadata: Dict = None) -> Dict[str, Any]:
        """
        Get complete PDF generation options
        
        Args:
            document_metadata: Document-specific metadata
            
        Returns:
            PDF options for Playwright
        """
        page_config = self.get_page_config(document_metadata)
        header_config = self.config.get('header', {})
        footer_config = self.config.get('footer', {})
        
        # Determine template name from metadata
        template_name = None
        if document_metadata:
            template_name = document_metadata.get('template', None)
        
        # Create template variables
        variables = TemplateVariables(document_metadata or {}, {})
        
        # Build PDF options
        pdf_options = {
            'format': page_config['format'],
            'landscape': page_config['orientation'] == 'landscape',
            'margin': page_config['margins'],
            'scale': page_config['scale'],
            'print_background': page_config['print_background'],
            'prefer_css_page_size': True,
            'display_header_footer': header_config.get('enabled', False) or footer_config.get('enabled', False),
        }
        
        # Add header template
        if header_config.get('enabled', False):
            header_template = self.get_header_template(template_name)
            pdf_options['header_template'] = self.render_template(header_template, variables)
        
        # Add footer template
        if footer_config.get('enabled', False):
            footer_template = self.get_footer_template(template_name)
            pdf_options['footer_template'] = self.render_template(footer_template, variables)
        
        return pdf_options
    
    def get_text_alignment_css(self) -> str:
        """
        Get CSS for text alignment configuration
        
        Returns:
            CSS string for text alignment
        """
        alignment = self.config.get('text_alignment', {})
        
        css_rules = []
        
        if alignment.get('paragraphs'):
            css_rules.append(f"p {{ text-align: {alignment['paragraphs']}; }}")
        
        if alignment.get('headers'):
            css_rules.append(f"h1, h2, h3, h4, h5, h6 {{ text-align: {alignment['headers']}; }}")
        
        if alignment.get('tables'):
            css_rules.append(f"table {{ margin-left: {'auto' if alignment['tables'] == 'center' else '0'}; margin-right: {'auto' if alignment['tables'] == 'center' else '0'}; }}")
        
        if alignment.get('code_blocks'):
            css_rules.append(f"pre {{ text-align: {alignment['code_blocks']}; }}")
        
        if alignment.get('images'):
            css_rules.append(f"img {{ display: block; margin-left: {'auto' if alignment['images'] in ['center', 'right'] else '0'}; margin-right: {'auto' if alignment['images'] in ['center', 'left'] else '0'}; }}")
        
        return '\n'.join(css_rules)
    
    def update_config(self, new_config: Dict[str, Any]):
        """
        Update configuration and save to file
        
        Args:
            new_config: New configuration dictionary
        """
        self.config.update(new_config)
        try:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                yaml.dump(self.config, f, default_flow_style=False, indent=2)
            logger.info(f"Configuration saved to {self.config_path}")
        except Exception as e:
            logger.error(f"Error saving config: {e}")
    
    def list_templates(self) -> list:
        """
        Get list of available templates
        
        Returns:
            List of template names
        """
        if 'templates' in self.config:
            return list(self.config['templates'].keys())
        return []
    
    def validate_config(self) -> list:
        """
        Validate configuration and return warnings
        
        Returns:
            List of validation warnings
        """
        warnings = []
        
        # Check required sections
        required_sections = ['page', 'header', 'footer']
        for section in required_sections:
            if section not in self.config:
                warnings.append(f"Missing required section: {section}")
        
        # Check page format
        valid_formats = ['A4', 'A3', 'A2', 'A1', 'A0', 'Letter', 'Legal', 'Tabloid']
        page_format = self.config.get('page', {}).get('format', '')
        if page_format not in valid_formats:
            warnings.append(f"Invalid page format: {page_format}. Valid options: {valid_formats}")
        
        # Check orientation
        valid_orientations = ['portrait', 'landscape']
        orientation = self.config.get('page', {}).get('orientation', '')
        if orientation not in valid_orientations:
            warnings.append(f"Invalid orientation: {orientation}. Valid options: {valid_orientations}")
        
        return warnings 