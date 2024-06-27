import flet as ft

def main(page: ft.Page):
    page.title = "Recipientes com cor de fundo"

    c1 = ft.Container(
        content=ft.ElevatedButton("Botão elevado no contêiner"),
        bgcolor=ft.colors.YELLOW,
        padding=5,
    )

    c2 = ft.Container(
        content=ft.ElevatedButton(
            "Botão elevado com opacidade = 0,5 no contêiner", opacity=0.5
        ),
        bgcolor=ft.colors.YELLOW,
        padding=5,
    )

    c3 = ft.Container(
        content=ft.OutlinedButton("Botão delineado no contêiner"),
        bgcolor=ft.colors.YELLOW,
        padding=5,
    )

    # adicionando os containers
    page.add(c1, c2, c3)

ft.app(target=main)