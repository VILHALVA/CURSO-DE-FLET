# COMO CRIAR UM DATATABLE ( TABELA )
Para criar um `DataTable` (tabela de dados) em Flet, você pode utilizar o componente `DataTable` fornecido pelo framework. Um `DataTable` é usado para exibir dados tabulares de forma organizada e interativa, permitindo que os usuários visualizem, filtrem e manipulem conjuntos de dados. Vamos criar um exemplo básico de como fazer isso em Flet:

Neste exemplo, vamos criar um `DataTable` simples que exibe informações fictícias de clientes, incluindo nome, idade e cidade.

## 1. Importação de Módulos
Primeiro, importe os módulos necessários do Flet, incluindo `App`, `DataTable`, `DataRow` e `Text`.

```python
from flet import App, DataTable, DataRow, Text
```

## 2. Criação do DataTable
Em seguida, crie um `DataTable` e adicione linhas de dados a ele usando `DataRow`.

```python
def main():
    app = App()

    # Cria um DataTable
    data_table = DataTable()

    # Adiciona cabeçalho ao DataTable
    data_table.add_header("Nome", "Idade", "Cidade")

    # Adiciona linhas de dados ao DataTable
    data_table.add_row(DataRow(["João", "30", "São Paulo"]))
    data_table.add_row(DataRow(["Maria", "25", "Rio de Janeiro"]))
    data_table.add_row(DataRow(["Carlos", "35", "Belo Horizonte"]))
    data_table.add_row(DataRow(["Ana", "28", "Curitiba"]))

    app.set_screen(data_table)
    app.run()

if __name__ == "__main__":
    main()
```

- **Explicação**:
  - `DataTable`: Cria uma tabela de dados onde você pode adicionar cabeçalhos e linhas de dados.
  - `DataRow`: Representa uma linha de dados na tabela.
  - `Text`: Componente para exibir texto dentro das células da tabela.

## Exemplo Completo
Aqui está o exemplo completo de como criar um DataTable simples em Flet:

```python
from flet import App, DataTable, DataRow, Text

def main():
    app = App()

    # Cria um DataTable
    data_table = DataTable()

    # Adiciona cabeçalho ao DataTable
    data_table.add_header("Nome", "Idade", "Cidade")

    # Adiciona linhas de dados ao DataTable
    data_table.add_row(DataRow(["João", "30", "São Paulo"]))
    data_table.add_row(DataRow(["Maria", "25", "Rio de Janeiro"]))
    data_table.add_row(DataRow(["Carlos", "35", "Belo Horizonte"]))
    data_table.add_row(DataRow(["Ana", "28", "Curitiba"]))

    app.set_screen(data_table)
    app.run()

if __name__ == "__main__":
    main()
```

## Considerações Adicionais
- **Personalização**: Você pode personalizar as células da tabela, como ajustar cores, tamanhos de fonte e estilos de texto.
  
- **Ordenação e Filtros**: O `DataTable` em Flet pode suportar funcionalidades avançadas como ordenação e filtros, dependendo da configuração e implementação.

- **Eventos**: Adicione manipuladores de eventos às células da tabela para permitir interações do usuário, como clicar em uma linha para exibir mais detalhes ou editar dados.

Criar um `DataTable` em Flet é uma maneira eficiente de exibir e manipular conjuntos de dados de forma organizada e interativa em suas aplicações, proporcionando uma experiência de usuário melhorada ao lidar com informações tabulares.