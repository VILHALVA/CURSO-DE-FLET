# ESTRUTURA BÁSICA DO APLICATIVO FLET
A estrutura básica de um aplicativo Flet envolve alguns elementos essenciais para criar e executar uma aplicação interativa. Aqui está como você pode estruturar um aplicativo Flet de forma simples:

## 1. Importação de Módulos
No início do seu script Python, você precisa importar os módulos necessários do Flet que serão utilizados no seu aplicativo, como `App`, `Label`, `Button`, entre outros componentes conforme necessário.

```python
from flet import App, Label, Button
```

## 2. Definição de Funções
Seu aplicativo pode incluir funções que serão chamadas em resposta a eventos, como cliques de botões ou alterações em controles de entrada de texto. Por exemplo:

```python
def on_click_button():
    label.text = "Botão clicado!"
```

## 3. Inicialização da Aplicação
Você inicializa sua aplicação Flet criando uma instância da classe `App`. Esta instância é essencial para gerenciar a execução da aplicação e a interação com a interface gráfica.

```python
app = App()
```

## 4. Criação da Interface Gráfica
Dentro do contexto da sua aplicação (`App`), você cria uma tela (`screen`) onde todos os elementos visuais serão colocados.

```python
screen = app.screen()
```

## 5. Adição de Componentes Visuais
Você adiciona componentes visuais, como `Label`, `Button`, `TextInput`, etc., à tela (`screen`) que você criou. Cada componente é configurado com suas propriedades específicas, como posição, texto exibido, comportamento de eventos, etc.

```python
label = Label(screen, text="Olá, Flet!")
button = Button(screen, text="Clique Aqui", on_click=on_click_button)
```

## 6. Execução da Aplicação
Finalmente, você inicia o loop principal da aplicação chamando o método `run()` do objeto `App`. Isso exibe a interface gráfica para o usuário e aguarda interações.

```python
app.run()
```

## Exemplo Completo
Aqui está um exemplo completo que mostra a estrutura básica de um aplicativo Flet que exibe um label e um botão:

```python
from flet import App, Label, Button

# Função para manipular o clique do botão
def on_click_button():
    label.text = "Botão clicado!"

# Inicializa a aplicação
app = App()

# Cria uma tela
screen = app.screen()

# Adiciona um label e um botão à tela
label = Label(screen, text="Olá, Flet!")
button = Button(screen, text="Clique Aqui", on_click=on_click_button)

# Executa a aplicação
app.run()
```

Esta estrutura básica pode ser expandida adicionando mais componentes visuais, como caixas de texto, checkboxes, radio buttons, sliders, etc., e definindo mais funções para manipular seus eventos.