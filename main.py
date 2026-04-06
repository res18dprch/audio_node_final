import flet as ft
import os
import shutil

def main(page: ft.Page):
    page.bgcolor = "black"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    # Тот самый подтвержденный путь из скриншота
    doc_path = os.path.join(os.path.expanduser('~'), 'Documents')
    
    header = ft.Text(" > NODE_PLAYER_v7", size=22, color="#00ff41", weight="bold")
    status = ft.Text("READY", color="#555555")
    files_view = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)
    
    audio_player = ft.Audio(src="", autoplay=False)
    page.overlay.append(audio_player)

    def play_file(e):
        audio_player.src = os.path.join(doc_path, e.control.data)
        audio_player.play()
        status.value = f"PLAYING: {e.control.data}"
        page.update()

    def on_file_result(e: ft.FilePickerResultEvent):
        if e.files:
            for f in e.files:
                # Копируем выбранный файл в нашу рабочую папку Documents
                dest = os.path.join(doc_path, f.name)
                shutil.copy(f.path, dest)
            status.value = "FILES_IMPORTED"
            refresh_list()
        page.update()

    picker = ft.FilePicker(on_result=on_file_result)
    page.overlay.append(picker)

    def refresh_list(e=None):
        files_view.controls.clear()
        try:
            items = [f for f in os.listdir(doc_path) if f.lower().endswith((".mp3", ".wav"))]
            for f in items:
                files_view.controls.append(
                    ft.TextButton(text=f" [ PLAY ] {f}", data=f, on_click=play_file, style=ft.ButtonStyle(color="white"))
                )
            status.value = f"FILES: {len(items)}" if items else "NO_AUDIO_FOUND"
        except Exception as ex:
            status.value = f"ERR: {str(ex)}"
        page.update()

    page.add(
        header,
        status,
        ft.Container(content=files_view, height=250, border=ft.border.all(1, "#1a1a1a")),
        ft.Row([
            ft.ElevatedButton(" [ + ADD FILES ] ", on_click=lambda _: picker.pick_files(allow_multiple=True)),
            ft.ElevatedButton(" [ REFRESH ] ", on_click=refresh_list)
        ], alignment="center")
    )
    
    page.update()
    refresh_list()

if __name__ == "__main__":
    ft.app(target=main)
