import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import  Button


class Main(App):
    def build(self):
        return layout()
    


class layout(GridLayout):
    def __init__(self, **kwargs):
        super(layout,self).__init__(**kwargs)
        self.cols=1
        self.rows=10
        self.buffer= 0 
        self.result= 0
        self.op_buffer=''

        self.screen=Label(text="WELCOME",font_size=40)
        self.add_widget(self.screen)

        self.numinput= GridLayout()
        self.numinput.cols=4

        #buttons
        self.numinput.add_widget(Button(text="1" ,font_size=40,on_press=self.pressed))
        self.numinput.add_widget(Button(text="2" ,font_size=40,on_press=self.pressed))
        self.numinput.add_widget(Button(text="3" ,font_size=40,on_press=self.pressed))
        self.numinput.add_widget(Button(text="/" ,font_size=40,on_press=self.pressed))
        self.numinput.add_widget(Button(text="4" ,font_size=40,on_press=self.pressed))
        self.numinput.add_widget(Button(text="5" ,font_size=40,on_press=self.pressed))
        self.numinput.add_widget(Button(text="6" ,font_size=40,on_press=self.pressed))
        self.numinput.add_widget(Button(text="*" ,font_size=40,on_press=self.pressed))
        self.numinput.add_widget(Button(text="7" ,font_size=40,on_press=self.pressed))
        self.numinput.add_widget(Button(text="8" ,font_size=40,on_press=self.pressed))
        self.numinput.add_widget(Button(text="9" ,font_size=40,on_press=self.pressed))
        self.numinput.add_widget(Button(text="-" ,font_size=40,on_press=self.pressed))
        self.numinput.add_widget(Button(text="=" ,font_size=40,on_press=self.pressed))
        self.numinput.add_widget(Button(text="0" ,font_size=40,on_press=self.pressed))
        self.numinput.add_widget(Button(text="+" ,font_size=40,on_press=self.pressed))
        self.numinput.add_widget(Button(text="c" ,font_size=40,on_press=self.pressed))
        self.add_widget(self.numinput)
    def pressed(self,instance):
        
        if(instance.text.isnumeric()):
            num =float(instance.text) 
            self.result=self.result*10+num
        elif(instance.text=="="):
             match self.op_buffer:
                 case "+": 
                    self.result =self.buffer+self.result
                 case "-":
                    self.result =self.buffer-self.result
                 case "/": 
                    self.result =self.buffer/self.result
                 case "*": 
                    self.result =self.buffer*self.result
             self.buffer=0           
                 

        elif(instance.text=="c"):
            self.result=0
            self.buffer=0
            self.op_buffer=''      
        else:
            self.buffer=self.result
            self.result=0
            self.op_buffer=instance.text


         

        self.screen.text=str(self.result )+"    |   "+str(self.buffer)
 
if __name__ == "__main__":
    Main().run()
