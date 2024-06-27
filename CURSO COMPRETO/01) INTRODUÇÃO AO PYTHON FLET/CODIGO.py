from flet import App, Label, Button

# Função para manipular o clique do botão
def on_click():
    label.text = "Botão clicado!"

# Inicializa a aplicação
app = App()

# Cria uma tela
screen = app.screen()

# Adiciona um label e um botão à tela
label = Label(screen, text="Olá, Flet!")
button = Button(screen, text="Clique Aqui", on_click=on_click)

# Executa a aplicação
app.run()
