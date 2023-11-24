import wikipedia
import json
from urllib import request
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('frontend.kv')


class ScreenOne(Screen):
    def search_image(self):
        # Get user query from TextInput in kivy GUI
        query = self.manager.current_screen.ids.user_query.text
        # Get list of Wikipedia page and first image URL
        # Get page information
        search_url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=pageimages&piprop=original" \
                     f"&titles={query}"
        response = request.urlopen(search_url)
        data = json.loads(response.read().decode('utf-8'))

        page_id = next(iter(data['query']['pages']))
        page_info = data['query']['pages'][page_id]

        # Check if original image exists
        if 'original' in page_info:
            original_image_url = page_info['original']['source']
            print(f"Full-size Image URL for {query}: {original_image_url}")

            # Download image to local files
            image_path = f"images/{query}.jpg"
            request.urlretrieve(original_image_url, image_path)

            # Set image in Image widget
            self.manager.current_screen.ids.img.source = image_path
        else:
            print(f"Original image not found for {query}.")


# Screen manager is usually called Root Widget by developers
class RootWidget(ScreenManager):
    pass


# Create a MainApp class and instantiate RootWidget(ScreenManager)
class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
