import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # create entry widget for displaying result
        self.result_entry = tk.Entry(master, width=20, font=('Arial', 16))
        self.result_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # create buttons for numbers and operators
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("=", 4, 2)
        self.create_button("+", 4, 3)

        # create clear button
        self.create_button("C", 5, 0, columnspan=2)
        self.create_button("AC", 5, 2, columnspan=2)

        # initialize variables
        self.expression = ""   # current expression
        self.last_operator = None   # last operator entered
        self.result = None   # result of calculation

    # helper function to create a button with specified text and position
    def create_button(self, text, row, column, columnspan=1, padx=10, pady=10, **kwargs):
        button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 14), command=lambda:self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, **kwargs)

    # handler function for button clicks
    def button_click(self, text):
        if text in "0123456789.":
            self.expression += text   # add digit or decimal point to expression
        elif text in "+-*/":
            if self.last_operator is not None:   # if there was a previous operator entered
                self.calculate()   # calculate previous operation
            self.expression += text   # add operator to expression
            self.last_operator = text   # update last operator
        elif text == "=":
            self.calculate()   # calculate current expression
            self.last_operator = None   # reset last operator
        elif text == "C":
            self.expression = self.expression[:-1]   # remove last character from expression
        elif text == "AC":
            self.expression = ""   # clear expression
            self.result = None   # reset result
            self.last_operator = None   # reset last operator

        # update display
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, self.expression)

def calculate(self):
    try:
        if self.expression:
            self.result = eval(self.expression)
            self.expression = str(self.result)
    except:
        self.expression = "Error"
        self.result = None

'''
def calculate(self):
    try:
        if self.result is None:   # if there is no previous result
            self.result = float(self.expression)   # set result to current expression
        else:
            # perform calculation based on last operator entered
            if self.last_operator == "+":
                self.result += float(self.expression)
            elif self.last_operator == "-":
                self.result -= float(self.expression)
            elif self.last_operator == "*":
                self.result *= float(self.expression)
            elif self.last_operator == "/":
                self.result /= float(self.expression)

        self.expression = str(self.result)   # update expression to result
    except ZeroDivisionError:
        # handle division by zero error
        self.expression = "Error"
        self.result = None
    except:
        # handle other calculation errors
        self.expression = "Error"
        self.result = None
'''

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()