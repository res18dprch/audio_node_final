import flet as ft
import os

def main(page: ft.Page):
    page.bgcolor = "black"
    page.padding = 30
    
    # Твой путь, где точно есть права
    doc_path = os.path.join(os.path.expanduser('~'), 'Documents')
    
    # Заголовок
    title = ft.Text(" > SYSTEM_NODE_V12", color="#00ff41", size=20, weight="bold")
    log = ft.Text("WAITING_FOR_SCAN", color="#555555")
    files_column = ft.Column(scroll=ft.ScrollMode.AUTO)

    def play_track(e):
        # Создаем плеер ТОЛЬКО тут, чтобы не вешать приложение при старте
        track_path = os.path.join(doc_path, e.control.data)
        try:
            # Если плеер уже есть в оверлее, удаляем старый (для чистоты)
            page.overlay.clear() 
            audio = ft.Audio(src=track_path, autoplay=True)
            page.overlay.append(audio)
            log.value = f"PLAYING: {e.control.data}"
        except Exception as ex:
            log.value = "AUDIO_ERROR"
        page.update()

    def scan_storage(e=None):
        files_column.controls.clear()
        try:
            if not os.path.exists(doc_path):
                os.makedirs(doc_path)
            
            # Читаем всё, что ты закинул в библиотеку
            items = [f for f in os.listdir(doc_path) if f.lower().endswith(('.mp3', '.wav', '.m4a'))]
            
            if not items:
                log.value = "STORAGE_EMPTY (ADD VIA KMP/FILES)"
            else:
                log.value = f"FOUND: {len(items)} TRACKS"
                for f in items:
                    files_column.controls.append(
                        ft.GestureDetector(
                            content=ft.Text(f" [ > ] {f}", color="white", size=18),
                            data=f,
                            on_tap=play_track
                        )
                    )
        except:
            log.value = "SCAN_FAILED"
        page.update()

    # Текстовая кнопка-триггер
    scan_btn = ft.GestureDetector(
        content=ft.Container(
            content=ft.Text(" [ RUN_SCAN ] ", color="#00ff41", size=24),
            padding=20,
            border=ft.border.all(1, "#00ff41")
        ),
        on_tap=scan_storage
    )

    page.add(title, log, ft.Divider(height=20), scan_btn, files_column)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
