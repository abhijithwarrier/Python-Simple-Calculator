#Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI TO CREATE A SIMPLE CALCULATOR

# imporitng packages for using tkinter
import tkinter as tk
from tkinter import *

# defining class SimpleCal
class SimpleCal(tk.Frame):

    def __init__(self, root1) :

        Frame.__init__(self, root1)
        self.createWidgets()

#-----

    # creating widgets
    def createWidgets(self) :

        # creating the widget
        labelNum1 = Label(self,text = "ENTER NUMBER 1 : ")
        # positioning the widget
        labelNum1.grid(row = 0, column = 0, pady = 5, padx = 5)

        num1Entry = Entry(self,width = 30,textvariable = number1)
        # textvaribale can be used for getting the value of the entry
        num1Entry.grid(row = 0, column = 1, pady = 5, padx = 5)

        labelNum2 = Label(self,text = "ENTER NUMBER 2 : ")
        labelNum2.grid(row = 1, column = 0, pady = 5, padx = 5)

        num2Entry = Entry(self,width = 30, textvariable = number2)
        num2Entry.grid(row = 1, column = 1, pady = 5, padx = 5)

        labelOP = Label(self, text = "ENTER OPERATOR : ")
        labelOP.grid(row = 2, column = 0, pady = 5, padx = 5)

        opEntry = Entry(self, width = 30, textvariable = operator)
        opEntry.grid(row = 2, column = 1, pady = 5, padx = 5)

        button = Button(self,width=20,text="CALCULATE",command=self.Calculate)
        # command can be used for calling the function Calculate()
        button.grid(row = 3, column = 1, pady = 5, padx = 5)

        labelAns = Label(self, text = "ANSWER : ")
        labelAns.grid(row = 4, column = 0, pady = 5, padx = 5)

        displayAns = Entry(self, textvariable = answer)
        displayAns.grid(row = 4, column = 1, pady = 5, padx = 5)

#-----

    #performing the operations
    def Calculate(self):

        num1 = int(number1.get())
        num2 = int(number2.get())
        op = operator.get()
        ans = ""
        try :
            if op == "+":
                ans = num1 + num2
                print(ans)
            elif op == "-":
                ans = num1 - num2
            elif op == "*":
                ans = num1 * num2
            elif op == "/":
                ans = num1 / num2
            elif op == "%":
                ans = num1 % num2
            else:
                displayAns = Entry(self, answer.set("INVALID OPERATOR"))
                displayAns.grid(row = 4, column = 1, pady = 5, padx = 5)

            displayAns = Entry(self, answer.set(str(ans)))
            displayAns.grid(row = 4, column = 1, pady = 5, padx = 5)
        except:
            print()
#-----

# creating object root of tk
root = tk.Tk()

# setting title
root.title("SIMPLE CALCULATOR")

# disabling resizing of window
root.resizable(False, False)

# creating tkinter variable
number1 = StringVar(root)
number2 = StringVar(root)
operator = StringVar(root)
answer = StringVar(root)

# creating object of class SimpleCal
frame = SimpleCal(root)

# organising label before placing them
# in parent
frame.pack()

# defining infinite loop to run application
frame.mainloop()

#-----