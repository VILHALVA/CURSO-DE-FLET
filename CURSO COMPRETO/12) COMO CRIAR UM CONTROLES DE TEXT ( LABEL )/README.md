# COMO CRIAR UM CONTROLES DE TEXT ( LABEL )
Para criar um controle de texto (label) em Flet, você pode utilizar o componente `Text` fornecido pelo framework. Um controle de texto é utilizado para exibir texto estático na interface do usuário, sendo útil para títulos, descrições ou qualquer outro conteúdo que não precise ser editado pelo usuário. Vamos criar um exemplo básico de como fazer isso em Flet:

Neste exemplo, vamos criar um controle de texto simples para exibir um título na interface.

## 1. Importação de Módulos
Primeiro, importe os módulos necessários do Flet, incluindo `App` e `Text`.

```python
from flet import App, Text
```

## 2. Criação do Controle de Texto
Em seguida, crie um `Text` e configure o texto que deseja exibir.

```python
def main():
    app = App()

    # Cria um controle de texto (label)
    label = Text(text="Bem-vindo ao Meu App!")

    app.set_screen(label)
    app.run()

if __name__ == "__main__":
    main()
```

- **Explicação**:
  - `Text`: Cria um controle de texto para exibir texto estático na interface.
  - `text`: Parâmetro para definir o texto que será exibido pelo controle.

## Exemplo Completo
Aqui está o exemplo completo de como criar um controle de texto (label) em Flet:

```python
from flet import App, Text

def main():
    app = App()

    # Cria um controle de texto (label)
    label = Text(text="Bem-vindo ao Meu App!")

    app.set_screen(label)
    app.run()

if __name__ == "__main__":
    main()
```

## Considerações Adicionais
- **Personalização**: Você pode personalizar o controle de texto ajustando propriedades como cor, tamanho de fonte, alinhamento e estilo.
  
- **Integração com Layouts**: O controle de texto pode ser facilmente integrado em layouts mais complexos, como `Row`, `Column` ou outros componentes de layout disponíveis no Flet.
  
- **Interatividade**: Por ser um texto estático, não possui eventos diretamente associados. Para interatividade, considere outros componentes como botões ou elementos de entrada de texto.

Criar controles de texto em Flet é simples e eficaz para exibir informações estáticas de maneira clara e organizada na sua aplicação.