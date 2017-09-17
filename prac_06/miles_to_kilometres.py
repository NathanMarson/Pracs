from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class MilesToKilometres(App):
    """ named it to the name of the file """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometres.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = value * 1.609344
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, value):
        result = int(self.get_correct_number() + value)
        self.root.ids.input_number.text = str(result)

    def get_correct_number(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


MilesToKilometres().run()
