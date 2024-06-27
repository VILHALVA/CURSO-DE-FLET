# COMO CRIAR UM APPBAR ( NAVBAR )
Para criar um AppBar (ou navbar, barra de navegação) em Flet, você pode usar o componente `AppBar` fornecido pelo framework. O AppBar é comumente utilizado para exibir menus, botões de navegação e outros controles de interface em um layout de aplicativo. Vamos criar um exemplo básico de como fazer isso em Flet:

Neste exemplo, vamos criar um AppBar simples com um título e alguns botões de navegação.

## 1. Importação de Módulos
Primeiro, importe os módulos necessários do Flet, incluindo `App`, `AppBar`, `IconButton` e `Text`.

```python
from flet import App, AppBar, IconButton, Text
```

## 2. Criação do AppBar
Em seguida, crie um `AppBar` e adicione elementos a ele, como título e botões.

```python
def main():
    app = App()

    # Cria um AppBar
    app_bar = AppBar()

    # Adiciona elementos ao AppBar
    title = Text(app_bar, text="Meu App")
    button1 = IconButton(app_bar, icon="menu")
    button2 = IconButton(app_bar, icon="search")

    app.set_app_bar(app_bar)

    app.run()

if __name__ == "__main__":
    main()
```

- **Explicação**:
  - `AppBar`: Cria uma barra de aplicativo (AppBar) onde você pode adicionar elementos como título e botões.
  - `Text`: Componente para exibir texto dentro do AppBar.
  - `IconButton`: Componente para adicionar botões com ícones dentro do AppBar.

## 3. Personalização e Layout
Você pode personalizar o AppBar conforme necessário, ajustando cores, estilos de texto, tamanhos e posicionamento dos elementos dentro dele.

```python
# Personalização do título
title.font_size = '20px'
title.color = 'white'

# Personalização dos botões
button1.icon_color = 'white'
button2.icon_color = 'white'
```

## Exemplo Completo
Aqui está o exemplo completo de como criar um AppBar simples em Flet:

```python
from flet import App, AppBar, IconButton, Text

def main():
    app = App()

    # Cria um AppBar
    app_bar = AppBar()

    # Adiciona elementos ao AppBar
    title = Text(app_bar, text="Meu App")
    button1 = IconButton(app_bar, icon="menu")
    button2 = IconButton(app_bar, icon="search")

    # Personalização do título
    title.font_size = '20px'
    title.color = 'white'

    # Personalização dos botões
    button1.icon_color = 'white'
    button2.icon_color = 'white'

    app.set_app_bar(app_bar)

    app.run()

if __name__ == "__main__":
    main()
```

