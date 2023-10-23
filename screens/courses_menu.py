from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from appdir.config import TEXT_SIZE as text_size
from appdir.config import TITLE_SIZE as title_size


class CoursesMenu(BoxLayout):
    def __init__(self, on_back_click, on_course_click, **kwargs):
        super(CoursesMenu, self).__init__(orientation='vertical', spacing=10, padding=10, **kwargs)

        # Title
        title = Label(text='Courses Menu', font_size=title_size, size_hint=(1, 0.3), halign='center')
        self.add_widget(title)

        # ScrollView para desplazamiento vertical
        scroll_view = ScrollView(size_hint=(1, 0.8))
        self.add_widget(scroll_view)

        # GridLayout para organizar los cursos en una cuadrícula
        grid_layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))
        scroll_view.add_widget(grid_layout)

        # Añadir cursos con botones que abren las pantallas correspondientes
        for i in range(1, 9):
            course_button = Button(text=f'Course {i}', size_hint_y=None, height=140, font_size=text_size)
            course_button.bind(on_press=lambda btn, course_num=i: on_course_click(course_num))
            grid_layout.add_widget(course_button)

        # Ejemplo: Botón de regreso al menú principal
        btn_back = Button(text='Back to Main Menu', on_release=on_back_click, size_hint=(1, None), height=50, font_size=text_size)
        self.add_widget(btn_back)
