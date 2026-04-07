import flet as ft

def main(page: ft.Page):
    # Устанавливаем принудительно белый фон, чтобы проверить, работает ли отрисовка
    page.bgcolor = "white"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Добавляем один простой текст
    page.add(
        ft.Text("SYSTEM ONLINE: V18", size=40, color="black", weight="bold")
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
