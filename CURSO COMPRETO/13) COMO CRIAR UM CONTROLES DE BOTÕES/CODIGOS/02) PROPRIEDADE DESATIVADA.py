import flet as ft

def main(page):
    # Cria campos de texto para primeiro e último nome
    first_name = ft.TextField()
    last_name = ft.TextField()

    # Cria uma coluna para organizar os controles
    column = ft.Column(controls=[first_name, last_name])
    column.disabled = True  # Desabilita toda a coluna

    # Adiciona a coluna à página
    page.add(column)

# Inicia a aplicação Flet com a função main como alvo
ft.app(target=main)
