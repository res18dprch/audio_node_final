import flet as ft
import os

def main(page: ft.Page):
    page.bgcolor = "black"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    # Создаем путь к папке Документы
    doc_path = os.path.expanduser('~/Documents')
    music_dir = os.path.join(doc_path, "MUSIC_NODE")
    
    # Пытаемся создать папку, если её нет
    try:
        if not os.path.exists(music_dir):
            os.makedirs(music_dir)
        status_msg = "FOLDER_READY"
    except Exception as e:
        status_msg = f"ERROR: {str(e)}"

    header = ft.Text(" > AUDIO_NODE_v5", size=25, color="#00ff41", weight="bold")
    path_text = ft.Text(f"PATH: {music_dir}", size=10, color="#555555", selectable=True)
    
    files_list = ft.ListView(expand=1, spacing=10)

    def scan(e=None):
        files_list.controls.clear()
        for f in os.listdir(music_dir):
            if f.endswith((".mp3", ".wav")):
                files_list.controls.append(ft.Text(f" [OK] {f}", color="white"))
        if not files_list.controls:
            files_list.controls.append(ft.Text("EMPTY: COPY MP3 TO THIS FOLDER", color="red"))
        page.update()

    btn = ft.ElevatedButton(" [ REFRESH ] ", on_click=scan, style=ft.ButtonStyle(color="#00ff41"))

    page.add(header, status_msg, path_text, ft.Container(files_list, height=150), btn)
    page.update()
    scan()

if __name__ == "__main__":
    ft.app(target=main)
