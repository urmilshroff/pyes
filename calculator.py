import kivy
kivy.require("1.10.0") #not important

from kivy.app import App #classes
from kivy.uix.gridlayout import GridLayout

class CalcGridLayout(GridLayout):
    def calculate(self,args):
        if args:
            try:
                self.input.text=str(eval(args))
            except Exception:
                self.input.text="Error!"
                
    def clear(self,args):
        if args:
            self.input.text=("")                
    
class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()
        
calcApp=CalculatorApp()
calcApp.run()