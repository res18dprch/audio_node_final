import flet as ft

def main(page: ft.Page):
    page.bgcolor = "black"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Создаем пикер ЗАРАНЕЕ, но максимально просто
    def on_result(e: ft.FilePickerResultEvent):
        if e.files:
            btn.text = f"FILE: {e.files[0].name}"
        page.update()

    picker = ft.FilePicker(on_result=on_result)
    page.overlay.append(picker)

    # Заголовок
    header = ft.Text(" > DEVICE_NODE_v5", size=25, color="#00ff41", weight="bold")
    
    # Кнопка, которая просто дергает пикер
    btn = ft.ElevatedButton(
        " [ SELECT_FILE ] ",
        on_click=lambda _: picker.pick_files(),
        style=ft.ButtonStyle(
            color="#00ff41", 
            bgcolor="#111111",
            shape=ft.RoundedRectangleBorder(radius=2)
        )
    )

    page.add(header, ft.Divider(height=20, color="transparent"), btn)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
