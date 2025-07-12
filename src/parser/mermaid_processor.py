#!/usr/bin/env python3
"""
Mermaid Diagram Processor using Playwright
"""

import asyncio
import tempfile
import os
import base64
import logging
from typing import Dict, List, Optional
from playwright.async_api import async_playwright

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MermaidProcessor:
    """
    Process Mermaid diagrams to SVG using Playwright
    """
    
    def __init__(self, timeout: int = 30000, scale: float = 2.0):
        """
        Initialize Mermaid processor
        
        Args:
            timeout: Timeout for rendering in milliseconds
            scale: Scale factor for high-DPI rendering
        """
        self.timeout = timeout
        self.scale = scale
        self.mermaid_html_template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10.6.1/dist/mermaid.min.js"></script>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: white;
        }
        .mermaid {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 300px;
        }
        .mermaid svg {
            max-width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <div class="mermaid">
        {mermaid_content}
    </div>
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
            },
            sequence: {
                diagramMarginX: 50,
                diagramMarginY: 10,
                actorMargin: 50,
                width: 150,
                height: 65,
                boxMargin: 10,
                boxTextMargin: 5,
                noteMargin: 10,
                messageMargin: 35,
                mirrorActors: true,
                bottomMarginAdj: 1,
                useMaxWidth: true,
                rightAngles: false,
                showSequenceNumbers: false
            },
            gantt: {
                titleTopMargin: 25,
                barHeight: 20,
                fontSe: 11,
                sidePadding: 75,
                leftPadding: 75,
                gridLineStartPadding: 35,
                fontSize: 11,
                fontFamily: '"Open Sans", sans-serif',
                numberSectionStyles: 4,
                axisFormat: '%Y-%m-%d'
            }
        });
    </script>
</body>
</html>
        """
    
    async def render_diagram(self, diagram_id: str, mermaid_content: str) -> Optional[str]:
        """
        Render a single Mermaid diagram to SVG
        
        Args:
            diagram_id: Unique identifier for the diagram
            mermaid_content: Mermaid diagram code
            
        Returns:
            SVG content as string or None if failed
        """
        try:
            # Create temporary HTML file
            html_content = self.mermaid_html_template.format(
                mermaid_content=mermaid_content
            )
            
            with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
                f.write(html_content)
                temp_html_path = f.name
            
            async with async_playwright() as p:
                # Launch browser
                browser = await p.chromium.launch(headless=True)
                page = await browser.new_page()
                
                # Set viewport for consistent rendering
                await page.set_viewport_size({"width": 1200, "height": 800})
                
                # Navigate to the HTML file
                await page.goto(f"file://{temp_html_path}")
                
                # Wait for Mermaid to render
                await page.wait_for_selector('.mermaid svg', timeout=self.timeout)
                await page.wait_for_timeout(1000)  # Additional wait for rendering
                
                # Get the SVG element
                svg_element = await page.query_selector('.mermaid svg')
                if not svg_element:
                    logger.error(f"No SVG found for diagram {diagram_id}")
                    return None
                
                # Extract SVG content
                svg_content = await svg_element.inner_html()
                
                # Get the outer HTML to include the SVG tag
                svg_outer = await svg_element.evaluate('element => element.outerHTML')
                
                await browser.close()
                
                # Clean up temporary file
                os.unlink(temp_html_path)
                
                logger.info(f"Successfully rendered diagram {diagram_id}")
                return svg_outer
                
        except Exception as e:
            logger.error(f"Failed to render diagram {diagram_id}: {e}")
            # Clean up temporary file if it exists
            if 'temp_html_path' in locals():
                try:
                    os.unlink(temp_html_path)
                except:
                    pass
            return None
    
    async def process_diagrams(self, diagrams: List[Dict]) -> Dict[str, str]:
        """
        Process multiple Mermaid diagrams
        
        Args:
            diagrams: List of diagram dictionaries with id and content
            
        Returns:
            Dictionary mapping diagram IDs to SVG content
        """
        logger.info(f"Processing {len(diagrams)} Mermaid diagrams...")
        
        results = {}
        
        # Process diagrams concurrently
        tasks = []
        for diagram in diagrams:
            task = self.render_diagram(diagram['id'], diagram['content'])
            tasks.append(task)
        
        # Wait for all tasks to complete
        svg_results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Collect successful results
        for i, result in enumerate(svg_results):
            if isinstance(result, Exception):
                logger.error(f"Failed to process diagram {diagrams[i]['id']}: {result}")
            elif result:
                results[diagrams[i]['id']] = result
        
        logger.info(f"Successfully processed {len(results)}/{len(diagrams)} diagrams")
        return results
    
    def validate_mermaid_syntax(self, content: str) -> List[str]:
        """
        Basic validation of Mermaid syntax
        
        Args:
            content: Mermaid diagram content
            
        Returns:
            List of validation warnings
        """
        warnings = []
        
        if not content.strip():
            warnings.append("Empty diagram content")
            return warnings
        
        # Check for common diagram types
        diagram_types = [
            'graph', 'flowchart', 'sequenceDiagram', 'classDiagram',
            'stateDiagram', 'gantt', 'pie', 'journey', 'gitgraph',
            'mindmap', 'timeline', 'er', 'c4Context'
        ]
        
        first_line = content.strip().split('\n')[0].lower()
        has_valid_type = any(dtype in first_line for dtype in diagram_types)
        
        if not has_valid_type:
            warnings.append(f"Unknown diagram type in: {first_line}")
        
        # Check for common syntax issues
        if content.count('-->') != content.count('-->'):
            warnings.append("Mismatched arrow syntax")
        
        if '```' in content:
            warnings.append("Code block syntax found in diagram content")
        
        return warnings
    
    def get_supported_diagrams(self) -> List[str]:
        """
        Get list of supported Mermaid diagram types
        
        Returns:
            List of supported diagram types
        """
        return [
            'flowchart', 'graph', 'sequenceDiagram', 'classDiagram',
            'stateDiagram', 'gantt', 'pie', 'journey', 'gitgraph',
            'mindmap', 'timeline', 'er', 'c4Context', 'sankey',
            'requirementDiagram', 'quadrantChart'
        ] 