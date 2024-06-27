import flet as ft

def main(page: ft.Page):
    
    page.add(
    ft.Row(controls=[
        ft.TextField(label="Seu nome"),
        ft.ElevatedButton(text="Diga meu nome!")
    ])
    )

ft.app(target=main)