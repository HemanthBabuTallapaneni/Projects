# import tkinter
# from tkinter import *
# window = tkinter.Tk()
# window.title("My first GUI")
# window.minsize(400, 300)
#
# label = tkinter.Label(window, text="Label", font=("lucida", 24, "bold"))
# label.pack()
#
#
#
#
# def button_clicked():
#     text = input.get()
#     label.config(text= text)
#     print("Button clicked")
#
# button = tkinter.Button(window, text="Click me", command = button_clicked)
# button.pack()
#
# input = Entry()
# input.pack()
# print(input.get())
#
# window.mainloop()


from tkinter import *

def miles_to_kilometers():
    miles = float(miles_input.get())
    km = miles * 1.60934
    kilometers_result.config(text = f"{km}")


window = Tk()
window.title("Miles to kilometers converter")
window.configure(padx = 20, pady = 20)

miles_input = Entry(width = 7)
miles_input.grid(column = 1, row = 0)

miles_label = Label(text="Miles")
miles_label.grid(column = 2, row = 0)

is_equal_label = Label(text="is Equal to")
is_equal_label.grid(column = 0, row = 1)

kilometers_result = Label(text="0")
kilometers_result.grid(column = 1, row = 1
                       )
kilometers_label = Label(text="kilometers")
kilometers_label.grid(column = 2, row = 1)

calculate_button = Button(text="Calculate", command=miles_to_kilometers)
calculate_button.grid(column = 1, row = 2)


window.mainloop()
