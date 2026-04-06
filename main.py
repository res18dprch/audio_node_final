import flet as ft
import time

def main(page: ft.Page):
    # 1. Настройки страницы - максимально простые
    page.bgcolor = "black"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Даем системе 1 секунду просто показать черный экран
    page.update()
    time.sleep(1)

    # 2. Основной текст
    status = ft.Text(" > SYSTEM_STABLE", size=20, color="#00ff41")
    page.add(status)
    page.update()

    # 3. Функция, которая создаст Picker ТОЛЬКО при нажатии
    def start_selection(e):
        status.value = " > INITIALIZING_PICKER..."
        status.color = "white"
        page.update()
        
        # Создаем picker прямо здесь, "на лету"
        def on_result(res: ft.FilePickerResultEvent):
            if res.files:
                status.value = f" > SELECTED: {res.files[0].name}"
                status.color = "#00ff41"
            page.update()

        picker = ft.FilePicker(on_result=on_result)
        page.overlay.append(picker)
        page.update()
        
        # Сразу запускаем выбор
        picker.pick_files()

    # 4. Кнопка
    btn = ft.ElevatedButton(
        " [ START_PROCESS ] ",
        on_click=start_selection,
        style=ft.ButtonStyle(color="#00ff41", bgcolor="#111111")
    )
    
    page.add(ft.Divider(height=20, color="transparent"), btn)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
