import flet as ft

# Definição da função principal (main)
def main(page):
    # Função para fechar o banner de notificação
    def close_banner(e):
        page.banner.open = False
        page.update()

    # Configuração do tamanho da janela
    page.window_width = 500
    page.window_height = 550

    # Configuração do banner de notificação
    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text("Ops, Adicione algum Valor"),
        actions=[
            ft.TextButton("Ok", on_click=close_banner),
        ],
    )

    # Função para adicionar uma nova tarefa
    def adicionar(e):
        if nova_tarefa.value == "":
            # Mostrar notificação de erro
            page.banner.open = True
            page.update()
        else:
            page.add(ft.Checkbox(label=nova_tarefa.value))
            nova_tarefa.value = ""
            nova_tarefa.focus()
            nova_tarefa.update()

    # Criação de elementos de interface gráfica
    nova_tarefa = ft.TextField(hint_text="O que precisa ser feito", width=300)
    botao_adicionar = ft.ElevatedButton("Adicionar", on_click=adicionar)

    # Adição de elementos à página em uma linha (Row)
    page.add(ft.Row([nova_tarefa, botao_adicionar]))

# Inicia a aplicação Flet com a função main como alvo
ft.app(target=main)
