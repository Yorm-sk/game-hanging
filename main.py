# main prog
from algorimth import *
from tkinter import *
import pickle
from tkinter import messagebox
from random import randint

#import dict and choose of word
f  = open('dict1.txt', 'rb')
l1 = pickle.load(f)
f.close()
word = l1[randint(0, len(l1) - 1)]

#function for check and enter
def do(letter):
    global word
    global field2
    global counter
    field.delete(0, END)
    if check(letter) == FALSE:
        messagebox.showerror('Error', 'You can only use letter from a to z')
    elif letter in field2.get():
        messagebox.showerror('Error', 'Your letter is already quessed!')
    else:
        i2 = 0
        for i in range (0, len(word)):
            if letter == word[i]:
                field2.delete(i)
                field2.insert(i, letter)
                if str(field2.get()) == str(word):
                    messagebox.showinfo('WIN!', 'Gonratualion the word was quessed!')
                    root.destroy()
            else:
                i2 +=1
                if i2 == len(word):
                    counter = calc(counter)
                    lab1.config(text =('U have '+ str(counter)+' tryes!'))
                if counter == 0:
                    messagebox.showinfo('Defeeat', 'You was hang')
                    root.destroy()


#create window
root = Tk()
root.title('Hanging')
root.geometry('800x600')

#counter of  tryes
counter = 6
lab1 = Label(root, text  = ('U have '+ str(counter)+' tryes!'), font = '24')
lab1.pack()
Label(root, text = 'Enter small letter', font = '24').pack()


#field for entry
field = Entry(width = 1)
field.pack()

#buttton for check
Button(root, text = 'Enter', command = lambda: do(field.get()), font = '24').pack()
root.bind('<Return>', lambda e: do(field.get()))

#label with your word
Label(root, text = 'Word to guess:', font = '24').pack()

# field with your word
field2 = Entry(width = len(word))
field2.pack()
field2.insert(0, '_' * len(word))


print(word)
print(len(word))
root.mainloop()