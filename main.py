import flet as ft
import os

def main(page: ft.Page):
    page.bgcolor = "black"
    page.padding = 30
    
    doc_path = os.path.join(os.path.expanduser('~'), 'Documents')
    title = ft.Text(" > STORAGE_INITIALIZER", color="#00ff41", size=20)
    log = ft.Column()

    def force_create_folder(e=None):
        try:
            # 1. Создаем папку, если ее нет
            if not os.path.exists(doc_path):
                os.makedirs(doc_path)
            
            # 2. Создаем ПУСТОЙ файл-маяк. Именно он заставляет iOS показать папку в "Файлах"
            beacon_file = os.path.join(doc_path, "PUT_MUSIC_HERE.txt")
            with open(beacon_file, "w") as f:
                f.write("Place your mp3 files in this folder.")
            
            log.controls.append(ft.Text("!!! FOLDER_ACTIVATED !!!", color="#00ff41"))
            log.controls.append(ft.Text("Check 'Files' -> 'On My iPhone'", color="white"))
        except Exception as ex:
            log.controls.append(ft.Text(f"ERR: {str(ex)}", color="red"))
        page.update()

    btn = ft.GestureDetector(
        content=ft.Container(
            content=ft.Text(" [ ACTIVATE_FOLDER ] ", size=24, color="#00ff41"),
            padding=20, border=ft.border.all(1, "#00ff41")
        ),
        on_tap=force_create_folder
    )

    page.add(title, btn, log)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
