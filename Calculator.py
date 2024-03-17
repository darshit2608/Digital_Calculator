from tkinter import Tk, END, Entry, N, E, S, W, Button
from tkinter import font
from tkinter import Label
from functools import partial

def get_input(entry, argu):
    entry.insert(END, argu)

def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)

def clear(entry):
    entry.delete(0, END)

def calc(entry):
    input_info = entry.get()
    try:
        output = str(eval(input_info.strip()))
    except ZeroDivisionError:
        popupmsg()
        output = ""
    clear(entry)
    entry.insert(END, output)

def popupmsg():
    popup = Tk()
    popup.resizable(0, 0)
    popup.geometry("150x100")
    popup.title("Alert")
    label = Label(popup, text="Cannot divide by 0 ! \n Enter valid values", fg="red")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", bg="#FF7F0E", fg="white", command=popup.destroy)
    B1.pack()

def cal():
    root = Tk()
    root.title("Calculator")
    root.resizable(0, 0)

    entry_font = font.Font(family="Helvetica", size=15)
    entry = Entry(root, justify="right", font=entry_font)
    entry.grid(row=0, column=0, columnspan=4,
               sticky=N + W + S + E, padx=5, pady=5)

    num_button_bg = '#2C3E50'
    cal_button_bg = '#E74C3C'
    other_button_bg = '#3498DB'
    text_fg = '#FFFFFF'
    button_active_bg = '#FF5733'

    num_button = partial(Button, root, fg=text_fg, bg=num_button_bg,
                         padx=10, pady=3)
    cal_button = partial(Button, root, fg=text_fg, bg=cal_button_bg,
                         padx=10, pady=3, activebackground=button_active_bg)

    button7 = num_button(text='7', command=lambda: get_input(entry, '7'), activebackground="#3498DB")
    button7.grid(row=2, column=0, pady=5)

    button8 = num_button(text='8', command=lambda: get_input(entry, '8'), activebackground="#3498DB")
    button8.grid(row=2, column=1, pady=5)

    button9 = num_button(text='9', command=lambda: get_input(entry, '9'), activebackground="#3498DB")
    button9.grid(row=2, column=2, pady=5)

    button10 = cal_button(text='+', command=lambda: get_input(entry, '+'))
    button10.grid(row=4, column=3, pady=5)

    button4 = num_button(text='4', command=lambda: get_input(entry, '4'), activebackground="#3498DB")
    button4.grid(row=3, column=0, pady=5)

    button5 = num_button(text='5', command=lambda: get_input(entry, '5'), activebackground="#3498DB")
    button5.grid(row=3, column=1, pady=5)

    button6 = num_button(text='6', command=lambda: get_input(entry, '6'), activebackground="#3498DB")
    button6.grid(row=3, column=2, pady=5)

    button11 = cal_button(text='-', command=lambda: get_input(entry, '-'))
    button11.grid(row=3, column=3, pady=5)

    button1 = num_button(text='1', command=lambda: get_input(entry, '1'), activebackground="#3498DB")
    button1.grid(row=4, column=0, pady=5)

    button2 = num_button(text='2', command=lambda: get_input(entry, '2'), activebackground="#3498DB")
    button2.grid(row=4, column=1, pady=5)

    button3 = num_button(text='3', command=lambda: get_input(entry, '3'), activebackground="#3498DB")
    button3.grid(row=4, column=2, pady=5)

    button12 = cal_button(text='*', command=lambda: get_input(entry, '*'))
    button12.grid(row=2, column=3, pady=5)

    button0 = num_button(text='0', command=lambda: get_input(entry, '0'), activebackground="#3498DB")
    button0.grid(row=5, column=0, pady=5)

    button13 = num_button(text='.', command=lambda: get_input(entry, '.'), activebackground="#3498DB")
    button13.grid(row=5, column=1, pady=5)

    button14 = Button(root, text='/', fg=text_fg, bg=cal_button_bg, padx=10, pady=3,
                      command=lambda: get_input(entry, '/'))
    button14.grid(row=1, column=3, pady=5)

    button15 = Button(root, text='<-', bg=other_button_bg, padx=10, pady=3,
                      command=lambda: backspace(entry), activebackground=button_active_bg)
    button15.grid(row=1, column=0, columnspan=2,
                  padx=3, pady=5, sticky=N + S + E + W)

    button16 = Button(root, text='C', bg=other_button_bg, padx=10, pady=3,
                      command=lambda: clear(entry), activebackground=button_active_bg)
    button16.grid(row=1, column=2, pady=5)

    button17 = Button(root, text='=', fg=text_fg, bg=cal_button_bg, padx=10, pady=3,
                      command=lambda: calc(entry), activebackground=button_active_bg)
    button17.grid(row=5, column=3, pady=5)

    button18 = Button(root, text='^', fg=text_fg, bg=cal_button_bg, padx=10, pady=3,
                      command=lambda: get_input(entry, '**'))
    button18.grid(row=5, column=2, pady=5)

    exit_button = Button(root, text='Quit', fg='white', bg='#3498DB', font=("Helvetica", 10, "bold"), command=root.quit, height=1, width=7)
    exit_button.grid(row=6, column=1)

    root.mainloop()

if __name__ == '__main__':
    cal()
