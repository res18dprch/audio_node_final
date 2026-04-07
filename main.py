import flet as ft
import os

def main(page: ft.Page):
    page.bgcolor = "black"
    page.padding = 30
    page.theme_mode = ft.ThemeMode.DARK
    
    # Прямой путь к папке, которую мы видим на скрине
    doc_path = os.path.join(os.path.expanduser('~'), 'Documents')
    
    # Заголовок в стиле терминала
    title = ft.Text(" > AUDIO_NODE_CORE_v14", color="#00ff41", size=20, weight="bold")
    status = ft.Text("STATUS: FILES_DETECTED", color="#555555")
    
    files_column = ft.Column(scroll=ft.ScrollMode.AUTO, spacing=15)
    audio_player = ft.Audio(src="", autoplay=False)
    page.overlay.append(audio_player)

    def play_track(e):
        track_name = e.control.data
        audio_player.src = os.path.join(doc_path, track_name)
        audio_player.play()
        status.value = f"PLAYING: {track_name}"
        status.color = "#00ff41"
        page.update()

    def refresh_library(e=None):
        files_column.controls.clear()
        try:
            # Список файлов из папки на скрине
            items = [f for f in os.listdir(doc_path) if f.lower().endswith(('.mp3', '.m4a', '.wav'))]
            
            if not items:
                status.value = "STATUS: NO_AUDIO_FILES_FOUND"
            else:
                for f in items:
                    files_column.controls.append(
                        ft.GestureDetector(
                            content=ft.Container(
                                content=ft.Text(f" [ PLAY ] > {f}", color="white", size=16),
                                padding=10,
                                border=ft.border.all(1, "#333333"),
                                border_radius=5
                            ),
                            data=f,
                            on_tap=play_track
                        )
                    )
                status.value = f"STATUS: {len(items)} TRACKS_READY"
        except Exception as ex:
            status.value = f"FS_ERROR: {str(ex)[:20]}"
        page.update()

    # Кнопка обновления списка
    refresh_btn = ft.GestureDetector(
        content=ft.Text(" [ REFRESH_LIBRARY ] ", color="#00ff41", size=18, weight="bold"),
        on_tap=refresh_library
    )

    page.add(
        title,
        status,
        ft.Divider(height=20, color="#1a1a1a"),
        refresh_btn,
        ft.Container(content=files_column, margin=ft.margin.only(top=20), expand=True)
    )
    
    page.update()
    refresh_library()

if __name__ == "__main__":
    ft.app(target=main)
