import flet as ft

def main(page: ft.Page):
    # 1. Жесткие настройки страницы
    page.bgcolor = "#000000"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 2. Компонент выбора файлов (создаем заранее)
    def on_result(e: ft.FilePickerResultEvent):
        if e.files:
            status.value = f"FILE: {e.files[0].name}"
            status.color = "#00ff41"
        page.update()

    picker = ft.FilePicker(on_result=on_result)
    page.overlay.append(picker)

    # 3. Элементы интерфейса
    header = ft.Text(" > NODE_V5", size=30, color="#00ff41", weight="bold")
    status = ft.Text("STATUS: STANDBY", color="#555555")
    
    btn = ft.ElevatedButton(
        " [ OPEN_STORAGE ] ",
        on_click=lambda _: picker.pick_files(),
        style=ft.ButtonStyle(
            color="#00ff41", 
            bgcolor="#111111",
            shape=ft.RoundedRectangleBorder(radius=2)
        )
    )

    # 4. Добавляем всё ОДНИМ махом
    page.add(
        ft.Column(
            [
                header,
                status,
                ft.Divider(height=20, color="transparent"),
                btn
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    
    # ФИНАЛЬНЫЙ ПИНОК
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
