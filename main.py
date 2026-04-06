import flet as ft
import os

def main(page: ft.Page):
    # Устанавливаем черный фон принудительно, чтобы уйти от белого
    page.bgcolor = "black"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Элементы интерфейса
    header = ft.Text(" > NODE_FINAL_TEST", size=25, color="#00ff41", weight="bold")
    status = ft.Text("READY_FOR_FILES", color="#555555")
    
    # Список файлов (пока пустой)
    files_list = ft.ListView(expand=1, spacing=5)

    def refresh_list(e):
        files_list.controls.clear()
        try:
            # Сканируем только текущую директорию (самый безопасный путь)
            curr_dir = os.getcwd()
            files = os.listdir(curr_dir)
            for f in files:
                if f.endswith((".mp3", ".wav", ".ipa", ".py")):
                    files_list.controls.append(ft.Text(f" [F] {f}", color="white", size=14))
            
            status.value = f"PATH: {curr_dir}"
            status.color = "blue"
        except Exception as ex:
            status.value = f"ERROR: {str(ex)}"
            status.color = "red"
        page.update()

    btn = ft.ElevatedButton(
        " [ REFRESH_FILES ] ",
        on_click=refresh_list,
        style=ft.ButtonStyle(color="#00ff41", bgcolor="#111111")
    )

    # Добавляем все элементы
    page.add(
        header,
        status,
        ft.Divider(height=20, color="#1a1a1a"),
        ft.Container(content=files_list, height=150),
        btn
    )
    
    # Финальное обновление
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
