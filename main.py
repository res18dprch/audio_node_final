import flet as ft
import time

def main(page: ft.Page):
    # Настройки страницы
    page.title = "AUDIO_NODE_v5"
    page.bgcolor = "#050505"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_full_screen = True

    # Первая отрисовка пустого фона
    page.update()
    time.sleep(1.5) # Даем системе "продышаться"

    # Элементы интерфейса
    status_text = ft.Text("STATUS: SYSTEM_READY", color="#555555", size=12)
    header = ft.Text(" > DEVICE_NODE_v5.0", size=30, color="#00ff41", weight="bold")
    
    def on_click(e):
        header.value = " > SCANNING_FILES..."
        header.color = "white"
        page.update()

    btn = ft.ElevatedButton(
        " [ SELECT_AUDIO_FILES ] ",
        on_click=on_click,
        style=ft.ButtonStyle(
            color="#00ff41", 
            bgcolor="#111111",
            shape=ft.RoundedRectangleBorder(radius=2)
        )
    )

    # Добавляем всё на страницу
    page.add(
        ft.Column(
            [
                header,
                status_text,
                ft.Divider(color="#1a1a1a", height=40),
                btn
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    
    # Финальное обновление
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
