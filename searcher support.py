from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
class Mykivyapp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.button = Button(text='Izlash')
        self.label = Label(text='Natija: ')
        self.button.bind(on_press = self.update_label)

        layout.add_widget(self.button)
        layout.add_widget(self.label)
        return layout
    def update_label(self,instance):
        self.label.text = 'Siz bosdiz'

if __name__ = '__main__':
    Mykivyapp().run()
