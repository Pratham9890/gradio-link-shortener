import gradio as gr
from modules import shared, script_callbacks


def on_ui_settings():
    SECTION = ("gls", "Gradio Link Shortener")

    shared.opts.add_option(
        "gls_enabled",
        shared.OptionInfo(
            True,
            "Enable Gradio link shortener",
            section=SECTION,
        )
    )

    shared.opts.add_option(
        "gls_provider",
        shared.OptionInfo(
            "is.gd",
            "Shortener service",
            gr.Dropdown,
            lambda: {
                "choices": [
                    "is.gd",
                    "tinyurl",
                    "shrtco.de",
                    "clck.ru",
                ]
            },
            section=SECTION,
        )
    )


script_callbacks.on_ui_settings(on_ui_settings)
