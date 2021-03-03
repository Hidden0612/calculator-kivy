from kivy.app import App
from kivy.uix.gridlayout import GridLayout

#================#

class MyGridLayout(GridLayout):
    def calculate(self, cal):
        if cal:
            try:
                self.display.text = str(eval(cal))
            except Exception:
                self.display.text = "Error"

#================#

class CalculatorApp(App):
    def build(self):
        return MyGridLayout()

#================#

if __name__ == "__main__":
    CalculatorApp().run()