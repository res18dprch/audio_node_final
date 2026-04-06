import flet as ft
import os

def main(page: ft.Page):
    page.bgcolor = "black"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    header = ft.Text(" > AUDIO_NODE_v5", size=25, color="#00ff41", weight="bold")
    status = ft.Text("SCANNING_LOCAL_STORAGE...", color="#555555")
    
    # Список для файлов
    files_list = ft.ListView(expand=1, spacing=10, padding=20)

    def scan_files(e=None):
        files_list.controls.clear()
        # Сканируем текущую папку приложения
        path = os.getcwd() 
        try:
            found = False
            for f in os.listdir(path):
                if f.endswith((".mp3", ".wav", ".m4a")):
                    files_list.controls.append(
                        ft.Text(f" [ FILE ]: {f}", color="white", size=16)
                    )
                    found = True
            if not found:
                files_list.controls.append(ft.Text("NO_AUDIO_FOUND", color="#ff4141"))
        except Exception as ex:
            files_list.controls.append(ft.Text(f"ERROR: {str(ex)}", color="red"))
        
        status.value = f"STORAGE_OK | PATH: {path}"
        page.update()

    btn_scan = ft.ElevatedButton(
        " [ REFRESH_LIST ] ",
        on_click=scan_files,
        style=ft.ButtonStyle(color="#00ff41", bgcolor="#111111")
    )

    page.add(
        header,
        status,
        ft.Divider(color="#1a1a1a"),
        ft.Container(content=files_list, height=200),
        btn_scan
    )
    
    page.update()
    # Авто-сканирование при запуске
    scan_files()

if __name__ == "__main__":
    ft.app(target=main)
