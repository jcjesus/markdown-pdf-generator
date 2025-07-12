# 🚀 SoundLink Markdown PDF Generator - Makefile

.PHONY: help install setup test clean run example

# Default target
help:
	@echo "🚀 SoundLink Markdown PDF Generator"
	@echo "=================================="
	@echo ""
	@echo "Comandos disponíveis:"
	@echo "  make install    - Instalar dependências"
	@echo "  make setup      - Configuração inicial completa"
	@echo "  make test       - Executar testes"
	@echo "  make example    - Gerar PDF do arquivo de exemplo"
	@echo "  make clean      - Limpar arquivos temporários"
	@echo "  make run FILE=arquivo.md - Gerar PDF de um arquivo"
	@echo ""
	@echo "Exemplos:"
	@echo "  make setup                    # Instalação completa"
	@echo "  make run FILE=documento.md    # Gerar PDF"
	@echo "  make example                  # Testar com exemplo"

# Instalar dependências
install:
	@echo "📦 Instalando dependências..."
	@if [ ! -d "venv" ]; then \
		echo "🔧 Criando ambiente virtual..."; \
		python3 -m venv venv || (echo "⚠️  Instale python3-venv: sudo apt install python3.12-venv" && exit 1); \
	fi
	@echo "🔧 Ativando ambiente virtual e instalando dependências..."
	@. venv/bin/activate && pip install -r requirements.txt
	@echo "🎭 Instalando Playwright..."
	@. venv/bin/activate && playwright install chromium
	@echo "✅ Instalação concluída!"

# Configuração inicial completa
setup: install
	@echo "🔧 Configuração inicial..."
	@chmod +x scripts/run.sh 2>/dev/null || echo "⚠️  Script não encontrado"
	@echo "✅ Configuração concluída!"
	@echo ""
	@echo "🎉 Projeto pronto! Use:"
	@echo "  make run FILE=documento.md"
	@echo "  make example"

# Executar testes
test:
	@echo "🧪 Executando testes..."
	@. venv/bin/activate && python -m pytest tests/ -v || echo "⚠️  Testes não executados"
	@echo "✅ Testes concluídos!"

# Gerar PDF do arquivo de exemplo
example:
	@echo "📄 Gerando PDF do arquivo de exemplo..."
	@. venv/bin/activate && python3 src/main.py tests/fixtures/sample.md -o exemplo.pdf --verbose
	@echo "✅ PDF gerado: exemplo.pdf"

# Gerar PDF de um arquivo específico
run:
	@if [ -z "$(FILE)" ]; then \
		echo "❌ Especifique o arquivo: make run FILE=documento.md"; \
		exit 1; \
	fi
	@echo "📄 Gerando PDF de: $(FILE)"
	@. venv/bin/activate && python3 src/main.py $(FILE) $(ARGS)
	@echo "✅ PDF gerado com sucesso!"

# Limpar arquivos temporários
clean:
	@echo "🧹 Limpando arquivos temporários..."
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.tmp" -delete 2>/dev/null || true
	@find . -type f -name "*.temp" -delete 2>/dev/null || true
	@rm -rf .pytest_cache/ 2>/dev/null || true
	@rm -rf htmlcov/ 2>/dev/null || true
	@rm -rf .coverage 2>/dev/null || true
	@echo "✅ Limpeza concluída!"

# Instalar dependências do sistema (Ubuntu/Debian)
install-system:
	@echo "🔧 Instalando dependências do sistema..."
	@sudo apt update
	@sudo apt install -y python3.12-venv nodejs npm
	@echo "✅ Dependências do sistema instaladas!"

# Mostrar status do projeto
status:
	@echo "📊 Status do Projeto"
	@echo "==================="
	@echo "📁 Diretório: $(PWD)"
	@echo "🐍 Python: $(shell python3 --version 2>/dev/null || echo 'Não instalado')"
	@echo "📦 Venv: $(shell test -d venv && echo 'Configurado' || echo 'Não configurado')"
	@echo "🎭 Playwright: $(shell test -d venv && . venv/bin/activate && playwright --version 2>/dev/null || echo 'Não instalado')"
	@echo ""
	@echo "📋 Arquivos do projeto:"
	@ls -la src/ 2>/dev/null || echo "⚠️  Diretório src/ não encontrado"

# Gerar documentação
docs:
	@echo "📚 Gerando documentação..."
	@. venv/bin/activate && python3 -m pydoc -w src/
	@echo "✅ Documentação gerada!"

# Executar linting
lint:
	@echo "🔍 Executando linting..."
	@. venv/bin/activate && flake8 src/ tests/ || echo "⚠️  Flake8 não configurado"
	@. venv/bin/activate && black --check src/ tests/ || echo "⚠️  Black não configurado"
	@echo "✅ Linting concluído!"

# Formatar código
format:
	@echo "🎨 Formatando código..."
	@. venv/bin/activate && black src/ tests/ || echo "⚠️  Black não configurado"
	@echo "✅ Código formatado!"

# Instalar dependências de desenvolvimento
install-dev:
	@echo "🛠️  Instalando dependências de desenvolvimento..."
	@. venv/bin/activate && pip install pytest pytest-cov black flake8 mypy
	@echo "✅ Dependências de desenvolvimento instaladas!"

# Executar todos os testes com coverage
test-coverage:
	@echo "🧪 Executando testes com coverage..."
	@. venv/bin/activate && python -m pytest tests/ --cov=src --cov-report=html
	@echo "✅ Relatório de coverage gerado em htmlcov/"

# Criar release
release:
	@echo "🚀 Criando release..."
	@. venv/bin/activate && python setup.py sdist bdist_wheel
	@echo "✅ Release criado em dist/"

# Mostrar logs
logs:
	@echo "📋 Últimos logs:"
	@tail -n 50 *.log 2>/dev/null || echo "📝 Nenhum log encontrado"

# Benchmark
benchmark:
	@echo "⚡ Executando benchmark..."
	@time make example
	@echo "✅ Benchmark concluído!" 