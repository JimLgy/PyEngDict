from tkinter import *
import xlrd

def LboxSelection(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)

    book = xlrd.open_workbook('Vocab_list.xlsx')
    sheet = book.sheet_by_name('Sheet1')
    for i in range(sheet.nrows):
        if i is 0:
            continue
        else:
            cell_value_word = sheet.cell(i,1).value
            cell_value_id = int(sheet.cell(i,0).value)
            cell_value_meaning1 = sheet.cell(i,2).value
            if sheet.row_len(i) > 3:
                if sheet.row_len(i) == 4:
                    cell_value_meaning2 = sheet.cell(i,3).value
                    cell_value_meaning3 = ''
                else:
                    cell_value_meaning2 = ''
                    cell_value_meaning3 = ''
                if sheet.row_len(i) == 5:
                    cell_value_meaning2 = sheet.cell(i,3).value
                    cell_value_meaning3 = sheet.cell(i,4).value
                else:
                    cell_value_meaning2 = sheet.cell(i,3).value
                    cell_value_meaning3 = ''
            else:
                cell_value_meaning2 = ''
                cell_value_meaning3 = ''
            meaning[cell_value_word] = [cell_value_id, cell_value_meaning1, cell_value_meaning2, cell_value_meaning3]

    display.config(state=NORMAL)
    display.delete(1.0,END)
    output = meaning[value[1]][1] + '\n' + meaning[value[1]][2] + '\n' + meaning[value[1]][3]
    display.insert(INSERT, output)
    display.config(state=DISABLED)

root = Tk()

book = xlrd.open_workbook('Vocab_list.xlsx')
sheet = book.sheet_by_name('Sheet1')

historyBox = Listbox(root, height = 35, width = 50)
historyBox.grid(row = 0, column = 0)

display = Text(root, font = 16)
display.config(state=NORMAL)
display.grid(row = 0, column = 1)

row_count = 1
meaning = {}


for i in range(sheet.nrows):
    if i is 0:
        continue
    else:
        cell_value_word = sheet.cell(i,1).value
        cell_value_id = int(sheet.cell(i,0).value)
        cell_value_meaning1 = sheet.cell(i,2).value
        if sheet.row_len(i) > 3:
            if sheet.row_len(i) == 4:
                cell_value_meaning2 = sheet.cell(i,3).value
                cell_value_meaning3 = ''
            else:
                cell_value_meaning2 = ''
                cell_value_meaning3 = ''
            if sheet.row_len(i) == 5:
                cell_value_meaning2 = sheet.cell(i,3).value
                cell_value_meaning3 = sheet.cell(i,4).value
            else:
                cell_value_meaning2 = sheet.cell(i,3).value
                cell_value_meaning3 = ''
        else:
            cell_value_meaning2 = ''
            cell_value_meaning3 = ''
        meaning[cell_value_word] = [cell_value_id, cell_value_meaning1, cell_value_meaning2, cell_value_meaning3]


for word in meaning:
    historyBox.insert(END, [meaning[word][0], word])

# display.insert(INSERT, row[3].value)
historyBox.bind('<<ListboxSelect>>', LboxSelection)



# root.bind('<Return>', buttonSearch)
# searchBtn = Button(root, text = 'Search', padx = 20, command = buttonSearch)
# searchBtn.pack()

root.title('English Dictionary by Guanyun Liu - Review Mode')
root.geometry('1200x700')

root.mainloop()
