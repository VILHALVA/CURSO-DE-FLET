import flet as ft

def main(page: ft.Page):
    page.title = "Cálculo do IMC"
    
    def button_clicked(e):
        # Remove quaisquer caracteres não numéricos da entrada
        peso = ''.join(c for c in tb1.value if c.isdigit())
        altura = ''.join(c for c in tb2.value if c.isdigit())

        # Insere um ponto no lugar correto para converter a altura para metros
        if len(altura) > 2:
            altura = altura[:-2] + '.' + altura[-2:]

        try:
            # Tenta converter os valores de peso e altura para float
            peso = float(peso)
            altura = float(altura)
        except ValueError:
            # Se a conversão falhar, mostra uma mensagem de erro e retorna
            t.value = "Por favor, insira apenas números nas caixas de texto."
            return

        # Realiza o cálculo do IMC
        imc = peso / (altura**2)
        
        t.value = f"O seu Imc é : '{format(imc, '.2f')}'."
                
        # Define a mensagem de acordo com o valor do IMC
        if imc < 17:
            imcmensagem.value = 'Você está muito abaixo do peso'
        elif imc >= 17 and imc <= 18.49:
            imcmensagem.value = 'Você está abaixo do peso'
        elif imc >= 18.5 and imc <= 24.99:
            imcmensagem.value = 'Você está no peso normal'
        elif imc >= 25 and imc <= 29.99:
            imcmensagem.value = 'Acima do Peso'
        elif imc >= 30 and imc <= 34.99:
            imcmensagem.value = 'Obesidade Grau I'
        elif imc >= 35 and imc <= 39.99:
            imcmensagem.value = 'Obesidade Grau II (Severa)'
        else:
            imcmensagem.value = 'Obesidade Grau III (Mórbida)'
        
        page.update()

    t_imc = ft.Text(value="Cálculo do IMC:")
    page.add(t_imc)

    t = ft.Text()
    tb1 = ft.TextField(label="Peso")
    tb2 = ft.TextField(label="Altura (em cm)")
    b = ft.ElevatedButton(text="CALCULAR", on_click=button_clicked)
    imcmensagem = ft.Text(value="")
    
    img = ft.Image(src='./FOTO.jpg')
    page.add(img, tb1, tb2, b, t, imcmensagem)

ft.app(target=main)