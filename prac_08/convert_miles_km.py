
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertToMilesApp(App):

    def build(self):
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertToMilesApp().run()
