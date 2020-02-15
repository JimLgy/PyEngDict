from tkinter import *

def buttonSearch(event = None):
    global vocab_entry
    wordLabel = Label(window_search, text=vocab_entry.get())
    wordLabel.grid(row=0, column=3)

def SearchWindow():
    window_search = Toplevel(app)
    # Part
    vocab_text = StringVar()
    vocab_label = Label(window_search, text='Please Enter a Word', font=('bold', 14), pady=20)
    vocab_label.grid(row=0, column=0, sticky=W)
    vocab_entry = Entry(window_search, textvariable=vocab_text)
    vocab_entry.grid(row=0, column=1)

    window_search.bind('<Return>', buttonSearch)
    button_search = Button(window_search, text='Search', padx=20, command=buttonSearch)
    button_search.grid(row=0, column=2)
    return
# Create main window object
app = Tk()

# Search button to search window
button_newWin = Button(app, text='Search', padx=40, pady=40, command=SearchWindow)
button_newWin.grid(row=0, column=0)

# Review button to review window





app.title('English Dictionary by Guanyun Liu')
app.geometry('1000x700')
# Start program
app.mainloop()
