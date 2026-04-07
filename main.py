import flet as ft
import os

def main(page: ft.Page):
    # Явно задаем параметры страницы
    page.bgcolor = "white"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Путь к папке
    doc_path = os.path.join(os.path.expanduser('~'), 'Documents')

    # Простая надпись для проверки жизни
    info_text = ft.Text("AUDIO NODE V22", color="black", size=20)
    list_col = ft.Column()

    def play_action(e):
        try:
            page.overlay.clear()
            audio = ft.Audio(src=os.path.join(doc_path, e.control.data), autoplay=True)
            page.overlay.append(audio)
            info_text.value = f"Playing... {e.control.data[:15]}"
            page.update()
        except:
            pass

    def load_files(e):
        list_col.controls.clear()
        try:
            if not os.path.exists(doc_path):
                os.makedirs(doc_path)
            
            files = [f for f in os.listdir(doc_path) if not f.startswith('.')]
            if not files:
                info_text.value = "FOLDER IS EMPTY"
            else:
                info_text.value = f"FOUND: {len(files)}"
                for f in files:
                    list_col.controls.append(
                        ft.TextButton(text=f"Play: {f}", data=f, on_click=play_action)
                    )
        except Exception as ex:
            info_text.value = "SCAN ERROR"
        page.update()

    # Добавляем элементы по одному
    page.add(info_text)
    page.add(ft.ElevatedButton("SHOW FILES", on_click=load_files))
    page.add(list_col)
    
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
