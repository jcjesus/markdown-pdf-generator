#!/usr/bin/env python3
"""
Professional PDF Generator using Playwright with advanced configuration
"""

import asyncio
import os
import tempfile
from typing import Dict, Optional
from playwright.async_api import async_playwright
import logging

# Import configuration manager
from ..config import ConfigManager, TemplateVariables

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PDFGenerator:
    """
    Generate PDF from HTML using Playwright with advanced configuration system
    """
    
    def __init__(self, 
                 config_path: Optional[str] = None,
                 format: str = None,
                 margin: Dict[str, str] = None,
                 print_background: bool = None,
                 landscape: bool = None,
                 scale: float = None):
        """
        Initialize PDF generator with configuration support
        
        Args:
            config_path: Path to configuration file
            format: Paper format (overrides config)
            margin: Page margins (overrides config)
            print_background: Print background (overrides config)
            landscape: Landscape orientation (overrides config)
            scale: Scale factor (overrides config)
        """
        # Initialize configuration manager
        self.config_manager = ConfigManager(config_path)
        
        # Store overrides
        self.overrides = {
            'format': format,
            'margin': margin,
            'print_background': print_background,
            'landscape': landscape,
            'scale': scale
        }
        
        # Remove None values from overrides
        self.overrides = {k: v for k, v in self.overrides.items() if v is not None}
    
    async def generate_pdf(self, html_file_path: str, output_path: str, 
                          metadata: Optional[Dict] = None,
                          stats: Optional[Dict] = None) -> bool:
        """
        Generate PDF from HTML file using configuration system
        
        Args:
            html_file_path: Path to HTML file
            output_path: Path for output PDF
            metadata: Document metadata for templates
            stats: Document statistics for templates
            
        Returns:
            True if successful, False otherwise
        """
        try:
            logger.info(f"Starting PDF generation: {output_path}")
            
            # Merge metadata with overrides
            combined_metadata = (metadata or {}).copy()
            combined_metadata.update(self.overrides)
            
            # Create template variables
            template_vars = TemplateVariables(
                document_metadata=combined_metadata,
                stats=stats or {}
            )
            
            # Get PDF options from configuration
            pdf_options = self.config_manager.get_pdf_options(combined_metadata)
            
            async with async_playwright() as p:
                # Launch browser
                browser = await p.chromium.launch(headless=True)
                context = await browser.new_context()
                page = await context.new_page()
                
                # Set viewport for consistent rendering
                await page.set_viewport_size({"width": 1200, "height": 1600})
                
                # Navigate to HTML file
                await page.goto(f"file://{html_file_path}")
                
                # Wait for content to load
                await page.wait_for_load_state('networkidle')
                
                # Wait for Mermaid diagrams to render if any
                try:
                    await page.wait_for_selector('.mermaid svg', timeout=10000)
                    await page.wait_for_timeout(2000)  # Additional wait
                except:
                    logger.info("No Mermaid diagrams found or timeout")
                
                # Update template variables with actual page count
                total_pages = await self._get_page_count(page, pdf_options)
                template_vars.set_page_info(1, total_pages)
                
                # Re-render templates with correct page info
                template_name = combined_metadata.get('template')
                if pdf_options.get('display_header_footer'):
                    if 'header_template' in pdf_options:
                        header_template = self.config_manager.get_header_template(template_name)
                        pdf_options['header_template'] = self.config_manager.render_template(
                            header_template, template_vars
                        )
                    
                    if 'footer_template' in pdf_options:
                        footer_template = self.config_manager.get_footer_template(template_name)
                        pdf_options['footer_template'] = self.config_manager.render_template(
                            footer_template, template_vars
                        )
                
                # Generate PDF
                await page.pdf(path=output_path, **pdf_options)
                
                await browser.close()
                
                logger.info(f"PDF generated successfully: {output_path}")
                logger.info(f"Configuration template: {template_name or 'default'}")
                logger.info(f"Total pages: {total_pages}")
                
                return True
                
        except Exception as e:
            logger.error(f"PDF generation failed: {e}")
            return False
    
    async def _get_page_count(self, page, pdf_options: Dict) -> int:
        """
        Get the total number of pages that will be generated
        
        Args:
            page: Playwright page object
            pdf_options: PDF generation options
            
        Returns:
            Total number of pages
        """
        try:
            # Create a temporary PDF to count pages
            temp_pdf = await page.pdf(**{k: v for k, v in pdf_options.items() 
                                       if k not in ['header_template', 'footer_template']})
            
            # Use a simple heuristic based on content height
            content_height = await page.evaluate('document.documentElement.scrollHeight')
            page_height = 1123  # A4 height in pixels at 96 DPI
            
            # Account for margins
            margin_top = self._parse_margin(pdf_options.get('margin', {}).get('top', '20mm'))
            margin_bottom = self._parse_margin(pdf_options.get('margin', {}).get('bottom', '20mm'))
            
            effective_page_height = page_height - margin_top - margin_bottom
            estimated_pages = max(1, (content_height // effective_page_height) + 1)
            
            return int(estimated_pages)
            
        except Exception as e:
            logger.warning(f"Could not determine page count: {e}")
            return 1
    
    def _parse_margin(self, margin_str: str) -> int:
        """Parse margin string to pixels"""
        if margin_str.endswith('mm'):
            mm = float(margin_str[:-2])
            return int(mm * 3.78)  # Convert mm to pixels
        elif margin_str.endswith('px'):
            return int(margin_str[:-2])
        else:
            return 20  # Default margin
    
    async def generate_pdf_from_html_content(self, html_content: str, 
                                           output_path: str,
                                           metadata: Optional[Dict] = None) -> bool:
        """
        Generate PDF directly from HTML content
        
        Args:
            html_content: HTML content as string
            output_path: Path for output PDF
            metadata: Optional metadata for PDF
            
        Returns:
            True if successful, False otherwise
        """
        # Create temporary HTML file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', 
                                       delete=False, encoding='utf-8') as f:
            f.write(html_content)
            temp_html_path = f.name
        
        try:
            # Generate PDF from temporary file
            result = await self.generate_pdf(temp_html_path, output_path, metadata)
            return result
        finally:
            # Clean up temporary file
            try:
                os.unlink(temp_html_path)
            except:
                pass
    
    def get_supported_formats(self) -> list:
        """
        Get list of supported paper formats
        
        Returns:
            List of supported formats
        """
        return ['A4', 'A3', 'A2', 'A1', 'A0', 'Letter', 'Legal', 'Tabloid']
    
    def set_custom_css(self, css_content: str):
        """
        Set custom CSS for PDF styling
        
        Args:
            css_content: CSS content as string
        """
        self.custom_css = css_content
    
    def validate_output_path(self, output_path: str) -> bool:
        """
        Validate output path
        
        Args:
            output_path: Path to validate
            
        Returns:
            True if valid, False otherwise
        """
        try:
            # Check if directory exists
            output_dir = os.path.dirname(output_path)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir, exist_ok=True)
            
            # Check file extension
            if not output_path.lower().endswith('.pdf'):
                return False
            
            return True
        except Exception as e:
            logger.error(f"Output path validation failed: {e}")
            return False
    
    def estimate_pdf_size(self, html_content: str) -> Dict[str, int]:
        """
        Estimate PDF size and page count
        
        Args:
            html_content: HTML content
            
        Returns:
            Dictionary with estimated metrics
        """
        # Simple estimation based on content length
        content_length = len(html_content)
        estimated_pages = max(1, content_length // 3000)  # Rough estimate
        
        return {
            'estimated_pages': estimated_pages,
            'content_length': content_length,
            'estimated_size_kb': content_length // 100  # Very rough estimate
        } 