import flet as ft
import os
import time

def main(page: ft.Page):
    page.bgcolor = "black"
    page.padding = 30
    
    # Путь к песочнице
    doc_path = os.path.join(os.path.expanduser('~'), 'Documents')
    
    # Принудительная проверка папки СРАЗУ
    if not os.path.exists(doc_path):
        os.makedirs(doc_path)

    # Элементы интерфейса
    title = ft.Text(" > NODE_STABLE_v16", color="#00ff41", size=20, weight="bold")
    status = ft.Text("SYSTEM_BOOT_COMPLETE", color="#555555")
    
    # Контейнер для списка, который НИКОГДА не бывает совсем пустым
    files_view = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO)
    
    audio_player = ft.Audio(src="", autoplay=False)
    page.overlay.append(audio_player)

    def play_track(e):
        audio_player.src = os.path.join(doc_path, e.control.data)
        audio_player.play()
        status.value = f"PLAYING: {e.control.data}"
        page.update()

    def refresh(e=None):
        files_view.controls.clear()
        # Добавляем невидимый или мелкий элемент, чтобы Column не был пустым
        files_view.controls.append(ft.Text("--- LIBRARY_START ---", color="#1a1a1a", size=10))
        
        try:
            items = [f for f in os.listdir(doc_path) if f.lower().endswith(('.mp3', '.m4a', '.wav'))]
            if not items:
                status.value = "NO_FILES: ADD_VIA_FILES_APP"
            else:
                status.value = f"FILES_FOUND: {len(items)}"
                for f in items:
                    files_view.controls.append(
                        ft.GestureDetector(
                            content=ft.Container(
                                content=ft.Text(f" [ > ] {f}", color="white", size=16),
                                padding=12, bgcolor="#111111", border_radius=5
                            ),
                            data=f, on_tap=play_track
                        )
                    )
        except:
            status.value = "SCAN_ERROR"
        
        files_view.controls.append(ft.Text("--- LIBRARY_END ---", color="#1a1a1a", size=10))
        page.update()

    # Постоянная кнопка сканирования
    scan_btn = ft.GestureDetector(
        content=ft.Container(
            content=ft.Text(" [ RUN_SCAN_CMD ] ", color="#00ff41", size=18, weight="bold"),
            padding=15, border=ft.border.all(1, "#00ff41"), border_radius=5
        ),
        on_tap=refresh
    )

    # Собираем экран
    page.add(
        title,
        status,
        ft.Divider(height=20, color="#1a1a1a"),
        scan_btn,
        ft.Container(content=files_view, expand=True, margin=ft.margin.only(top=20))
    )
    
    page.update()
    # Пауза перед первым сканом, чтобы iOS "проснулась"
    time.sleep(0.3)
    refresh()

if __name__ == "__main__":
    ft.app(target=main)
