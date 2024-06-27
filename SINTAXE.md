# SINTAXE
## LABELS
Os labels são usados para exibir texto estático na interface.

### CÓDIGO
```python
from flet import App, Label

# Inicializa a aplicação
app = App()

# Cria uma tela
screen = app.screen()

# Adiciona um label
label = Label(screen, text="Este é um Label")

# Executa a aplicação
app.run()
```

### EXPLICAÇÃO
- `Label`: Cria um label.
- `text`: Define o texto exibido pelo label.
- `screen`: Cria uma tela para conter os widgets.

## BOTÕES
Os botões permitem ao usuário executar ações quando clicados.

### CÓDIGO
```python
from flet import App, Button

# Função de clique do botão
def on_click():
    print("Botão clicado!")

# Inicializa a aplicação
app = App()

# Cria uma tela
screen = app.screen()

# Adiciona um botão
button = Button(screen, text="Clique Aqui", on_click=on_click)

# Executa a aplicação
app.run()
```

### EXPLICAÇÃO
- `Button`: Cria um botão.
- `text`: Define o texto exibido no botão.
- `on_click`: Conecta o clique do botão a uma função.

## CAIXAS DE ENTRADA DE TEXTO
As caixas de entrada de texto permitem ao usuário inserir texto.

### CÓDIGO
```python
from flet import App, TextInput, Button

# Função para obter o texto
def get_text():
    texto = text_input.value
    print(f"Você digitou: {texto}")

# Inicializa a aplicação
app = App()

# Cria uma tela
screen = app.screen()

# Adiciona uma caixa de entrada de texto e um botão
text_input = TextInput(screen)
button = Button(screen, text="Enviar", on_click=get_text)

# Executa a aplicação
app.run()
```

### EXPLICAÇÃO
- `TextInput`: Cria uma caixa de entrada de texto.
- `value`: Obtém o texto inserido na caixa de entrada.

## CAIXAS DE SELEÇÃO
As caixas de seleção permitem ao usuário selecionar ou desmarcar opções.

### CÓDIGO
```python
from flet import App, Checkbox, Button

# Função para verificar o estado da caixa de seleção
def check_status():
    status = 'marcado' if checkbox.value else 'desmarcado'
    print(f"Checkbox está: {status}")

# Inicializa a aplicação
app = App()

# Cria uma tela
screen = app.screen()

# Adiciona uma caixa de seleção e um botão
checkbox = Checkbox(screen, text="Aceito os termos e condições")
button = Button(screen, text="Verificar", on_click=check_status)

# Executa a aplicação
app.run()
```

### EXPLICAÇÃO
- `Checkbox`: Cria uma caixa de seleção.
- `value`: Verifica se a caixa de seleção está marcada.

## RADIO BUTTONS
Os radio buttons permitem ao usuário selecionar apenas uma opção de um grupo de opções.

### CÓDIGO
```python
from flet import App, RadioGroup, Button

# Função para verificar a seleção
def check_selection():
    selecao = radio_group.selected.text
    print(f"Você selecionou: {selecao}")

# Inicializa a aplicação
app = App()

# Cria uma tela
screen = app.screen()

# Adiciona um grupo de radio buttons e um botão
radio_group = RadioGroup(screen, options=["Opção 1", "Opção 2"])
button = Button(screen, text="Verificar Seleção", on_click=check_selection)

# Executa a aplicação
app.run()
```

### EXPLICAÇÃO
- `RadioGroup`: Cria um grupo de radio buttons.
- `selected.text`: Obtém o texto da opção selecionada.

## SLIDERS
Os sliders permitem ao usuário selecionar um valor de um intervalo.

### CÓDIGO
```python
from flet import App, Slider

# Função para capturar o valor do slider
def slider_changed():
    value = slider.value
    print(f"Valor do slider: {value}")

# Inicializa a aplicação
app = App()

# Cria uma tela
screen = app.screen()

# Adiciona um slider
slider = Slider(screen, min=0, max=100, step=1, value=50, orientation="horizontal", on_change=slider_changed)

# Executa a aplicação
app.run()
```

### EXPLICAÇÃO
- `Slider`: Cria um slider.
- `value`: Obtém o valor atual do slider.

## COMBOBOXES
As comboboxes permitem ao usuário selecionar um valor de uma lista suspensa.

### CÓDIGO
```python
from flet import App, ComboBox, Button

# Função para obter a seleção
def get_selection():
    selecao = combobox.selected.text
    print(f"Você selecionou: {selecao}")

# Inicializa a aplicação
app = App()

# Cria uma tela
screen = app.screen()

# Adiciona uma combobox e um botão
combobox = ComboBox(screen, options=["Opção 1", "Opção 2", "Opção 3"])
button = Button(screen, text="Verificar Seleção", on_click=get_selection)

# Executa a aplicação
app.run()
```

### EXPLICAÇÃO
- `ComboBox`: Cria uma combobox.
- `selected.text`: Obtém o texto da opção selecionada.

