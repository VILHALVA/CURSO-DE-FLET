import flet as ft

def main(page: ft.Page):
    page.add(ft.Text("Body!"))
    page.appbar = ft.AppBar(
    leading=ft.Icon(ft.icons.PALETTE),
    leading_width=40,
    title=ft.Text("AppBar Example"),
    center_title=False,
    bgcolor=ft.colors.SURFACE_VARIANT,
    actions=[
        ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
        ft.IconButton(ft.icons.FILTER_3)
    ],
)
    page.update()
    
ft.app(target=main)