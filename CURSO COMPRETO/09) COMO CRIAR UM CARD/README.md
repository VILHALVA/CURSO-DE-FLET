# COMO CRIAR UM CARD 
Para criar um "card" em Flet, você pode utilizar uma combinação de componentes visuais para organizar e exibir informações de maneira visualmente agradável e estruturada. Um "card" é geralmente usado para representar um único item ou conjunto de informações em um formato compacto e fácil de ler. Vamos criar um exemplo básico de como fazer isso em Flet:

Neste exemplo, vamos criar um card simples que contém um título, uma descrição e um botão.

## 1. Importação de Módulos
Primeiro, importe os módulos necessários do Flet, incluindo `App`, `Card`, `Text` e `Button`.

```python
from flet import App, Card, Text, Button
```

## 2. Criação do Card
Em seguida, crie um `Card` e adicione elementos a ele, como texto e botão.

```python
def main():
    app = App()

    # Cria um Card
    card = Card()

    # Adiciona conteúdo ao Card
    title = Text(card, text="Título do Card")
    description = Text(card, text="Descrição do Card")
    button = Button(card, text="Botão")

    app.set_screen(card)
    app.run()

if __name__ == "__main__":
    main()
```

- **Explicação**:
  - `Card`: Cria um card no qual você pode adicionar outros componentes visuais.
  - `Text`: Componente para exibir texto dentro do card.
  - `Button`: Componente para adicionar botões dentro do card.

## 3. Personalização e Layout
Você pode personalizar o card conforme necessário, ajustando cores, estilos de texto, tamanhos e posicionamento dos elementos dentro do card.

```python
# Personalização do título
title.font_size = '20px'
title.color = 'blue'

# Personalização do botão
button.background_color = 'green'
button.text_color = 'white'
```

## Exemplo Completo
Aqui está o exemplo completo de como criar um card simples em Flet:

```python
from flet import App, Card, Text, Button

def main():
    app = App()

    # Cria um Card
    card = Card()

    # Adiciona conteúdo ao Card
    title = Text(card, text="Título do Card")
    description = Text(card, text="Descrição do Card")
    button = Button(card, text="Botão")

    # Personalização do título
    title.font_size = '20px'
    title.color = 'blue'

    # Personalização do botão
    button.background_color = 'green'
    button.text_color = 'white'

    app.set_screen(card)
    app.run()

if __name__ == "__main__":
    main()
```

