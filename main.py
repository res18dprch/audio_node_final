import flet as ft
import os

def main(page: ft.Page):
    # Оставляем белый фон — он доказал свою стабильность
    page.bgcolor = "white"
    page.padding = 20
    page.title = "Audio Node Final"
    
    # Путь к песочнице (где лежит твой файл signal)
    doc_path = os.path.join(os.path.expanduser('~'), 'Documents')
    
    title = ft.Text("AUDIO_NODE_CORE", size=26, color="black", weight="bold")
    status = ft.Text("Status: Standby", color="blue")
    files_view = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO)

    # Инициализируем плеер без файла
    audio_player = ft.Audio(src="", autoplay=True)
    page.overlay.append(audio_player)

    def play_track(e):
        track_name = e.control.data
        try:
            # Указываем путь к файлу
            audio_player.src = os.path.join(doc_path, track_name)
            audio_player.play()
            status.value = f"Playing: {track_name}"
            status.color = "green"
        except Exception as ex:
            status.value = "Playback Error"
            status.color = "red"
        page.update()

    def scan_folder(e=None):
        files_view.controls.clear()
        try:
            # Читаем все файлы в папке (кроме системных)
            items = [f for f in os.listdir(doc_path) if not f.startswith('.')]
            
            if not items:
                status.value = "Folder is empty"
            else:
                status.value = f"Found {len(items)} objects"
                for f in items:
                    files_view.controls.append(
                        ft.Container(
                            content=ft.Row([
                                ft.Icon(ft.icons.MUSIC_NOTE, color="black"),
                                ft.Text(f, color="black", size=16, weight="w500", expand=True),
                                ft.IconButton(
                                    icon=ft.icons.PLAY_CIRCLE_FILL,
                                    icon_color="black",
                                    data=f,
                                    on_click=play_track
                                )
                            ]),
                            padding=10,
                            border=ft.border.all(1, "#eeeeee"),
                            border_radius=8,
                            bgcolor="#f9f9f9"
                        )
                    )
        except Exception as ex:
            status.value = f"Scan failed: {str(ex)[:15]}"
        page.update()

    # Сборка интерфейса
    page.add(
        title,
        status,
        ft.Divider(height=20, color="transparent"),
        ft.ElevatedButton(
            "REFRESH LIBRARY", 
            on_click=scan_folder, 
            bgcolor="black", 
            color="white",
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
        ),
        ft.Container(content=files_view, expand=True, margin=ft.margin.only(top=10))
    )
    
    page.update()
    # Автоматический скан при старте
    scan_folder()

if __name__ == "__main__":
    ft.app(target=main)
