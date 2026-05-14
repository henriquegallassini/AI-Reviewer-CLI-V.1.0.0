import ast
from rich.console import Console
from rich.table import Table

console = Console()

def analisar_codigo(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        codigo = f.read()

    arvore = ast.parse(codigo)
    
    tabela = Table(title=f"🔍 Análise de: {caminho_arquivo}")
    tabela.add_column("Linha", style="cyan", width=8)
    tabela.add_column("Problema", style="yellow")
    tabela.add_column("Função", style="green")

    for no in ast.walk(arvore):
        if isinstance(no, ast.FunctionDef):
            tem_docstring = (
                isinstance(no.body[0], ast.Expr) and
                isinstance(no.body[0].value, ast.Constant)
            )
            if not tem_docstring:
                tabela.add_row(
                    str(no.lineno),
                    "⚠️ Sem docstring ",
                    no.name
                )

            tamanho = no.end_lineno - no.lineno
            if tamanho > 5 and <= 20:
                    tabela.add_row(
                        str(no.lineno),
                        f"📏 Função muito longa ({tamanho} linhas)",
                        no.name
                    )

        if isinstance(no, ast.Name):
            if len(no.id) == 1 and no.id not in ["i", "j", "k", "n", "_"]:
                tabela.add_row(
                    str(no.col_offset),
                    f"🏷️  Nome de variável muito curto: '{no.id}'",
                    "-"
            )
    
    total_problemas = len(tabela.rows)

    console.print(tabela)
    console.print()

    if total_problemas == 0:
         console.print("✅ [bold green]Código perfeito! Nenhum problema encontrado.[/bold green]")
    elif total_problemas <=3:
         console.print(f"🟡 [bold yellow]Código OK — {total_problemas} problema(s) encontrado(s). Pode melhorar![/bold yellow]")
    else:
         console.print(f"🔴 [bold red]Código precisa de atenção — {total_problemas} problema(s) encontrado(s)![/bold red]")
   
    console.print()
    console.print(f"[dim]Total de problemas: {total_problemas}[/dim]")
analisar_codigo("AI Reviewer-CLI.py")
