import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class Btns(GridLayout):
    def __init__(self, **kwargs):
        super(Btns, self).__init__(**kwargs)
        self.cols = 5
        btns = ["sin", "cos", "tan", "log", "+", "7", "8", "9", "sqr", "-", "4", "5",
                "6", "root", "X", "1", "2", "3", "cube", "/", ".", "0", "=", "del", "clr"]
        for i in btns:
            self.add_widget(Button(text=i))


class GL(GridLayout):
    def __init__(self, **kwargs):
        super(GL, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(TextInput(font_size=50, multiline=False,
                                  size_hint_y=.7, size_hint_x=1))
        self.add_widget(Btns())


class Calculator(App):
    def build(self):
        return(GL())


if __name__ == "__main__":
    Calculator().run()
