#!/usr/bin/env python3
"""
Markdown PDF Generator

Professional tool for converting Markdown documents to PDF with support for:
- Mermaid diagrams
- Emojis
- Tables, code blocks, images
- Custom CSS styling
- Temporary HTML generation (auto-cleanup)
"""

__version__ = "1.0.0"
__author__ = "SoundLink Infrastructure Team"
__email__ = "dev@soundlink.com"

from .main import main, generate_pdf

__all__ = ["main", "generate_pdf"] 