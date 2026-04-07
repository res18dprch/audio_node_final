import flet as ft
import os

def main(page: ft.Page):
    page.bgcolor = "white"
    page.padding = 20
    
    # Путь к твоей папке
    doc_path = os.path.join(os.path.expanduser('~'), 'Documents')
    
    # Элементы интерфейса
    title = ft.Text("AUDIO_NODE_FINAL", size=24, color="black", weight="bold")
    status = ft.Text("Status: Waiting", color="blue")
    files_list = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO)
    
    # Аудио-плеер
    audio_player = ft.Audio(src="", autoplay=True)
    page.overlay.append(audio_player)

    def play_track(e):
        track_name = e.control.data
        audio_player.src = os.path.join(doc_path, track_name)
        audio_player.play()
        status.value = f"Playing: {track_name}"
        page.update()

    def refresh_list(e=None):
        files_list.controls.clear()
        try:
            # Получаем список всех mp3, m4a и даже файлов без расширения (как твой signal)
            items = [f for f in os.listdir(doc_path) if not f.startswith('.')]
            
            if not items:
                status.value = "No files found in folder"
            else:
                status.value = f"Found {len(items)} items"
                for f in items:
                    # Создаем кнопку для каждого файла
                    files_list.controls.append(
                        ft.Container(
                            content=ft.Row([
                                ft.Icon(ft.icons.AUDIO_FILE, color="black"),
                                ft.Text(f, color="black", size=16, weight="medium"),
                                ft.ElevatedButton("PLAY", on_click=play_track, data=f)
                            ], alignment="spaceBetween"),
                            padding=10,
                            border=ft.border.all(1, "lightgrey"),
                            border_radius=10
                        )
                    )
        except Exception as ex:
            status.value = f"Error: {str(ex)}"
        page.update()

    # Сборка экрана
    page.add(
        title,
        status,
        ft.ElevatedButton("REFRESH FOLDER", on_click=refresh_list, bgcolor="black", color="white"),
        ft.Divider(height=20),
        ft.Container(content=files_list, expand=True)
    )
    
    page.update()
    refresh_list() # Автоматический скан при запуске

if __name__ == "__main__":
    ft.app(target=main)
