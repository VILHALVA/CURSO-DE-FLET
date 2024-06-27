# COMO CRIA CALCULADORA DE ÍNDICE DE MASSA CORPORAL (IMC)
Para criar uma calculadora de Índice de Massa Corporal (IMC) utilizando a biblioteca Flet, podemos desenvolver uma aplicação simples onde o usuário pode inserir seu peso e altura para calcular o IMC. Vamos seguir com um exemplo básico:

```python
import flet as ft

def main(page):
    # Função para calcular o IMC
    def calcular_imc(event):
        try:
            peso = float(input_peso.value)
            altura = float(input_altura.value)
            imc = peso / (altura ** 2)

            # Exibe o resultado do IMC
            resultado_imc.value = f"Seu IMC é: {imc:.2f}"
        except ValueError:
            # Caso haja erro na conversão dos valores
            resultado_imc.value = "Por favor, insira valores válidos."

    # Criação dos elementos da interface
    input_peso = ft.TextField(label="Peso (kg):")
    input_altura = ft.TextField(label="Altura (m):")
    botao_calcular = ft.ElevatedButton("Calcular", on_click=calcular_imc)
    resultado_imc = ft.Text("")

    # Organização dos elementos em uma coluna
    column = ft.Column(controls=[input_peso, input_altura, botao_calcular, resultado_imc])

    # Adiciona a coluna à página
    page.add(column)

# Inicia a aplicação Flet com a função main como alvo
ft.app(target=main)
```

## Explicação do Código:
1. **Importação da Biblioteca Flet**: Importamos a biblioteca Flet usando `import flet as ft`.

2. **Função `main`**: Esta é a função principal que define a estrutura da interface gráfica. Ela recebe um parâmetro `page`, que representa a página principal da interface.

3. **Função `calcular_imc`**: Esta função é chamada quando o botão "Calcular" é clicado. Ela calcula o IMC com base nos valores inseridos nos campos de texto `input_peso` e `input_altura`, exibindo o resultado no elemento `resultado_imc`.

4. **Criação de Elementos de Interface**:
   - `input_peso`: Campo de texto para inserir o peso, com rótulo "Peso (kg):".
   - `input_altura`: Campo de texto para inserir a altura, com rótulo "Altura (m):".
   - `botao_calcular`: Botão elevado com o texto "Calcular", que quando clicado executa a função `calcular_imc`.
   - `resultado_imc`: Elemento de texto inicializado vazio para exibir o resultado do cálculo do IMC.

5. **Organização dos Elementos em uma Coluna**: Os elementos são organizados verticalmente em uma coluna (`Column`) usando `ft.Column(controls=[...])`.

6. **Adição da Coluna à Página**: A coluna é adicionada à página principal usando `page.add(column)`.

7. **Execução da Aplicação**: A aplicação Flet é iniciada com a função `main` como alvo principal usando `ft.app(target=main)`.

## Funcionamento da Aplicação:
Ao executar este código, uma interface gráfica será exibida com dois campos de texto para inserir peso e altura, um botão "Calcular" e uma área de texto para exibir o resultado do IMC. Ao inserir os valores válidos de peso e altura e clicar em "Calcular", o IMC será calculado e exibido com duas casas decimais.

Este exemplo demonstra como criar uma aplicação simples de calculadora de IMC usando a biblioteca Flet, permitindo interações intuitivas com o usuário através de elementos de interface gráfica como campos de texto e botões.