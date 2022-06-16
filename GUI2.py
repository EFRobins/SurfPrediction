from kivy import Config
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from Graphs import plot
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivymd.theming import ThemeManager
from kivymd.uix.label import MDLabel
import _sqlite3
from Accuracy import Acc
from WeatherMap import update_app

Config.set('graphics', 'fullscreen', '1')
table = ''
conn = _sqlite3.connect('Predictions.db')
c = conn.cursor()
models = ['Gradient Descent', 'Multivariate', 'By Hand']


class Homepage(Screen):
    def __init__(self, **kw):
        super(Homepage, self).__init__(**kw)
        legend = [["Dark Blue- 0-2 ft", 0.6], ['Medium Dark Blue 2-4 ft', 0.5], ['Light Blue- 4-6 ft', 0.4],
                  ['Lighter Colours- 6+ ft', 0.3]]
        for i in legend:
            self.add_widget(MDLabel(text=i[0], pos_hint={'x': 0.7, 'y': i[1]}, size_hint=(0.1, 0.3)))


class Model(Screen):
    layout = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.Models = ['Gradient Descent', 'Multivariate', 'By Hand']

    def on_enter(self, *args):
        Clock.schedule_once(self.fill_grid)

    def fill_grid(self, _):
        plot()

        self.layout.add_widget(MDLabel(text='Model'))
        self.layout.add_widget(MDLabel(text='Accuracy of Model/ % error'))

        for i in range(len(Acc())):
            self.layout.add_widget(MDLabel(text=self.Models[i - 1]))
            self.layout.add_widget(MDLabel(text=str(Acc()[i - 1])))


class AlAsh(Screen):
    def __init__(self, **kwargs):
        super(AlAsh, self).__init__(**kwargs)
        c.execute('SELECT * FROM PredictionsA')


class Masirah(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        c.execute('SELECT * FROM PredictionsM')


class Table(GridLayout):
    def create_table(self):
        for i in self.records:
            for k in i:
                self.add_widget(MDLabel(text=str(k)))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.records = c.fetchall()
        top_row = ["Date/Time", "Magic Seaweed Prediction", "Gradient Descent", "By Hand",
                   "SciKit Multivariate"]
        for i in range(len(top_row)):
            self.add_widget(MDLabel(text=top_row[i], font_style='H6', pos=(Window.width, Window.height)))
        for i in range(0, 5):
            self.add_widget(MDLabel(text=''))
        self.create_table()


class MainApp(App):
    def build(self):
        self.title = "My Surfing App pls like and subscribe"
        update_app()

    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Blue'


MainApp().run()
