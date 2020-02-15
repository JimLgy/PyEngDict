from tkinter import *

def buttonSearch(event = None):
    if len(vocabText.get()) > 0:
        historyBox.insert(0, vocabText.get())
        vocabEntry.delete(0, END)

# Create main window object
root = Tk()

# Widgets

# Search Label
searchLabel = Label(root, text='Please Enter a Word: ',\
    font = ('bold', 14), pady = 20)
searchLabel.grid(row = 0, column = 0, sticky = W)

# Entry bar
vocabText = StringVar()
vocabEntry = Entry(root, textvariable = vocabText)
vocabEntry.grid(row = 0, column = 1)

# search history list and its scrollbar
scrollbarhB = Scrollbar(root, orient = VERTICAL)
scrollbarhB.grid(row = 1, column = 3)
historyBox = Listbox(root, height = 35, width = 50)
historyBox.grid(row = 1, column = 0, columnspan = 3, padx = 20)
# connect the scrollbar to the history listbox
historyBox.configure(yscrollcommand = scrollbarhB.set)
scrollbarhB.configure(command = historyBox.yview)

# text box
meaning = Text(root, height = 45, width = 70)
meaning.grid(row = 1, column = 3)

# Search button
root.bind('<Return>', buttonSearch)
searchBtn = Button(root, text = 'Search', padx = 20, command = buttonSearch)
searchBtn.grid(row = 0, column = 2)



# Main window config
root.title('English Dictionary by Guanyun Liu - Searching Mode')
root.geometry('1000x700')
# Start program
root.mainloop()
