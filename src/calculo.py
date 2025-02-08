import flet as ft

def main(page: ft.Page):
    page.title = "soma"
    page.window.width = 400
    page.window.height = 300

    a = 10
    b = 5

    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b
    divisao_inteira = a // b
    resto = a % b
    potencia = a ** b

    texto = ft.Text(f"soma: {soma}\nsubtracao: {subtracao}\nmultiplicacao: {multiplicacao}\ndivisao: {divisao}\ndivisao inteira: {divisao_inteira}\nresto: {resto}\npotencia: {potencia}")

    page.add(texto)

ft.app(target=main)