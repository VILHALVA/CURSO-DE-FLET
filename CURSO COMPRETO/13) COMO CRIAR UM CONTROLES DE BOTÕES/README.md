# COMO CRIAR UM CONTROLES DE BOTÕES
Para criar controles de botões em Flet, você pode usar o componente `Button` fornecido pelo framework. Os botões são fundamentais para permitir interações do usuário, como executar ações, enviar formulários ou navegar entre telas. Vamos criar um exemplo básico de como fazer isso em Flet:

Neste exemplo, vamos criar um botão simples que imprime uma mensagem no console quando clicado.

## 1. Importação de Módulos
Primeiro, importe os módulos necessários do Flet, incluindo `App` e `Button`.

```python
from flet import App, Button
```

## 2. Criação do Controle de Botão
Em seguida, crie um `Button` e defina a função que será executada quando o botão for clicado.

```python
def on_click(event):
    print("Botão clicado!")

def main():
    app = App()

    # Cria um botão
    button = Button(text="Clique Aqui")
    button.on_click = on_click  # Define a função de clique do botão

    app.set_screen(button)
    app.run()

if __name__ == "__main__":
    main()
```

- **Explicação**:
  - `Button`: Cria um botão que permite ao usuário realizar uma ação quando clicado.
  - `text`: Parâmetro para definir o texto exibido no botão.
  - `on_click`: Propriedade que recebe a função a ser executada quando o botão é clicado.

## Exemplo Completo
Aqui está o exemplo completo de como criar um controle de botão em Flet:

```python
from flet import App, Button

def on_click(event):
    print("Botão clicado!")

def main():
    app = App()

    # Cria um botão
    button = Button(text="Clique Aqui")
    button.on_click = on_click  # Define a função de clique do botão

    app.set_screen(button)
    app.run()

if __name__ == "__main__":
    main()
```

## Considerações Adicionais
- **Personalização**: Você pode personalizar o botão ajustando propriedades como cor, tamanho de fonte, estilo de texto, entre outros.
  
- **Integração com Eventos**: Além do clique (`on_click`), os botões em Flet podem suportar outros eventos como `on_hover`, `on_press`, `on_release`, dependendo da necessidade da aplicação.
  
- **Layout e Posicionamento**: Os botões podem ser posicionados em diferentes layouts como `Row`, `Column`, `Stack`, ou diretamente na tela conforme necessário.

Criar controles de botões em Flet é fundamental para adicionar funcionalidades interativas à sua aplicação, permitindo aos usuários executar ações de maneira intuitiva e eficaz.