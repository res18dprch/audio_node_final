import flet as ft
import os
import shutil

def main(page: ft.Page):
    page.bgcolor = "black"
    page.padding = 30
    
    # Подтвержденный путь
    doc_path = os.path.join(os.path.expanduser('~'), 'Documents')
    
    # Хранилище объектов
    state = {"audio": None}

    title = ft.Text(" > AUDIO_NODE_STABLE", color="#00ff41", size=20, weight="bold")
    status = ft.Text("SYSTEM_ACTIVE", color="#555555")
    files_view = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)

    def play_track(e):
        if state["audio"] is None:
            state["audio"] = ft.Audio(src="", autoplay=False)
            page.overlay.append(state["audio"])
        
        track_path = os.path.join(doc_path, e.control.data)
        state["audio"].src = track_path
        state["audio"].play()
        status.value = f"PLAYING: {e.control.data}"
        page.update()

    def on_result(e: ft.FilePickerResultEvent):
        if e.files:
            for f in e.files:
                dest = os.path.join(doc_path, f.name)
                shutil.copy(f.path, dest)
            status.value = "STATUS: IMPORT_COMPLETE"
            refresh()

    picker = ft.FilePicker(on_result=on_result)
    page.overlay.append(picker)

    def refresh(e=None):
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
        except: status.value = "STATUS: FS_ERROR"
        page.update()

    # Кнопки в текстовом стиле
    add_btn = ft.GestureDetector(
        content=ft.Text(" [ + ADD_TRACKS ] ", color="#00ff41", size=20, weight="bold"),
        on_tap=lambda _: picker.pick_files(allow_multiple=True)
    )
    
    refresh_btn = ft.GestureDetector(
        content=ft.Text(" [ R REFRESH ] ", color="white", size=16),
        on_tap=refresh
    )

    page.add(
        title, 
        status, 
        ft.Divider(color="#1a1a1a"), 
        add_btn,
        ft.Container(content=files_view, height=300, padding=10),
        refresh_btn
    )
    
    page.update()
    refresh()

if __name__ == "__main__":
    ft.app(target=main)
