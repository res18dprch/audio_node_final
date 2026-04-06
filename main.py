import flet as ft
import os

def main(page: ft.Page):
    # Убираем все темы и навороты
    page.bgcolor = "black"
    page.padding = 50
    
    # Прямой путь, который был WRITABLE (OK)
    doc_path = os.path.join(os.path.expanduser('~'), 'Documents')

    # Просто текстовые объекты (они самые легкие для рендера)
    title = ft.Text(" > SYSTEM_BOOT_OK", color="#00ff41", size=20)
    status = ft.Text("PRESS_SCREEN_TO_SCAN", color="white")
    
    # Список файлов
    files_list = ft.Column()

    def do_scan(e):
        files_list.controls.clear()
        try:
            if not os.path.exists(doc_path):
                os.makedirs(doc_path)
            items = os.listdir(doc_path)
            status.value = f"FOUND: {len(items)} ITEMS"
            for i in items:
                files_list.controls.append(ft.Text(f" FILE: {i}", color="#00ff41"))
        except Exception as ex:
            status.value = f"ERR: {str(ex)}"
        page.update()

    # Вместо кнопок - просто кликабельный текст
    scan_trigger = ft.GestureDetector(
        content=ft.Text(" [ RUN_SCAN_CMD ] ", size=30, color="#00ff41", weight="bold"),
        on_tap=do_scan
    )

    page.add(title, status, ft.Divider(height=20), scan_trigger, files_list)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
