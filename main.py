from tkinter import *
import random

# Configuring and Setting up the WINDOW
win = Tk()
win.configure(background='lime')
win.title('Dice App')
win.resizable(True, True)


# Defining the FUNC. for the roll_button
def roll_func():
    nums = [1, 2, 3, 4, 5, 6]
    rolled_num = random.choice(nums)
    rolled_num_label = Label(win, text=rolled_num, bg='red', fg='white', font=('Tahoma', 15))
    rolled_num_label.pack()



# Configuring and Setting up the WIDGETS
guid_label_text = 'This is a Program that can be a good graphical Dice ☺'
guid_label = Label(win, text=guid_label_text, bg='cyan', fg='black', font=('Tahoma', 15))
guid_label.pack()
roll_button = Button(win, text='Roll The Dice', bg='blue', fg='white', font=('Tahoma', 15), command=roll_func)
roll_button.pack()


# Putting the Window in the MAINLOOP
win.mainloop()
