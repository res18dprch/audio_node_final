import flet as ft
import asyncio

async def main(page: ft.Page):
    # Настройки страницы для предотвращения конфликтов графики
    page.title = "NODE_v5"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "black"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # ПРИНУДИТЕЛЬНАЯ ПАУЗА: Даем iPhone 11 время проснуться
    await asyncio.sleep(3.0)

    # Самый простой текстовый элемент для проверки отрисовки
    test_text = ft.Text(
        value=" > SYSTEM_LOADED_OK",
        size=30,
        color="#00ff41",
        weight=ft.FontWeight.BOLD,
        font_family="monospace"
    )

    # Добавляем элемент и принудительно обновляем страницу
    await page.add_async(test_text)
    await page.update_async()

if __name__ == "__main__":
    # Запуск в режиме мобильного приложения
    ft.app(target=main)
