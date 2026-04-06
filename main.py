import flet as ft
import os
import shutil

def main(page: ft.Page):
    # 1. Принудительные настройки экрана
    page.bgcolor = "black"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_prevent_close = True

    # Путь к проверенной папке Documents
    doc_path = os.path.join(os.path.expanduser('~'), 'Documents')
    
    # Переменные для компонентов (создадим их позже)
    state = {
        "audio": None,
        "picker": None
    }

    # Интерфейс
    header = ft.Text(" > NODE_ULTIMATE_v8", size=22, color="#00ff41", weight="bold")
    status = ft.Text("SYSTEM_READY", color="#555555")
    files_view = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)

    def play_file(e):
        if state["audio"] is None:
            state["audio"] = ft.Audio(src="", autoplay=False)
            page.overlay.append(state["audio"])
        
        state["audio"].src = os.path.join(doc_path, e.control.data)
        state["audio"].play()
        status.value = f"PLAYING: {e.control.data}"
        page.update()

    def on_file_result(e: ft.FilePickerResultEvent):
        if e.files:
            for f in e.files:
                dest = os.path.join(doc_path, f.name)
                try:
                    shutil.copy(f.path, dest)
                except: pass
            status.value = "FILES_ADDED"
            refresh_list()
        page.update()

    def init_and_pick(e):
        # Создаем пикер только в момент нажатия
        if state["picker"] is None:
            state["picker"] = ft.FilePicker(on_result=on_file_result)
            page.overlay.append(state["picker"])
            page.update()
        state["picker"].pick_files(allow_multiple=True)

    def refresh_list(e=None):
        files_view.controls.clear()
        try:
            if not os.path.exists(doc_path): os.makedirs(doc_path)
            items = [f for f in os.listdir(doc_path) if f.lower().endswith((".mp3", ".wav", ".m4a"))]
            for f in items:
                files_view.controls.append(
                    ft.TextButton(text=f" [ > ] {f}", data=f, on_click=play_file, style=ft.ButtonStyle(color="white"))
                )
            status.value = f"STORAGE: {len(items)} TRACKS"
        except Exception as ex:
            status.value = f"FS_ERROR"
        page.update()

    # Сборка экрана
    page.add(
        header,
        status,
        ft.Container(content=files_view, height=300, border=ft.border.all(1, "#1a1a1a"), padding=10),
        ft.Row([
            ft.ElevatedButton(" [ + ] ADD ", on_click=init_and_pick, style=ft.ButtonStyle(color="#00ff41", bgcolor="#111111")),
            ft.ElevatedButton(" [ R ] REFRESH ", on_click=refresh_list, style=ft.ButtonStyle(color="white", bgcolor="#111111"))
        ], alignment="center")
    )
    
    page.update()
    refresh_list()

if __name__ == "__main__":
    ft.app(target=main)
