import flet as ft
import os
import shutil

def main(page: ft.Page):
    page.bgcolor = "black"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    # Путь к папке, которую iOS обычно открывает для пользователя
    # Попробуем стандартную папку Documents
    doc_path = os.path.expanduser('~/Documents')
    
    header = ft.Text(" > AUDIO_NODE_v5", size=25, color="#00ff41", weight="bold")
    status = ft.Text("READY", color="#555555")
    files_list = ft.ListView(expand=1, spacing=10)

    audio_player = ft.Audio(src="", autoplay=False)
    page.overlay.append(audio_player)

    def play_file(e):
        file_name = e.control.data
        # Полный путь к файлу для плеера
        audio_player.src = os.path.join(doc_path, file_name)
        audio_player.play()
        status.value = f"PLAYING: {file_name}"
        page.update()

    def refresh(e=None):
        files_list.controls.clear()
        try:
            # Если папки нет - создаем (это может заставить iOS показать её)
            if not os.path.exists(doc_path):
                os.makedirs(doc_path)
            
            items = os.listdir(doc_path)
            found = False
            for f in items:
                if f.lower().endswith((".mp3", ".wav", ".m4a")):
                    files_list.controls.append(
                        ft.TextButton(
                            text=f" [ PLAY ] {f}",
                            data=f,
                            on_click=play_file,
                            style=ft.ButtonStyle(color="white")
                        )
                    )
                    found = True
            
            if not found:
                status.value = "EMPTY: COPY FILES TO APP FOLDER"
            else:
                status.value = f"FOUND {len(files_list.controls)} FILES"
                
        except Exception as ex:
            status.value = f"ERR: {str(ex)}"
        page.update()

    page.add(
        header,
        status,
        ft.Divider(color="#1a1a1a"),
        ft.Container(content=files_list, height=250),
        ft.ElevatedButton(" [ REFRESH_LIST ] ", on_click=refresh)
    )
    
    page.update()
    refresh()

if __name__ == "__main__":
    ft.app(target=main)
