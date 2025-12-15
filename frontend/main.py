from nicegui import ui
from frontend.pages import register_page

def start_ui(app):
    ui.run_with(app, dark=True)