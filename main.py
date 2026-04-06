import flet as ft
import os

def main(page: ft.Page):
    page.bgcolor = "black"
    page.vertical_alignment = "center"
    
    # Список стандартных путей iOS
    paths = {
        "Home": os.path.expanduser('~'),
        "Documents": os.path.join(os.path.expanduser('~'), 'Documents'),
        "Library": os.path.join(os.path.expanduser('~'), 'Library'),
        "Cwd": os.getcwd()
    }

    log = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)
    header = ft.Text(" > SYSTEM_PATH_DETECTOR", size=18, color="#00ff41")

    def run_check(e=None):
        log.controls.clear()
        for name, path in paths.items():
            exists = os.path.exists(path)
            # Пробуем создать тестовый файл, чтобы проверить права
            writable = "READ_ONLY"
            if exists:
                try:
                    test_file = os.path.join(path, "test.txt")
                    with open(test_file, "w") as f:
                        f.write("test")
                    os.remove(test_file)
                    writable = "WRITABLE (OK)"
                except:
                    writable = "LOCKED"
            
            log.controls.append(
                ft.Text(f"[{name}]: {path}\nSTATUS: {writable}", 
                        size=12, color="white" if exists else "red")
            )
        page.update()

    page.add(
        header,
        ft.Container(log, height=400, border=ft.border.all(1, "#333333"), padding=10),
        ft.ElevatedButton(" [ SCAN_SYSTEM ] ", on_click=run_check)
    )
    page.update()
    run_check()

if __name__ == "__main__":
    ft.app(target=main)
