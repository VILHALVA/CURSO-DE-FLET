import flet as ft

def main(page: ft.Page):
    items = []
    for i in range(1, 8):
        items.append(
            ft.Container(
                content=ft.Text(value=str(i)),
                alignment=ft.alignment.center,
                width=50,
                height=50,
                bgcolor=ft.colors.AMBER,
                border_radius=ft.border_radius.all(5),
            )
        )
    col = ft.Column(spacing=5, controls=items)
    page.add(ft.Column([ft.Text("Exemplo de column em Flet")]), col)
    
ft.app(target=main)