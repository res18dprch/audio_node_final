import flet as ft
import os

def main(page: ft.Page):
    # Жесткая настройка визуала
    page.bgcolor = "black"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Используем стандартную песочницу Flet
    # Это путь, который iOS 100% открывает для папки "Файлы"
    upload_path = os.getenv("FLET_APP_STORAGE_DATA") or os.getcwd()

    header = ft.Text(" > NODE_AUDIO_v5", size=25, color="#00ff41", weight="bold")
    status = ft.Text("STATUS: WAITING", color="#555555")
    
    files_list = ft.ListView(expand=1, spacing=5)
    audio_player = ft.Audio(src="", autoplay=False)
    page.overlay.append(audio_player)

    def play_file(e):
        audio_player.src = os.path.join(upload_path, e.control.data)
        audio_player.play()
        status.value = f"PLAYING: {e.control.data}"
        page.update()

    def refresh(e=None):
        files_list.controls.clear()
        try:
            # Проверяем файлы в текущей папке
            for f in os.listdir(upload_path):
                if f.lower().endswith((".mp3", ".wav", ".m4a")):
                    files_list.controls.append(
                        ft.TextButton(
                            text=f" > {f}",
                            data=f,
                            on_click=play_file,
                            style=ft.ButtonStyle(color="white")
                        )
                    )
            if not files_list.controls:
                status.value = "EMPTY: ADD MP3 IN 'FILES' APP"
            else:
                status.value = f"FILES_FOUND: {len(files_list.controls)}"
        except Exception as ex:
            status.value = f"ERROR: {str(ex)}"
        page.update()

    page.add(
        header,
        status,
        ft.Divider(color="#1a1a1a"),
        ft.Container(content=files_list, height=200),
        ft.ElevatedButton(" [ REFRESH ] ", on_click=refresh)
    )
    
    page.update()
    refresh()

if __name__ == "__main__":
    ft.app(target=main)
