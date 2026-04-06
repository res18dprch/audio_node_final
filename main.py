import flet as ft
import time

def main(page: ft.Page):
    page.title = "AUDIO_NODE_v5"
    page.bgcolor = "#050505"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Пробиваем черный экран
    page.update()
    time.sleep(1.5)

    header = ft.Text(" > DEVICE_NODE_v5.0", size=30, color="#00ff41", weight="bold")
    file_info = ft.Text("NO_FILE_SELECTED", color="#555555", size=12)

    # Функция, которая сработает после выбора файла
    def on_file_result(e: ft.FilePickerResultEvent):
        if e.files:
            header.value = f" > LOADED: {e.files[0].name}"
            header.color = "white"
            file_info.value = f"SIZE: {e.files[0].size} bytes | PATH: OK"
        else:
            header.value = " > SELECTION_CANCELLED"
            header.color = "#ff4141"
        page.update()

    # Создаем компонент выбора файлов
    file_picker = ft.FilePicker(on_result=on_file_result)
    page.overlay.append(file_picker)

    btn = ft.ElevatedButton(
        " [ OPEN_STORAGE ] ",
        on_click=lambda _: file_picker.pick_files(allow_multiple=False),
        style=ft.ButtonStyle(
            color="#00ff41", 
            bgcolor="#111111",
            shape=ft.RoundedRectangleBorder(radius=2)
        )
    )

    page.add(
        ft.Column(
            [
                header,
                file_info,
                ft.Divider(color="#1a1a1a", height=40),
                btn
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
