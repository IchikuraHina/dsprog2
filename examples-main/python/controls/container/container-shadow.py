import flet as ft


def main(page: ft.Page):

    page.add(
        ft.Container(
            bgcolor=ft.colors.YELLOW,
            width=100,
            height=100,
            border_radius=50,
            shadow=[
                ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.colors.WHITE,
                    offset=ft.Offset(-5, -5),
                ),
                ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.colors.GREY_600,
                    offset=ft.Offset(5, 5),
                ),
            ],
        ),
        ft.Container(
            # bgcolor=ft.colors.WHITE,
            border_radius=10,
            width=100,
            height=100,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors.BLUE_GREY_300,
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
        ),
    )


ft.app(main)
