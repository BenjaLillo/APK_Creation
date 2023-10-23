from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from appdir.screens.course_menu import Course1Menu
#from appdir.screens.course_menu import Course2Menu
from appdir.screens.game_screen import GameScreen
from appdir.screens.main_menu import MainMenu
from appdir.screens.courses_menu import CoursesMenu
from appdir.screens.stats_menu import StatsMenu

# Global variables:
global font_size

class MyApp(App):
    def build(self):        
        self.screen_manager = ScreenManager()
        self.main_menu_screen = Screen(name='main_menu')
        main_menu = MainMenu(on_courses_click=self.show_courses_menu, on_stats_click=self.show_stats_menu)
        self.main_menu_screen.add_widget(main_menu)
        self.screen_manager.add_widget(self.main_menu_screen)
        self.game_screen_screen = Screen(name='game_screen')  # Agrega una pantalla para GameScreen
        return self.screen_manager

    def show_main_menu(self, instance):
        self.screen_manager.switch_to(self.main_menu_screen)
        
    def show_courses_menu(self, instance):
        courses_menu_screen = Screen(name='courses_menu')
        courses_menu = CoursesMenu(on_back_click=self.show_main_menu, on_course_click=self.show_course_menu)
        courses_menu_screen.add_widget(courses_menu)
        self.screen_manager.add_widget(courses_menu_screen)
        self.screen_manager.switch_to(courses_menu_screen)

    def show_stats_menu(self, instance):
        stats_menu_screen = Screen(name='stats_menu')
        stats_menu = StatsMenu(on_back_click=self.show_main_menu)
        stats_menu_screen.add_widget(stats_menu)
        self.screen_manager.add_widget(stats_menu_screen)
        self.screen_manager.switch_to(stats_menu_screen)

    def show_course_menu(self, course_num):
        # Obtén el nombre de la clase de menú correspondiente
        menu_class_name = f'Course{course_num}Menu'

        # Usa globals() para obtener la clase del espacio de nombres global
        menu_class = globals().get(menu_class_name, None)

        if menu_class:
            # Crea una instancia de la clase de menú encontrada
            course_menu_screen = Screen(name=f'course{course_num}_menu')
            course_menu = menu_class(on_back_click=self.show_courses_menu, on_easy_mode_click=self.start_game, 
                                     on_intermediate_mode_click=self.start_game, on_expert_mode_click=self.start_game)
            course_menu_screen.add_widget(course_menu)
            self.screen_manager.add_widget(course_menu_screen)
            self.screen_manager.switch_to(course_menu_screen)
            
    def start_game(self, instance):
        current_question_index = 0
        game_screen = GameScreen(question_index=current_question_index, on_back_click=self.show_courses_menu)
        self.game_screen_screen.clear_widgets()  # Limpia los widgets de la pantalla game_screen_screen
        self.game_screen_screen.add_widget(game_screen)
        self.screen_manager.add_widget(self.game_screen_screen)
        self.screen_manager.switch_to(self.game_screen_screen)
        


if __name__ == '__main__':
    MyApp().run()
