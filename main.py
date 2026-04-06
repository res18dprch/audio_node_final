import flet as ft
import os
import shutil
import asyncio

def main(page: ft.Page):
    page.bgcolor = "black"
    page.padding = 30
    
    # Тот самый путь из твоего скриншота
    doc_path = os.path.join(os.path.expanduser('~'), 'Documents')
    
    # Контейнеры для тяжелых модулей
    modules = {"audio": None, "picker": None}

    title = ft.Text(" > AUDIO_NODE_STABLE", color="#00ff41", size=20, weight="bold")
    status = ft.Text("SYSTEM_ACTIVE", color="#555555")
    files_view = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)

    async def play_track(e):
        track_name = e.control.data
        if modules["audio"] is None:
            status.value = "INIT_AUDIO..."
            page.update()
            modules["audio"] = ft.Audio(src="", autoplay=False)
            page.overlay.append(modules["audio"])
        
        modules["audio"].src = os.path.join(doc_path, track_name)
        status.value = f"PLAYING: {track_name}"
        page.update()
        await modules["audio"].play_async()

    async def on_result(e: ft.FilePickerResultEvent):
        if e.files:
            status.value = "COPYING_FILES..."
            page.update()
            for f in e.files:
                dest = os.path.join(doc_path, f.name)
                try:
                    shutil.copy(f.path, dest)
                except: pass
            status.value = "STATUS: SUCCESS"
            await refresh()

    async def open_picker(e):
        if modules["picker"] is None:
            status.value = "INIT_PICKER..."
            page.update()
            modules["picker"] = ft.FilePicker(on_result=on_result)
            page.overlay.append(modules["picker"])
            page.update()
        await modules["picker"].pick_files_async(allow_multiple=True)

    async def refresh(e=None):
        files_view.controls.clear()
        try:
            if not os.path.exists(doc_path): os.makedirs(doc_path)
            items = [f for f in os.listdir(doc_path) if f.lower().endswith((".mp3", ".wav", ".m4a"))]
            for f in items:
                files_view.controls.append(
                    ft.GestureDetector(
                        content=ft.Text(f" [ PLAY ] > {f}", color="white", size=16),
                        data=f,
                        on_tap=play_track
                    )
                )
            if not items: status.value = "STATUS: NO_FILES"
            else: status.value = f"FOUND: {len(items)} TRACKS"
        except: status.value = "STATUS: FS_ERROR"
        page.update()

    # Текстовые кнопки
    add_btn = ft.GestureDetector(
        content=ft.Text(" [ + ADD_TRACKS ] ", color="#00ff41", size=24, weight="bold"),
        on_tap=open_picker
    )
    
    refresh_btn = ft.GestureDetector(
        content=ft.Text(" [ R REFRESH_LIST ] ", color="#555555", size=16),
        on_tap=refresh
    )

    page.add(
        title, 
        status, 
        ft.Divider(color="#1a1a1a"), 
        add_btn,
        ft.Container(content=files_view, height=350, padding=10),
        refresh_btn
    )
    
    page.update()
    # Запускаем первичный скан асинхронно
    page.run_task(refresh)

if __name__ == "__main__":
    ft.app(target=main)
