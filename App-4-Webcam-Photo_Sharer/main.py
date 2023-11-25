from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file("frontend.kv")


class CameraScreen(Screen):  # (requirement from kivy)
    pass

    def start(self):
        pass

    def stop(self):
        pass

    def capture(self):
        pass


class ImageScreen(Screen):  # (requirement from kivy)
    pass



class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
