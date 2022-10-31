from tkinter import *
# globally declare the expression variable
expression = ""

# Function to update expression
# in the text entry box
def press(num):
  # point out the global expression variable
  global expression

  # concatenation of string
  expression = expression + str(num)

  # update the expression by using set method
  equation.set(expression)


# Function to evaluate the final expression
def equalpress():
  # Try and except statement is used
  try:

     global expression

     # into string
     total = str(eval(expression))

     equation.set(total)

     # initialize the expression variable
     expression = ""

  except:

     equation.set(" error ")
     expression = ""

# of text entry box
def remove():
  global expression
  expression = ""
  equation.set("")

def backspace():
   global expression
   expression= expression[:-1]
   equation.set(expression)

# Driver code
if __name__ == "__main__":
  gui = Tk()
  gui.configure(background="blue")
  gui.title("Calculator")
  gui.geometry("280x160")
  equation = StringVar()
  expression_field = Entry(gui, textvariable=equation)
  expression_field.grid(columnspan=4, ipadx=70)

  # create a Buttons and place at a particular
  # location inside the root window .
  # when user press the button, the command or
  # function affiliated to that button is executed .
  one = Button(gui, text=' 1 ', fg='purple', bg='orange',
              command=lambda: press(1), height=2, width=8)
  one.grid(row=2, column=0)

  two = Button(gui, text=' 2 ', fg='purple', bg='orange',
              command=lambda: press(2), height=2, width=8)
  two.grid(row=2, column=1)

  three = Button(gui, text=' 3 ', fg='purple', bg='orange',
              command=lambda: press(3), height=2, width=8)
  three.grid(row=2, column=2)

  four = Button(gui, text=' 4 ', fg='purple', bg='orange',
              command=lambda: press(4), height=2, width=8)
  four.grid(row=3, column=0)

  five = Button(gui, text=' 5 ', fg='purple', bg='orange',
              command=lambda: press(5), height=2, width=8)
  five.grid(row=3, column=1)

  six = Button(gui, text=' 6 ', fg='purple', bg='orange',
              command=lambda: press(6), height=2, width=8)
  six.grid(row=3, column=2)

  seven = Button(gui, text=' 7 ', fg='purple', bg='orange',
              command=lambda: press(7), height=2, width=8)
  seven.grid(row=4, column=0)

  eight = Button(gui, text=' 8 ', fg='purple', bg='orange',
              command=lambda: press(8), height=2, width=8)
  eight.grid(row=4, column=1)

  nine = Button(gui, text=' 9 ', fg='purple', bg='orange',
              command=lambda: press(9), height=2, width=8)
  nine.grid(row=4, column=2)

  zero = Button(gui, text=' 0 ', fg='purple', bg='orange',
              command=lambda: press(0), height=2, width=8)
  zero.grid(row=5, column=0)

  add = Button(gui, text=' + ', fg='purple', bg='orange',
           command=lambda: press("+"), height=2, width=8)
  add.grid(row=2, column=3)

  substract = Button(gui, text=' - ', fg='purple', bg='orange',
           command=lambda: press("-"), height=2, width=8)
  substract.grid(row=3, column=3)

  exponential = Button(gui, text=' ^ ', fg='purple', bg='orange',
                 command=lambda: press("**"), height=2, width=8)
  exponential.grid(row=6, column=1)

  left_bracket = Button(gui, text=' ( ', fg='purple', bg='orange',
                       command=lambda: press("("), height=2, width=8)
  left_bracket.grid(row=6, column=2)

  right_bracket = Button(gui, text=' ) ', fg='purple', bg='orange',
                         command=lambda: press(")"), height=2, width=8)
  right_bracket.grid(row=6, column=3)

  back_space = Button(gui, text=' backspace ', fg='purple', bg='orange',
                      command=backspace, height=2, width=8)
  back_space.grid(row=7, column=1)

  multiply = Button(gui, text=' * ', fg='purple', bg='orange',
              command=lambda: press("*"), height=2, width=8)
  multiply.grid(row=4, column=3)

  divide = Button(gui, text=' / ', fg='purple', bg='orange',
              command=lambda: press("/"), height=2, width=8)
  divide.grid(row=5, column=3)

  equal = Button(gui, text=' = ', fg='purple', bg='orange',
           command=equalpress, height=2, width=8)
  equal.grid(row=5, column=2)

  remove = Button(gui, text='AC', fg='purple', bg='orange',
           command=remove, height=2, width=8)
  remove.grid(row=5, column='1')

  Decimal= Button(gui, text='.', fg='purple', bg='orange',
              command=lambda: press('.'), height=2, width=8)
  Decimal.grid(row=6, column=0)

  # start the GUI
  gui.mainloop()
