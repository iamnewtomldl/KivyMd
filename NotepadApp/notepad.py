from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDIconButton
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (400, 660)


class Set_Password(Screen):
    pass


class Enter(Screen):
    pass


class Notes(Screen):
    def on_kv_post(self, base_widget):
        caller = self.ids.Dots
        self.dropdown = MDDropdownMenu(caller=caller, width_mult=3)
        self.dropdown.items.append(
            {"viewclass": "MDMenuItem", "text": "Theme"})
        self.dropdown.items.append(
            {"viewclass": "MDMenuItem", "text": "Sort by"})
        self.dropdown.bind(on_release=Notepad.theme_cls.primary_dark)


class New_Note(Screen):
    def on_kv_post(self, base_widget):
        caller = self.ids.Note_Dots
        self.dropdown = MDDropdownMenu(caller=caller, width_mult=3)
        self.dropdown.items.append(
            {"viewclass": "MDMenuItem", "text": "Font"})
        self.dropdown.items.append(
            {"viewclass": "MDMenuItem", "text": "Send", 'icon': "send"})
        self.dropdown.items.append(
            {"viewclass": "MDMenuItem", "text": "Delete"})


class Manage_Window(ScreenManager):
    pass


class Notepad(MDApp):

    def build(self):
        # Automaticly load kv file so no need for anything more
        pass


Notepad().run()
