from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILE_TO_KM = 1.60934


class MilesConverterApp(App):
    result_km = StringProperty()
    """Main program - Kivy app to convert miles to kilometers."""
    def build(self):
        """Build Kivy GUI."""
        Window.size = (400, 200)
        self.title = "Miles to Kilometer Converter"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_calculate(self):
        """Convert miles into kilometer"""
        value = self.get_valid_input()
        self.result_km = str(value * MILE_TO_KM)

    def handle_change(self, change):
        """Handles Up and Down button, call calculation function"""
        value = self.get_valid_input() + change
        self.handle_calculate()
        self.root.ids.input_miles.text = str(value)

    def get_valid_input(self):
        """Filter literal inputs by setting the value as 0.0"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0


MilesConverterApp().run()
