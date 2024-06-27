import flet as ft

def main(page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="O que precisa ser feito?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Adicionar", on_click=add_clicked)]))

ft.app(target=main)