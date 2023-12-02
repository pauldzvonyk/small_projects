from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import time
import os
import webbrowser
from link_sharer import Uploader

Builder.load_file("frontend.kv")


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.opacity = 0
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        # Make new directory if it doesn't exist
        os.makedirs("photos", exist_ok=True)
        # Get the current time in the specified format
        current_time = time.strftime("%Y_%m_%d-%H_%M_%S")
        # Set the file name based on the current time
        self.file_path = f"photos/{current_time}.png"
        # Export the camera image to a PNG file with the specified file name
        self.ids.camera.export_to_png(self.file_path)
        # Switch current screen to ImageScreen name (in kv file RootWidget)
        self.manager.current = 'image_screen'
        # Allows access to img id (in kv), and sets it to file_path
        self.manager.current_screen.ids.img.source = self.file_path
        # self.ids -> access to widget functionality inside the class
        # self.manager.current_screen.ids -> access to actual user screen


class ImageScreen(Screen):
    link_message = "Create a Link First"

    def create_link(self):
        """Accesses the photo filepath, uploads to dropbox, and
        inserts sharable link into Label Widget"""
        filepath = App.get_running_app().root.ids.camera_screen.file_path
        uploader = Uploader()
        file_path = filepath
        uploader.upload_file(file_path)
        self.url = uploader.share_file()
        self.ids.link.text = self.url

    def copy_link(self):
        """Copy link to Clipboard for pasting"""
        try:
            Clipboard.copy(self.url)
        except AttributeError:
            self.ids.link.text = self.link_message

    def open_link(self):
        """Open link in default browser"""
        try:
            webbrowser.open(self.url)
        except AttributeError:
            self.ids.link.text = self.link_message


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
