from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from appdir.config import TEXT_SIZE as text_size
from appdir.config import TITLE_SIZE as title_size

class Course1Menu(BoxLayout):
    def __init__(self, on_back_click, on_easy_mode_click, on_intermediate_mode_click, on_expert_mode_click, **kwargs):
        super(Course1Menu, self).__init__(orientation='vertical', spacing=10, padding=10, **kwargs)

        # Title:
        title = Label(text='Course 1 Menu', font_size=title_size, size_hint=(1, 0.3), halign='center')
        self.add_widget(title)

        # Gamemode buttons:
        btn_easy = Button(text='Easy Mode', on_release=on_easy_mode_click, size_hint=(1, 0.1), font_size=text_size)
        btn_intermediate = Button(text='Intermediate Mode', on_release=on_intermediate_mode_click, size_hint=(1, 0.1), font_size=text_size)
        btn_expert = Button(text='Expert Mode', on_release=on_expert_mode_click, size_hint=(1, 0.1), font_size=text_size)

        self.add_widget(Label(size_hint=(1, 0.2)))

        self.add_widget(btn_easy)
        self.add_widget(btn_intermediate)
        self.add_widget(btn_expert)
        
        self.add_widget(Label(size_hint=(1, 0.2)))

        # Return button:
        btn_back = Button(text='Back to Courses', on_release=on_back_click, size_hint=(1, None), height=50, font_size=text_size)
        self.add_widget(btn_back)

    #def on_back_click(self, instance):
    #    print("Back to Courses button clicked")
    #    self.parent.switch_to('courses_menu')

    def on_easy_mode_click(self, instance):
        print("Easy Mode button clicked")

    def on_intermediate_mode_click(self, instance):
        print("Intermediate Mode button clicked")

    def on_expert_mode_click(self, instance):
        print("Expert Mode button clicked")
