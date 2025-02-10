import flet as ft #importando a biblioteca flet

def main(page: ft.Page):#função principal
    def add_clicked(e):#função para adicionar tarefas
        page.add(ft.Checkbox(label=new_task.value))#adicionando um checkbox com o valor do input
        new_task.value = ""#limpando o input
        new_task.focus()#focando no input
        new_task.update()#atualizando o input
    
    
    def toggle_theme(e):#função para alternar o tema
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            theme_button.icon = ft.icons.WB_SUNNY_OUTLINED
        else:
            page.theme_mode = ft.ThemeMode.DARK
            theme_button.icon = ft.icons.MODE_NIGHT_OUTLINED
        page.update()#atualizando a pagina

    theme_button = ft.IconButton(icon=ft.icons.BRIGHTNESS_6, on_click=toggle_theme)#criando um botão para alternar o tema
    
    page.add(theme_button)#adicionando o botão na pagina
    #page.theme_mode = ft.ThemeMode.LIGHT  # definindo o tema inicial como claro
    page.title = "To-Do App"  # definindo o título da página
    
    #configurações da pagina
    new_task = ft.TextField(hint_text="escreva suas anotaçoes aqui", width=300)#criando um input
    page.add(ft.Row([new_task, ft.ElevatedButton("adicionar", on_click=add_clicked)]))#adicionando o input e um botão
    
    


ft.app(target=main)#iniciando a aplicação