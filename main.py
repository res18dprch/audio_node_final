import flet as ft
import time

def main(page: ft.Page):
    # Убираем все лишнее, оставляем только базу
    page.bgcolor = "#000000"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Принудительное обновление страницы до добавления текста
    page.update()
    
    # Небольшая пауза старым добрым методом
    time.sleep(2)

    # Яркий текст, который точно должно быть видно
    text_node = ft.Text(
        " > READY_TO_WORK",
        size=35,
        color="#00FF41",
        weight="bold",
        font_family="monospace"
    )

    page.add(text_node)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
