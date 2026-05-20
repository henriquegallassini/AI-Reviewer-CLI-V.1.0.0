🔍 Reviewer CLI
Um analisador de código Python inteligente que roda direto no terminal — sem API, sem custo, 100% local.

💡 O que faz
O AI Reviewer CLI lê qualquer arquivo .py e detecta automaticamente problemas comuns de qualidade de código, exibindo o resultado em uma tabela colorida no terminal.
Regras de análise atuais
RegraDescrição⚠️ Sem docstringFunções que não têm descrição📏 Função muito longaFunções com mais de 20 linhas🏷️ Nome de variável curtoVariáveis com nomes de 1 letra (exceto i, j, k)

🚀 Como usar
1. Clone o repositório
bashgit clone https://github.com/seu-usuario/ai-reviewer-cli.git
cd ai-reviewer-cli
2. Crie e ative o ambiente virtual
bashpython -m venv .venv

# Windows
.venv\Scripts\Activate.ps1

# Linux/Mac
source .venv/bin/activate
3. Instale as dependências
bashpip install rich
4. Rode o analisador
bashpython "AI Reviewer-CLI.py"

📦 Dependências

rich — tabelas e cores no terminal
ast — biblioteca nativa do Python (já incluída)


🗓️ Roadmap

 Detectar funções sem docstring
 Detectar funções muito longas
 Detectar variáveis com nomes ruins
 Pontuação geral do código
 Analisar qualquer arquivo passado por argumento no terminal
 Detectar imports não utilizados
 Detectar loops muito aninhados
 Exportar relatório em .md ou .txt
 Suporte a múltiplos arquivos


🧠 Como funciona
O programa usa a biblioteca ast (Abstract Syntax Tree) do Python para transformar o código em uma árvore sintática — uma estrutura de dados que representa cada elemento do código (funções, variáveis, loops, etc). A partir dessa árvore, aplicamos regras para identificar problemas de qualidade.
Código .py  →  ast.parse()  →  Árvore  →  Regras  →  Relatório

📄 Licença
MIT License — fique à vontade pra usar, modificar e distribuir.

Feito com 🐍 Python por Henrique
