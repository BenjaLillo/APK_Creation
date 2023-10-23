from tkinter.tix import TEXT
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from appdir.config import TEXT_SIZE as text_size
from appdir.config import TITLE_SIZE as title_size

class MainMenu(BoxLayout):
    def __init__(self, on_courses_click, on_stats_click, **kwargs):
        super(MainMenu, self).__init__(orientation='vertical', spacing=10, padding=10, **kwargs)

        # Texto "QLearn"
        title = Label(text='QLearn', font_size=title_size, size_hint=(1, 0.5))
        self.add_widget(title)

        # Botón "Courses"
        btn_courses = Button(text='Courses', on_release=on_courses_click, size_hint=(1, 0.2), font_size=text_size)
        self.add_widget(btn_courses)

        # Botón "Stats"
        btn_stats = Button(text='Stats', on_release=on_stats_click, size_hint=(1, 0.2), font_size=text_size)
        self.add_widget(btn_stats)
