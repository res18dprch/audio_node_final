import flet as ft
import os

def main(page: ft.Page):
    # 1. ОТКЛЮЧАЕМ ВСЕ ЭФФЕКТЫ
    page.bgcolor = "black"
    page.theme_mode = ft.ThemeMode.DARK
    # Убираем анимации переходов, которые могут вешать старые iPhone
    page.window_prevent_close = True 
    
    doc_path = os.path.join(os.path.expanduser('~'), 'Documents')
    
    # Резервный плеер (создаем ПУСТЫМ)
    audio_ref = ft.Ref[ft.Audio]()

    def play_action(e):
        if not audio_ref.current:
            audio_ref.current = ft.Audio(src="", autoplay=False)
            page.overlay.append(audio_ref.current)
        
        audio_ref.current.src = os.path.join(doc_path, e.control.data)
        audio_ref.current.play()
        page.update()

    # Простая функция рендера списка
    def build_list():
        items = []
        try:
            if not os.path.exists(doc_path):
                os.makedirs(doc_path)
            
            raw_files = os.listdir(doc_path)
            # Отфильтровываем системный мусор и Inbox
            music_files = [f for f in raw_files if f.lower().endswith(('.mp3', '.wav'))]
            
            for f in music_files:
                items.append(
                    ft.TextButton(
                        text=f" > {f}",
                        data=f,
                        on_click=play_action,
                        style=ft.ButtonStyle(color="white")
                    )
                )
        except:
            items.append(ft.Text("FS_ERROR", color="red"))
        return items

    # ГЛАВНЫЙ ЭКРАН (Минимализм)
    main_container = ft.Column(
        controls=[
            ft.Text("STABLE_NODE_V11", color="#00ff41", size=18),
            ft.Divider(color="#1a1a1a"),
            ft.Column(controls=build_list(), scroll=ft.ScrollMode.AUTO)
        ]
    )

    # Добавляем всё ОДНИМ махом в конце
    page.add(main_container)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
