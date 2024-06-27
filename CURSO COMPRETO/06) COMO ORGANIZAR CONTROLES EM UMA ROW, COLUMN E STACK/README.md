# COMO ORGANIZAR CONTROLES EM UMA ROW, COLUMN E STACK
Em Flet, você pode organizar controles visualmente utilizando `Row`, `Column` e `Stack` para criar layouts flexíveis e responsivos. Cada um desses componentes oferece maneiras diferentes de posicionar e alinhar outros componentes visuais, como botões, caixas de texto, entre outros. Vamos explorar como cada um funciona:

## 1. `Row`
O `Row` permite organizar os elementos horizontalmente, alinhando-os lado a lado na mesma linha. Você pode especificar o alinhamento horizontal e vertical dos elementos dentro da linha.

Exemplo de uso do `Row`:

```python
from flet import App, Row, Button

def main():
    app = App()
    row = Row()
    
    button1 = Button(row, text="Botão 1")
    button2 = Button(row, text="Botão 2")
    button3 = Button(row, text="Botão 3")

    # Configura o alinhamento dos botões dentro da linha
    row.align_items(horizontal='center', vertical='middle')

    app.set_screen(row)
    app.run()

if __name__ == "__main__":
    main()
```

- **Explicação**:
  - `Row`: Cria uma linha horizontal para posicionar os botões.
  - `align_items`: Define o alinhamento dos itens dentro da linha. `horizontal='center'` centraliza horizontalmente os botões, e `vertical='middle'` alinha os botões verticalmente ao centro da linha.

## 2. `Column`
A `Column` organiza os elementos verticalmente, colocando-os um abaixo do outro. Isso é ideal para listas verticais de itens ou formulários.

Exemplo de uso da `Column`:

```python
from flet import App, Column, Button

def main():
    app = App()
    column = Column()
    
    button1 = Button(column, text="Botão 1")
    button2 = Button(column, text="Botão 2")
    button3 = Button(column, text="Botão 3")

    # Configura o alinhamento dos botões dentro da coluna
    column.align_items(horizontal='center', vertical='middle')

    app.set_screen(column)
    app.run()

if __name__ == "__main__":
    main()
```

- **Explicação**:
  - `Column`: Cria uma coluna vertical para posicionar os botões.
  - `align_items`: Define o alinhamento dos itens dentro da coluna. `horizontal='center'` centraliza horizontalmente os botões, e `vertical='middle'` alinha os botões verticalmente ao centro da coluna.

## 3. `Stack`
O `Stack` empilha elementos um sobre o outro, permitindo sobreposição de elementos visuais. Isso pode ser útil para criar efeitos de camadas ou sobreposições de interface.

Exemplo de uso do `Stack`:

```python
from flet import App, Stack, Button

def main():
    app = App()
    stack = Stack()
    
    button1 = Button(stack, text="Botão 1")
    button2 = Button(stack, text="Botão 2")
    button3 = Button(stack, text="Botão 3")

    # Configura o alinhamento dos botões dentro da pilha
    stack.align_items(horizontal='center', vertical='middle')

    app.set_screen(stack)
    app.run()

if __name__ == "__main__":
    main()
```

- **Explicação**:
  - `Stack`: Cria uma pilha de elementos, sobrepondo-os.
  - `align_items`: Define o alinhamento dos itens dentro do stack. `horizontal='center'` centraliza horizontalmente os botões, e `vertical='middle'` alinha os botões verticalmente ao centro da pilha.


