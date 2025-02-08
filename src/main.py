import flet as ft


def main(page: ft.Page):
    page.title = "minha primeira interface grafica"
    page.window.width = 400
    page.window.height = 200

    nome = "Denis"
    idade = 35
    altura = 1.80
    programador = "Sim"

    texto = ft.Text(f"Nome: {nome}\nidade: {idade}\naltura: {altura}\nprogramador: {programador}")

    page.add(texto)


ft.app(target=main)
