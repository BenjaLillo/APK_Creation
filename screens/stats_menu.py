from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.slider import Slider
from appdir.config import TEXT_SIZE as text_size
from appdir.config import TITLE_SIZE as title_size

class StatsMenu(BoxLayout):
    def __init__(self, on_back_click, **kwargs):
        super(StatsMenu, self).__init__(orientation='vertical', spacing=10, padding=10, **kwargs)

        # Title:
        title = Label(text='Stats Menu', font_size=title_size, size_hint=(1, 0.3), halign='center')
        self.add_widget(title)

        # Contenedor para las estadísticas
        stats_container = ScrollView(size_hint=(1, 0.8))
        self.add_widget(stats_container)

        # Contenido del ScrollView
        stats_layout = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None)
        stats_layout.bind(minimum_height=stats_layout.setter('height'))
        stats_container.add_widget(stats_layout)

        # Añadir las 80 estadísticas
        stats_layout.add_widget(Label(text="Stat1: data1", size_hint_y=None, height=40))
        stats_layout.add_widget(Label(text="Stat2: data2", size_hint_y=None, height=40))
        # ... Repite el proceso para todas las estadísticas ...

        # Ejemplo: Botón de regreso al menú principal
        btn_back = Button(text='Back to Main Menu', on_release=on_back_click, size_hint=(1, 0.1), font_size=text_size)
        self.add_widget(btn_back)
