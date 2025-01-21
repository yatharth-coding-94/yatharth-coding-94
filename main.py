from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import os

class GameBoosterApp(App):
    def boost_performance(self, instance):
        # Example to boost performance (dummy implementation)
        self.label.text = "Boosting performance...\nClearing memory and closing background apps!"
    
    def show_installed_games(self, instance):
        # Dummy game list
        games = ["Game 1", "Game 2", "Game 3"]
        self.label.text = "Installed Games:\n" + "\n".join(games)

    def build(self):
        layout = BoxLayout(orientation="vertical")
        
        self.label = Label(text="Welcome to Game Booster!", font_size="20sp")
        layout.add_widget(self.label)
        
        boost_button = Button(text="Boost Performance", size_hint=(1, 0.2))
        boost_button.bind(on_press=self.boost_performance)
        layout.add_widget(boost_button)
        
        games_button = Button(text="Show Installed Games", size_hint=(1, 0.2))
        games_button.bind(on_press=self.show_installed_games)
        layout.add_widget(games_button)
        
        return layout

if __name__ == "__main__":
    GameBoosterApp().run()
