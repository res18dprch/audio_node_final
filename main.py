import flet as ft
import os

def main(page: ft.Page):
    page.bgcolor = "white"
    page.padding = 30
    
    # Путь к файлам
    doc_path = os.path.join(os.path.expanduser('~'), 'Documents')
    
    # Элементы интерфейса
    title = ft.Text("AUDIO_NODE: V19", size=28, color="black", weight="bold")
    status = ft.Text("STATUS: SYSTEM_READY", color="grey")
    files_column = ft.Column(spacing=10)

    # Функция для запуска звука (создаем плеер только в момент клика!)
    def play_file(e):
        try:
            # Очищаем старые оверлеи, чтобы не копились
            page.overlay.clear()
            audio = ft.Audio(src=os.path.join(doc_path, e.control.data), autoplay=True)
            page.overlay.append(audio)
            status.value = f"NOW PLAYING: {e.control.data}"
            status.color = "blue"
        except Exception as ex:
            status.value = "AUDIO_START_FAILED"
            status.color = "red"
        page.update()

    def scan_files(e=None):
        files_column.controls.clear()
        if not os.path.exists(doc_path):
            os.makedirs(doc_path)
            
        # Берем только mp3 и m4a
        files = [f for f in os.listdir(doc_path) if f.lower().endswith(('.mp3', '.m4a'))]
        
        if not files:
            status.value = "NO_FILES_FOUND. COPY TO APP FOLDER!"
        else:
            status.value = f"FOUND {len(files)} TRACKS"
            for f in files:
                files_column.controls.append(
                    ft.ElevatedButton(
                        text=f"Play: {f}",
                        data=f,
                        on_click=play_file,
                        style=ft.ButtonStyle(color="black", bgcolor="lightgrey")
                    )
                )
        page.update()

    # Сборка экрана
    page.add(
        title,
        status,
        ft.Divider(color="black"),
        ft.ElevatedButton("SCAN LIBRARY", on_click=scan_files, bgcolor="black", color="white"),
        ft.Container(content=files_column, margin=ft.margin.only(top=20))
    )
    
    page.update()
    # Сразу сканируем при входе
    scan_files()

if __name__ == "__main__":
    ft.app(target=main)
