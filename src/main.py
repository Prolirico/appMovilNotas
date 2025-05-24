from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout

class TestApp(MDApp):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        button = MDRaisedButton(
            text="Hello, appMovilNotas!",
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        layout.add_widget(button)
        return layout

if __name__ == '__main__':
    TestApp().run()
