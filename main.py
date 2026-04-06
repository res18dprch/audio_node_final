import flet as ft
import asyncio

async def main(page: ft.Page):
    page.title = "AUDIO_NODE_v2"
    page.bgcolor = "#050505"
    page.theme_mode = ft.ThemeMode.DARK
    
    # Ждем полсекунды, чтобы iOS прогрузила графический контекст
    await asyncio.sleep(0.5)

    status = ft.Text("STATUS: SYSTEM_READY", color="#555555", size=12)
    
    await page.add_async(
        ft.Text(" > DEVICE_NODE_v5.0", size=30, color="#00ff41", weight="bold"),
        status,
        ft.Divider(color="#1a1a1a"),
        ft.ElevatedButton(
            " [ SELECT_AUDIO_FILES ] ",
            on_click=lambda _: print("Click"), # Заглушка для теста графики
            style=ft.ButtonStyle(color="#00ff41", bgcolor="#111111")
        )
    )
    await page.update_async()

if __name__ == "__main__":
    ft.app(target=main)
