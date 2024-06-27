# MANUAL
## INSTALAÇÃO DO FLET:
### PASSO 1: INSTALAR PYTHON:
Certifique-se de ter o Python instalado. Você pode baixar a versão mais recente do Python em [python.org](https://www.python.org/). Durante a instalação, marque a opção para adicionar Python ao PATH.

### PASSO 2: INSTALAR O FLET:
Você pode instalar o Flet usando o pip. Abra um terminal ou prompt de comando e execute o seguinte comando:

```sh
pip install flet
```

## CONFIGURAÇÃO:
### PASSO 1: VERIFICAR A INSTALAÇÃO:
Para verificar se a instalação foi bem-sucedida, você pode executar o seguinte comando no terminal:

```sh
python -c "import flet; print('Flet está instalado corretamente.')"
```

Se não houver erros, a instalação foi concluída com sucesso.

## CRIANDO O PRIMEIRO PROJETO COM FLET:
### PASSO 1: CRIAR UM ARQUIVO PYTHON:
Crie um novo arquivo Python chamado `hello_flet.py`.

### PASSO 2: ESCREVER O CÓDIGO:
Abra o `hello_flet.py` em seu editor de texto ou IDE favorito e adicione o seguinte código inicial básico:

```python
import flet

# Inicializa a aplicação Flet
app = flet.App()

# Cria uma janela principal
window = flet.Window(title="Meu Primeiro Aplicativo Flet", size=(400, 300))

# Adiciona um componente de texto à janela
text = flet.Text(window, text="Olá, Flet!", pos=(20, 20))

# Mostra a janela
window.show()

# Executa o loop da aplicação
app.run()
```

### PASSO 3: EXECUTAR O PROJETO:
Salve o arquivo e execute-o no terminal ou prompt de comando com o seguinte comando:

```sh
python hello_flet.py
```

Uma janela deve aparecer com a mensagem "Olá, Flet!".

## ESTRUTURA DO PROJETO:
Para projetos maiores, é recomendado organizar seu código em uma estrutura de diretórios. Aqui está um exemplo básico de estrutura de diretórios para um projeto Flet:

```
meu_projeto_flet/
│
├── main.py           # Ponto de entrada do aplicativo
├── gui/
│   ├── __init__.py   # Arquivo de inicialização do módulo
│   ├── main_window.py# Arquivo que define a janela principal
│
├── resources/        # Diretório para recursos como imagens, arquivos de estilo, etc.
```

### EXEMPLO DE `main_window.py`:
```python
import flet

class MainWindow(flet.Window):
    def __init__(self, title, size):
        super().__init__(title=title, size=size)

        panel = flet.Panel(self)
        text = flet.Text(panel, text="Bem-vindo ao Flet!", pos=(20, 20))

        self.show()
```

### EXEMPLO DE `main.py`
```python
import flet
from gui.main_window import MainWindow

def main():
    app = flet.App()
    
    window = MainWindow("Aplicativo Flet Estruturado", (400, 300))
    window.show()
    
    app.run()

if __name__ == '__main__':
    main()
```

Esse é um guia básico para começar a desenvolver aplicações usando o Flet. Para mais detalhes e funcionalidades avançadas, consulte a [documentação oficial do Flet.](https://flet.dev/docs/)
