import flet as ft
import os

def main(page: ft.Page):
    page.bgcolor = "white"
    doc_path = os.path.join(os.path.expanduser('~'), 'Documents')
    
    txt = ft.Text("READY TO ACTIVATE", color="black", size=20)

    def activate(e):
        try:
            if not os.path.exists(doc_path):
                os.makedirs(doc_path)
            
            # Создаем файл-пустышку
            with open(os.path.join(doc_path, "signal.txt"), "w") as f:
                f.write("active")
            
            txt.value = "DONE! RESTART 'FILES' APP"
            txt.color = "green"
        except Exception as ex:
            txt.value = f"ERROR: {str(ex)}"
            txt.color = "red"
        page.update()

    page.add(
        ft.Column([
            txt,
            ft.ElevatedButton("FORCE CREATE FOLDER", on_click=activate)
        ], alignment="center", expand=True)
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
