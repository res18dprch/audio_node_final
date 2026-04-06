import flet as ft
import os

def main(page: ft.Page):
    # Убираем все лишние настройки, оставляем только базу
    page.bgcolor = "black"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Путь к документам (самый простой вариант)
    doc_path = os.path.expanduser('~/Documents')

    header = ft.Text(" > NODE_DEBUG_v1", size=20, color="#00ff41")
    status = ft.Text("CHECKING_DOCUMENTS...", color="#555555")
    
    # Просто текстовое поле для вывода списка
    files_view = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)

    def check_folder(e=None):
        files_view.controls.clear()
        try:
            if not os.path.exists(doc_path):
                os.makedirs(doc_path)
            
            content = os.listdir(doc_path)
            if not content:
                status.value = "FOLDER_EMPTY"
            else:
                status.value = f"FOUND_{len(content)}_ITEMS"
                for item in content:
                    files_view.controls.append(ft.Text(f" - {item}", color="white"))
        except Exception as ex:
            status.value = f"ERROR: {str(ex)}"
        page.update()

    btn = ft.ElevatedButton(" [ REFRESH ] ", on_click=check_folder)

    page.add(
        header,
        status,
        ft.Container(content=files_view, height=200, border=ft.border.all(1, "#1a1a1a")),
        btn
    )
    
    page.update()
    # Запуск проверки через секунду после старта
    check_folder()

if __name__ == "__main__":
    ft.app(target=main)
