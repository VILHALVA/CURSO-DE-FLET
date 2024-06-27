# COMO ORGANIZAR CONTROLES EM UMA LISTVIEW E GRIDVIEW
Em Flet, para organizar controles em uma `ListView` e `GridView`, você pode usar componentes específicos que ajudam a exibir e gerenciar listas de itens de forma eficiente. Vamos explorar como você pode utilizar esses componentes para criar interfaces que exibem dados em formato de lista ou grade.

## 1. `ListView`
A `ListView` em Flet é ideal para exibir uma lista de itens onde cada item pode conter dados complexos, como texto, imagens ou outros elementos. Cada item é geralmente apresentado em uma linha vertical.

Exemplo de uso da `ListView`:

```python
from flet import App, ListView, ListItem, Text

def main():
    app = App()

    # Cria uma ListView
    list_view = ListView()

    # Adiciona itens à ListView
    for i in range(1, 6):
        item = ListItem()
        item.add_content(Text(f"Item {i}"))
        list_view.add_item(item)

    app.set_screen(list_view)
    app.run()

if __name__ == "__main__":
    main()
```

- **Explicação**:
  - `ListView`: Cria uma lista vertical de itens.
  - `ListItem`: Cada item da lista.
  - `Text`: Componente de texto para exibir o conteúdo do item.

## 2. `GridView`
A `GridView` em Flet permite organizar e exibir dados em uma grade (ou tabela), onde cada célula pode conter dados diferentes. É útil para exibir dados tabulares de forma estruturada.

Exemplo de uso da `GridView`:

```python
from flet import App, GridView, GridItem, Text

def main():
    app = App()

    # Cria uma GridView
    grid_view = GridView()

    # Adiciona itens à GridView
    for i in range(1, 4):
        for j in range(1, 4):
            item = GridItem(row=i, column=j)
            item.add_content(Text(f"Cell {i},{j}"))
            grid_view.add_item(item)

    app.set_screen(grid_view)
    app.run()

if __name__ == "__main__":
    main()
```

- **Explicação**:
  - `GridView`: Cria uma grade (tabela) de itens.
  - `GridItem`: Cada célula na grade.
  - `Text`: Componente de texto para exibir o conteúdo da célula.

