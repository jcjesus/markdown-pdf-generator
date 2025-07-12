#!/usr/bin/env python3
"""
Advanced Markdown Parser with emoji and extensions support
"""

import re
import markdown
from markdown.extensions import codehilite, tables, toc, fenced_code
from markdown.extensions.extra import ExtraExtension
import emoji
from typing import Dict, List, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MarkdownParser:
    """
    Advanced Markdown parser with support for:
    - Standard Markdown
    - GitHub Flavored Markdown
    - Emojis (Unicode and :shortcodes:)
    - Tables, code blocks, TOC
    - Mermaid diagram extraction
    """
    
    def __init__(self, custom_extensions: Optional[List[str]] = None):
        """
        Initialize the parser with extensions
        
        Args:
            custom_extensions: Optional list of additional markdown extensions
        """
        self.extensions = [
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            'markdown.extensions.tables',
            'markdown.extensions.fenced_code',
            'markdown.extensions.def_list',
            'markdown.extensions.abbr',
            'markdown.extensions.attr_list',
            'markdown.extensions.footnotes',
            'markdown.extensions.meta',
            'markdown.extensions.sane_lists',
            'markdown.extensions.smarty',
            'markdown.extensions.wikilinks',
        ]
        
        if custom_extensions:
            self.extensions.extend(custom_extensions)
            
        self.extension_configs = {
            'markdown.extensions.codehilite': {
                'css_class': 'highlight',
                'use_pygments': True,
                'noclasses': True,
            },
            'markdown.extensions.toc': {
                'anchorlink': True,
                'permalink': False,
                'toc_depth': 6,
                'title': 'Índice',
                'separator': '-',
            },
            'markdown.extensions.tables': {},
            'markdown.extensions.fenced_code': {},
        }
        
        # Initialize markdown processor
        self.md = markdown.Markdown(
            extensions=self.extensions,
            extension_configs=self.extension_configs,
            tab_length=4,
            safe_mode=False,
        )
        
        # Mermaid diagram patterns
        self.mermaid_patterns = [
            r'```mermaid\s*\n(.*?)\n```',
            r'```\s*mermaid\s*\n(.*?)\n```',
            r'<div class="mermaid">(.*?)</div>',
        ]
    
    def extract_mermaid_diagrams(self, content: str) -> Tuple[str, List[Dict]]:
        """
        Extract Mermaid diagrams from markdown content
        
        Args:
            content: Raw markdown content
            
        Returns:
            Tuple of (content_without_mermaid, list_of_mermaid_diagrams)
        """
        diagrams = []
        processed_content = content
        
        for i, pattern in enumerate(self.mermaid_patterns):
            matches = re.finditer(pattern, processed_content, re.DOTALL | re.MULTILINE)
            
            for match in matches:
                diagram_id = f"mermaid-{len(diagrams)}"
                diagram_content = match.group(1).strip()
                
                diagrams.append({
                    'id': diagram_id,
                    'content': diagram_content,
                    'placeholder': f'<div id="{diagram_id}" class="mermaid-placeholder"></div>'
                })
                
                # Replace diagram with placeholder
                processed_content = processed_content.replace(
                    match.group(0),
                    f'<div id="{diagram_id}" class="mermaid-placeholder"></div>'
                )
        
        logger.info(f"Extracted {len(diagrams)} Mermaid diagrams")
        return processed_content, diagrams
    
    def process_emojis(self, content: str) -> str:
        """
        Process emojis in content (both Unicode and :shortcodes:)
        
        Args:
            content: Content with emojis
            
        Returns:
            Content with processed emojis
        """
        # Convert :shortcodes: to Unicode emojis
        content = emoji.emojize(content, language='alias')
        
        # Ensure Unicode emojis are properly handled
        content = content.encode('utf-8').decode('utf-8')
        
        return content
    
    def parse_metadata(self, content: str) -> Tuple[str, Dict]:
        """
        Parse YAML front matter metadata
        
        Args:
            content: Markdown content with potential front matter
            
        Returns:
            Tuple of (content_without_metadata, metadata_dict)
        """
        metadata = {}
        
        # Check for YAML front matter
        if content.startswith('---\n'):
            try:
                parts = content.split('---\n', 2)
                if len(parts) >= 3:
                    import yaml
                    metadata = yaml.safe_load(parts[1]) or {}
                    content = parts[2]
            except Exception as e:
                logger.warning(f"Failed to parse YAML metadata: {e}")
        
        return content, metadata
    
    def parse(self, content: str) -> Dict:
        """
        Parse markdown content and return structured data
        
        Args:
            content: Raw markdown content
            
        Returns:
            Dictionary with parsed content and metadata
        """
        logger.info("Starting markdown parsing...")
        
        # 1. Parse metadata
        content, metadata = self.parse_metadata(content)
        
        # 2. Process emojis
        content = self.process_emojis(content)
        
        # 3. Extract Mermaid diagrams
        content, mermaid_diagrams = self.extract_mermaid_diagrams(content)
        
        # 4. Convert to HTML
        html_content = self.md.convert(content)
        
        # 5. Get TOC if available
        toc = getattr(self.md, 'toc', '')
        
        # 6. Reset markdown instance for next use
        self.md.reset()
        
        result = {
            'html': html_content,
            'toc': toc,
            'metadata': metadata,
            'mermaid_diagrams': mermaid_diagrams,
            'stats': {
                'lines': len(content.split('\n')),
                'words': len(content.split()),
                'chars': len(content),
                'mermaid_count': len(mermaid_diagrams),
            }
        }
        
        logger.info(f"Parsing complete: {result['stats']}")
        return result
    
    def validate_markdown(self, content: str) -> List[str]:
        """
        Validate markdown content and return list of warnings
        
        Args:
            content: Markdown content to validate
            
        Returns:
            List of validation warnings
        """
        warnings = []
        
        # Check for common issues
        if not content.strip():
            warnings.append("Empty document")
        
        # Check for unclosed code blocks
        fenced_blocks = re.findall(r'```', content)
        if len(fenced_blocks) % 2 != 0:
            warnings.append("Unclosed fenced code block detected")
        
        # Check for malformed links
        malformed_links = re.findall(r'\[([^\]]+)\]\([^)]*$', content)
        if malformed_links:
            warnings.append(f"Malformed links detected: {len(malformed_links)}")
        
        # Check for empty headers
        empty_headers = re.findall(r'^#+\s*$', content, re.MULTILINE)
        if empty_headers:
            warnings.append(f"Empty headers detected: {len(empty_headers)}")
        
        return warnings 