#Corey Dew
#cs21
#Question 3 on pg 562

import tkinter

class MyGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.top_frame = tkinter.Frame(self.main_window)
        self.top_frame2 = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        self.label1 = tkinter.Label(self.top_frame, \
                                    text="Enter the number of gallons: ")
        self.gallon_entry = tkinter.Entry(self.top_frame, \
                                          width=10)
        self.label2 = tkinter.Label(self.top_frame2, \
                                    text="Enter the number of miles: ")
        self.miles_entry = tkinter.Entry(self.top_frame2, \
                                         width=10)
        self.descr_label = tkinter.Label(self.mid_frame, \
                                         text='Miles Per Gallon = ')

        self.calc_button = tkinter.Button(self.bottom_frame, \
                                          text="Calculate MPG", \
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, \
                                          text="Quit", \
                                          command=self.main_window.destroy)


        self.label1.pack(side='left')
        self.gallon_entry.pack(side='left')
        self.label2.pack(side='left')
        self.miles_entry.pack(side='left')
 

        self.value = tkinter.StringVar()
        self.mpg_label = tkinter.Label(self.mid_frame, \
                                       textvariable=self.value)

        self.descr_label.pack(side='left')
        self.mpg_label.pack(side='left')

        self.top_frame.pack()
        self.top_frame2.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        tkinter.mainloop()
    def convert(self):
        try:
            gallon = float(self.gallon_entry.get())
            mile = float(self.miles_entry.get())
            mpg = mile / gallon
            self.value.set(format(mpg,'.2f'))
        except:
            self.value.set("Invalid input")
        
    
my_gui = MyGUI()


