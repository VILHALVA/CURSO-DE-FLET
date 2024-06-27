# INTRODUÇÃO AO PYTHON FLET
## CONCEITO
O Python Flet é um framework que permite o desenvolvimento de aplicações web, desktop e mobile usando Python, de forma integrada e sem exigir experiência prévia em desenvolvimento front-end. Ele facilita a criação de interfaces gráficas interativas e multiusuário.

### CÓDIGO DE EXEMPLO
```python
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
```

## EXPLICAÇÃO
- `App`: Inicializa a aplicação Flet.
- `screen`: Cria uma tela para a aplicação.
- `Label`: Cria um label para exibir texto na interface.
- `Button`: Cria um botão que executa uma função (`on_click`) quando clicado.
- `on_click`: Função que atualiza o texto do label quando o botão é clicado.
- `app.run()`: Inicia o loop principal da aplicação Flet, exibindo a interface gráfica e aguardando interações do usuário.

Este exemplo básico demonstra como começar a usar o Python Flet para criar uma interface simples com um label e um botão que respondem a eventos de clique.