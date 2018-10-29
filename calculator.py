#-*-coding: utf-8-*-
import sys
from tkinter import *
from decimal import *

# calculation methods
#####################
# given a simple equation string s, num1 = num2 =0,
# return operation, new num1 and num2
def parse_simple_eq(s, num1, num2):
    operation = ""
    # operations include +,-,*,/,%

    operation_known =  False
    num1_str = ""
    num2_str = ""
    for i in range(len(s)):
        curr_char = s[i]
        if curr_char != ' ':  # do something only if char is not blank
            if operation_known == False:  # operation isnt known yet - parsing num1
                if curr_char == '+' or curr_char == '-' or curr_char == '*' or curr_char == '/' or curr_char == '%':
                    #check num1_str is empty
                    num1 = 0 if num1_str == "" else Decimal(num1_str)
                    operation = curr_char
                    operation_known = True
                else:
                    num1_str += curr_char
            else:   # operation is known - parsing num2
                num2_str += curr_char
    #check num2_str is empty
    num2 = 0 if num2_str == "" else Decimal(num2_str)
    return (operation,num1,num2)

#return double by solving simple_eq
def solve_simple_eq(s):
    result = 0.0
    operation,num1,num2 = parse_simple_eq(s, 0.0, 0.0)

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/" or operation == "%":
        try:
            if operation == '/':
                result = num1 / num2
            else: # operation is %
                result = num1 % num2
        except:
            return "Cannot divide by 0"
    elif operation == "":
        result = 0 if s == "" else Decimal(s)
    else:
        raise ValueError("Improper simple_eq: ", s)
    return result

# tinker help functions
class calc:
    # pressed button's value is inserted into the end of the text area
    def action(self,argi):
        self.e.insert(END,argi)

    # when equals button is pressed
    def equals(self):
        self.expression = self.e.get()
        try:
            # evaluate the expression using solve_simple_eq function
            simple_eq = self.expression
            self.value = solve_simple_eq(simple_eq)
        except SyntaxError or NameErrror:
            self.e.delete(0,END)
            self.e.insert(0,'Invalid Input!')
        else:
            self.e.delete(0,END)
            self.e.insert(0,self.value)

    # when clear button is pressed,clears the text input area
    def clearall(self):
        self.e.delete(0,END)

    def clear1(self):
        self.txt=self.e.get()[:-1]
        self.e.delete(0,END)
        self.e.insert(0,self.txt)

    # gui initialization
    def __init__(self,master):
        master.title('Calulator')
        master.geometry('220x160')
        self.e = Entry(master)
        self.e.grid(row=0,column=0,columnspan=6,pady=3)
        self.e.focus_set() #Sets focus on the input text area
        #Generating Buttons
        Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
        Button(master,text='AC',width=3,command=lambda:self.clearall()).grid(row=1, column=4)
        Button(master,text='C',width=3,command=lambda:self.clear1()).grid(row=1, column=5)
        Button(master,text="+",width=3,command=lambda:self.action('+')).grid(row=4, column=3)
        Button(master,text="*",width=3,command=lambda:self.action('*')).grid(row=2, column=3)
        Button(master,text="-",width=3,command=lambda:self.action('-')).grid(row=3, column=3)
        Button(master,text="/",width=3,command=lambda:self.action('/')).grid(row=1, column=3)
        Button(master,text="%",width=3,command=lambda:self.action('%')).grid(row=4, column=2)
        Button(master,text="7",width=3,command=lambda:self.action('7')).grid(row=1, column=0)
        Button(master,text="8",width=3,command=lambda:self.action(8)).grid(row=1, column=1)
        Button(master,text="9",width=3,command=lambda:self.action(9)).grid(row=1, column=2)
        Button(master,text="4",width=3,command=lambda:self.action(4)).grid(row=2, column=0)
        Button(master,text="5",width=3,command=lambda:self.action(5)).grid(row=2, column=1)
        Button(master,text="6",width=3,command=lambda:self.action(6)).grid(row=2, column=2)
        Button(master,text="1",width=3,command=lambda:self.action(1)).grid(row=3, column=0)
        Button(master,text="2",width=3,command=lambda:self.action(2)).grid(row=3, column=1)
        Button(master,text="3",width=3,command=lambda:self.action(3)).grid(row=3, column=2)
        Button(master,text="0",width=3,command=lambda:self.action(0)).grid(row=4, column=0)
        Button(master,text=".",width=3,command=lambda:self.action('.')).grid(row=4, column=1)
        Button(master,text="(",width=3,command=lambda:self.action('(')).grid(row=2, column=4)
        Button(master,text=")",width=3,command=lambda:self.action(')')).grid(row=2, column=5)

# main
if __name__ == "__main__":
    root = Tk()
    obj=calc(root) # object instantiated
    root.mainloop()


# simple console test run
def run_calculator():
    while 1:
        menu = "calculator.py\n\n" + "___operations___\n. ( + )\n. ( - )\n. ( * )\n. ( / )\n. ( % )\n\n"
        print(menu)
        simple_eq = input(">> Input simple_eq...\n")
        if simple_eq == "quit" or simple_eq == "q" or simple_eq == "clear" or simple_eq == "c":
            break
        try:
            ans = solve_simple_eq(simple_eq)
            print("   _____________\n>> Ans:\t",ans,"\n   _____________")
        except:
            print("\n>> Wrong syntax for equation: ", simple_eq)
