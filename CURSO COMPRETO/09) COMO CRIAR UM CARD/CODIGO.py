import flet as ft

def main(page):
    page.title = "CARTÃO"
    page.add(
            ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.ALBUM),
                                title=ft.Text("O Rouxinol Encantado"),
                                subtitle=ft.Text(
                                    "Música de Julie Gable. Letra de Sidney Stein."
                                ),
                            ),
                            ft.Row(
                                [ft.TextButton("Comprar bilhetes"), ft.TextButton("Ouvir")],
                                alignment=ft.MainAxisAlignment.END,
                            ),
                        ]
                    ),
                    width=400,
                    padding=10,
                )
            )
        )
    
ft.app(target=main)