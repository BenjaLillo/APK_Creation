from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp
from appdir.config import TEXT_SIZE as text_size
from appdir.config import TITLE_SIZE as title_size
import json


class GameScreen(BoxLayout):
    def __init__(self, question_index, on_back_click, **kwargs):
        super(GameScreen, self).__init__(orientation='vertical', spacing=10, padding=10, **kwargs)
        self.question_index = question_index
        self.on_back_click = on_back_click
        
        # JSON Loading
        file_path = 'appdir/screens/questions.json'
        with open(file_path, 'r') as file:
            questions_data = json.load(file)

        # Obtain question from index:
        current_question = questions_data[question_index]

        # Question text:
        title = Label(text=current_question['question'], font_size=text_size, size_hint=(1, 0.2), halign='center')
        self.add_widget(title)

        # Question image:
        quiz_image = Image(source=current_question['image'], size_hint=(1, 0.4))
        self.add_widget(quiz_image)

        # Alternative buttons:
        grid_layout = GridLayout(cols=2, spacing=10, size_hint=(1, 0.3))
        for alternative_text in current_question['alternatives']:
            btn_alternative = Button(text=alternative_text, on_release=self.on_alternative_click, size_hint_y=None, height=50, font_size=text_size)
            grid_layout.add_widget(btn_alternative)

        self.add_widget(grid_layout)

    def on_alternative_click(self, instance):
        # Lógica para manejar la selección de alternativa
        print(f"Alternative clicked: {instance.text}")

        # Ejemplo de lógica condicional
        if 1 == 1:
            print("Respuesta correcta. Cargando nueva instancia de GameScreen.")

            # Incrementa el índice de la pregunta
            self.question_index += 1

            # Crea una nueva instancia de GameScreen con el nuevo índice
            new_game_screen = GameScreen(question_index=self.question_index, on_back_click=self.on_back_click)

            # Envuelve la instancia de GameScreen en un objeto Screen
            new_game_screen_screen = Screen(name=f'game_screen_{self.question_index}')
            new_game_screen_screen.add_widget(new_game_screen)

            # Accede al ScreenManager y reemplaza la instancia actual con la nueva
            self.parent.parent.switch_to(new_game_screen_screen)