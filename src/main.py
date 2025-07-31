import flet as ft
import flet_audio as fta


def main(page: ft.Page):
    page.adaptive = True
    audio1 = fta.Audio(
        src="https://luan.xyz/files/audio/ambient_c_motion.mp3", autoplay=True
    )
    body = ft.Column(
        controls=[
            ft.Text("This is an app with background audio."),
            ft.ElevatedButton("Stop playing", on_click=lambda _: audio1.pause()),
        ]
    )
    page.overlay.append(audio1)
    page.add(ft.SafeArea(body))


ft.app(main)
