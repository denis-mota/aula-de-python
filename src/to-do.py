import flet as ft

def main(page: ft.Page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()


    new_task = ft.TextField(hint_text="escreva suas anotaçoes aqui", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("adicionar", on_click=add_clicked)]))

    


ft.app(target=main)