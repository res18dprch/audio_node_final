import flet as ft
import os

def main(page: ft.Page):
    # 1. БАЗОВАЯ КОНФИГУРАЦИЯ (без теней и градиентов)
    page.bgcolor = "black"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    
    # Путь к документам (уже проверенный нами ранее)
    doc_path = os.path.join(os.path.expanduser('~'), 'Documents')
    
    # 2. ПРЕДВАРИТЕЛЬНАЯ ЗАГРУЗКА (чтобы не было "тьмы")
    audio1 = ft.Audio(src="", autoplay=False)
    page.overlay.append(audio1)
    
    status = ft.Text("SYSTEM: READY", color="#00ff41", size=14)
    files_list = ft.Column(scroll=ft.ScrollMode.HIDDEN)

    def play_click(e):
        try:
            audio1.src = os.path.join(doc_path, e.control.data)
            audio1.play()
            status.value = f"PLAYING: {e.control.data}"
            page.update()
        except Exception as ex:
            status.value = f"ERROR: {str(ex)[:20]}"
            page.update()

    def refresh(e=None):
        files_list.controls.clear()
        if not os.path.exists(doc_path):
            os.makedirs(doc_path)
        
        items = [f for f in os.listdir(doc_path) if f.lower().endswith(('.mp3', '.wav', '.m4a'))]
        
        for f in items:
            # Используем ListTile - это стандартный элемент iOS, он самый стабильный
            files_list.controls.append(
                ft.ListTile(
                    title=ft.Text(f, color="white", size=16),
                    on_click=play_click,
                    data=f,
                    bgcolor="#111111"
                )
            )
        
        status.value = f"FILES_FOUND: {len(items)}"
        page.update()

    # 3. УЛУЧШЕННЫЙ ИНТЕРФЕЙС
    page.add(
        ft.Text("NODE_PLAYER_PRO", size=24, color="#00ff41", weight="bold"),
        status,
        ft.Divider(color="#333333"),
        ft.ElevatedButton("SCAN STORAGE", on_click=refresh, color="white", bgcolor="#222222"),
        ft.Container(content=files_list, expand=True)
    )
    
    page.update()
    refresh()

if __name__ == "__main__":
    ft.app(target=main)
