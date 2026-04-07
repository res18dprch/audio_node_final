import flet as ft
import os
import time

def main(page: ft.Page):
    page.bgcolor = "black"
    page.padding = 30
    
    # Путь к документам
    doc_path = os.path.join(os.path.expanduser('~'), 'Documents')
    
    # 1. СТРАХОВКА: Проверяем и создаем папку ДО отрисовки интерфейса
    if not os.path.exists(doc_path):
        try:
            os.makedirs(doc_path)
            # Небольшая пауза, чтобы iOS успела обновить файловую таблицу
            time.sleep(0.5) 
        except:
            pass

    title = ft.Text(" > NODE_SYSTEM_v15", color="#00ff41", size=20, weight="bold")
    status = ft.Text("STATUS: INITIALIZED", color="#555555")
    files_column = ft.Column(scroll=ft.ScrollMode.AUTO, spacing=15)
    
    # Плеер создаем, но не крепим к нему файл сразу
    audio_player = ft.Audio(src="", autoplay=False)
    page.overlay.append(audio_player)

    def play_track(e):
        track_name = e.control.data
        full_path = os.path.join(doc_path, track_name)
        if os.path.exists(full_path):
            audio_player.src = full_path
            audio_player.play()
            status.value = f"PLAYING: {track_name}"
            status.color = "#00ff41"
        else:
            status.value = "ERROR: FILE_NOT_FOUND"
            status.color = "red"
        page.update()

    def refresh_library(e=None):
        files_column.controls.clear()
        try:
            # Сканируем папку, которая должна была появиться в "Файлах"
            if os.path.exists(doc_path):
                items = [f for f in os.listdir(doc_path) if f.lower().endswith(('.mp3', '.m4a', '.wav'))]
                if not items:
                    status.value = "STATUS: EMPTY_LIBRARY"
                else:
                    status.value = f"STATUS: {len(items)} TRACKS_LOADED"
                    for f in items:
                        files_column.controls.append(
                            ft.GestureDetector(
                                content=ft.Container(
                                    content=ft.Text(f" [ PLAY ] > {f}", color="white", size=16),
                                    padding=12,
                                    border=ft.border.all(1, "#222222"),
                                    border_radius=8
                                ),
                                data=f,
                                on_tap=play_track
                            )
                        )
            else:
                status.value = "STATUS: PATH_MISSING"
        except:
            status.value = "STATUS: SCAN_ERROR"
        page.update()

    # Кнопка ручного обновления
    refresh_btn = ft.GestureDetector(
        content=ft.Container(
            content=ft.Text(" [ REFRESH_FILES ] ", color="#00ff41", weight="bold"),
            padding=15,
            border=ft.border.all(1, "#00ff41"),
            border_radius=5
        ),
        on_tap=refresh_library
    )

    page.add(
        title,
        status,
        ft.Divider(height=25, color="#1a1a1a"),
        refresh_btn,
        ft.Container(content=files_column, expand=True, margin=ft.margin.only(top=15))
    )
    
    page.update()
    # Авто-скан при запуске
    refresh_library()

if __name__ == "__main__":
    ft.app(target=main)
