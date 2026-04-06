import flet as ft
import time

def main(page: ft.Page):
    # 1. Базовые настройки
    page.title = "NODE_FINAL"
    page.bgcolor = "black"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    
    # 2. РИСУЕМ ЭКРАН (Сначала только база!)
    page.update()
    time.sleep(2.0) # Даем 2 секунды на прогрузку черного фона

    header = ft.Text(" > SYSTEM_LOADED", size=25, color="#00ff41", weight="bold")
    page.add(header)
    page.update() 
    
    # 3. ПОДКЛЮЧАЕМ ТЯЖЕЛЫЕ МОЗГИ (После паузы)
    time.sleep(1.0)
    
    def on_result(e: ft.FilePickerResultEvent):
        if e.files:
            header.value = f" > FILE: {e.files[0].name}"
            header.color = "white"
        page.update()

    picker = ft.FilePicker(on_result=on_result)
    page.overlay.append(picker) # Добавляем скрытый компонент выбора
    
    # 4. ПОКАЗЫВАЕМ КНОПКУ
    btn = ft.ElevatedButton(
        " [ ACCESS_STORAGE ] ",
        on_click=lambda _: picker.pick_files(),
        style=ft.ButtonStyle(color="#00ff41", bgcolor="#111111")
    )
    
    page.add(ft.Divider(height=20, color="transparent"), btn)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
