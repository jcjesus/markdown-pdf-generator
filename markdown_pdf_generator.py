#!/usr/bin/env python3
"""
Markdown PDF Generator - Script Principal
"""

import sys
import os
from pathlib import Path

# Adicionar o diretório src ao PYTHONPATH
project_root = Path(__file__).parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))

# Importar e executar o main
if __name__ == "__main__":
    from main import main
    main() 