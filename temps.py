#Corey Dew
#cs21
#Question 4 on pg 562

import tkinter

class MyGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.left_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.right_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.left_frame, \
                                    text="Enter the Celsius temperature: ")
        self.celsius_entry = tkinter.Entry(self.left_frame, \
                                           width=10)
        self.label2 = tkinter.Label(self.mid_frame, \
                                    text="Fahrenheit temperature: ")
        
        self.convert_button = tkinter.Button(self.right_frame, \
                                             text="Convert to Fahrenheit", \
                                             command=self.convert)
        self.quit_button = tkinter.Button(self.right_frame, \
                                          text="Quit", \
                                          command=self.main_window.destroy)

        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.celsius_entry.pack(side='bottom')

        self.value = tkinter.StringVar()
        self.faren_heit_label = tkinter.Label(self.mid_frame, \
                                              textvariable=self.value)

        self.faren_heit_label.pack(side='bottom')


        self.left_frame.pack(side='left')
        self.mid_frame.pack(side='left')
        self.right_frame.pack(side='left')
        self.convert_button.pack(side='top')
        self.quit_button.pack(side='bottom')

        tkinter.mainloop()
    def convert(self):
        try:
            c = float(self.celsius_entry.get())
            f = (9 / 5) * c + 32
            self.value.set(format(f,'.2f'))
        except:
            self.value.set("Invalid input")

my_gui = MyGUI()
