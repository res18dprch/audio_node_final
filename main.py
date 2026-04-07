import flet as ft

def main(page: ft.Page):
    page.bgcolor = "black"
    # ЭТОТ ТЕКСТ ДОЛЖЕН БЫТЬ ВИДЕН СРАЗУ
    page.add(
        ft.Container(
            content=ft.Text("CORE_TEST_v17: ONLINE", color="#00ff41", size=30),
            alignment=ft.alignment.center,
            expand=True
        )
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
