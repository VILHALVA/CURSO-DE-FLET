# CRIE O SEU PRIMEIRO APLICATIVO 
Para criar o seu primeiro aplicativo em Flet, podemos começar com um exemplo simples que demonstre como usar alguns dos componentes básicos oferecidos pelo framework. Vamos criar um aplicativo que exiba um formulário básico para capturar o nome e a idade do usuário. Aqui está o código:

```python
import flet as ft

def main(page):
    # Cria campos de entrada para nome e idade
    name_field = ft.TextField(label="Nome:")
    age_field = ft.TextField(label="Idade:")

    # Função para lidar com o clique do botão
    def submit_handler(event):
        name = name_field.value
        age = age_field.value
        print(f"Nome: {name}, Idade: {age}")

    # Cria um botão para enviar o formulário
    submit_button = ft.Button(text="Enviar")
    submit_button.on_click = submit_handler

    # Organiza os campos e botão em uma coluna
    column = ft.Column(controls=[name_field, age_field, submit_button])

    # Adiciona a coluna à página
    page.add(column)

# Inicia o aplicativo Flet com a função main como alvo
ft.app(target=main)
```

## Explicação do Código:
1. **Importação de Módulos**: Importamos o `flet` como `ft` para facilitar o uso dos componentes.

2. **Função `main`**: A função `main` é o ponto de entrada do aplicativo, onde você define a estrutura da interface do usuário.

3. **Campos de Entrada (`TextField`)**: Criamos dois campos de texto para capturar o nome e a idade do usuário usando `ft.TextField()`. Cada campo recebe um rótulo (`label`) para indicar sua função.

4. **Manipulador de Clique do Botão**: Definimos uma função `submit_handler` que será chamada quando o botão for clicado. Ela simplesmente imprime os valores inseridos nos campos de texto.

5. **Botão (`Button`)**: Criamos um botão usando `ft.Button()` com o texto "Enviar" e associamos a função `submit_handler` ao evento `on_click` do botão.

6. **Organização em Coluna (`Column`)**: Agrupamos os campos de texto e o botão em uma coluna usando `ft.Column()`, que organiza verticalmente os componentes.

7. **Adição à Página**: Adicionamos a coluna à página usando `page.add(column)`, onde `page` é passado como parâmetro para a função `main`.

8. **Inicialização do Aplicativo**: Finalmente, iniciamos o aplicativo Flet com `ft.app(target=main)`, especificando `main` como a função principal que define a interface do usuário.

## Funcionamento do Aplicativo:
Ao executar esse código, você verá uma interface simples com dois campos de texto (Nome e Idade) e um botão "Enviar". Ao inserir um nome e idade nos campos e clicar no botão, os valores serão impressos no console.

Este é um exemplo básico para começar com Flet, demonstrando como criar uma interface de usuário interativa usando componentes fundamentais como campos de texto e botões.