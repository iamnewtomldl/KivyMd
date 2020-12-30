import kivy
import time
import random
from kivymd.app import MDApp
from kivy.lang import Builder
from PIL import ImageTk, Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

computer = ['rock', 'paper', 'scissor']


def result(user):
    player = user
    comp = random.choice(computer)
    win = "You win !"
    draw = "It's a draw !"
    lost = "You Lost !"

    if (player == 'rock'):
        if (comp == 'rock'):
            return [comp, draw]
        if (comp == 'paper'):
            return [comp, lost]
        if (comp == 'scissor'):
            return [comp, win]
    if (player == 'paper'):
        if (comp == 'rock'):
            return [comp, win]
        if (comp == 'paper'):
            return [comp, draw]
        if (comp == 'scissor'):
            return [comp, lost]
    if (player == 'scissor'):
        if (comp == 'rock'):
            return [comp, lost]
        if (comp == 'paper'):
            return [comp, win]
        if (comp == 'scissor'):
            return [comp, draw]


class StartWindow(Screen):
    pass


class PlayingWindow(Screen):
    pass


class ManageScreen(ScreenManager):
    pass


class RPS(MDApp):
    def build(self):
        return Builder.load_file('design.kv')

    def show_pop(self, user):

        res = ""
        com_label, res = result(user)
        layout = GridLayout(cols=1)
        label1 = Label(text="You Chose : "+user, font_size=20)
        label2 = Label(text="Computer Chose : "+com_label, font_size=20)
        label3 = Label(text=res, font_size=35)
        layout.add_widget(label1)
        layout.add_widget(label2)
        layout.add_widget(label3)
        popup = Popup(title='', content=layout,
                      size_hint=(None, None), size=(270, 270))
        time.sleep(1)
        popup.open()


if __name__ == "__main__":
    RPS().run()
