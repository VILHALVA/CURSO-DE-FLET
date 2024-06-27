# COMO INSTALAR FLET
## Usando pip (Python Package Index)
1. **Verifique se o Python e o pip estão instalados**: Certifique-se de ter o Python instalado em seu sistema. Você pode verificar isso digitando `python --version` e `pip --version` no terminal ou prompt de comando.

2. **Instale o Flet**: Execute o seguinte comando para instalar o Flet usando pip:

   ```
   pip install flet
   ```

   Este comando irá baixar e instalar o pacote Flet e suas dependências.

## Verificação da Instalação
Para verificar se a instalação foi bem-sucedida, você pode executar um script simples de teste no seu ambiente Python:

```python
from flet import App, Label

# Inicializa a aplicação
app = App()

# Cria uma tela
screen = app.screen()

# Adiciona um label à tela
label = Label(screen, text="Flet está funcionando!")

# Executa a aplicação
app.run()
```

Se a instalação foi feita corretamente, você deve ver uma janela ou tela exibindo o texto "Flet está funcionando!".

## Considerações
- **Compatibilidade**: O Python Flet suporta Python 3.6 e versões superiores.
- **Ambiente Virtual (opcional)**: É recomendável usar um ambiente virtual para gerenciar suas dependências Python de forma isolada, especialmente se você estiver trabalhando em vários projetos.
- **Documentação**: Para mais detalhes e exemplos, você pode consultar a [documentação oficial do Python Flet](https://flet.dev/docs).

Ao seguir essas instruções, você deve conseguir instalar o Python Flet e começar a desenvolver suas aplicações com este framework.