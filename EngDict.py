import re
# if vocab_in is 'quit()':
#     status = 0
# else:
#     status = 1
status = 1
vocab = dict()
vocab_sort = list()
vocab_list = list()
# vocab_char = ['n.','v.','-v.','Abbr.','adj.','contr.','-n.','-adj.','colloq.','var.','pl.','adv.','']

# Build dictionary
fname = 'OxfordDict.txt'
fh = open(fname)

for line in fh:
    line = line.rstrip()
    # line = line.lower()
    if len(line) != 0:
        words = line.lower().split()
        vocab_list.append(words[0])
        # print(words[0])

# print(vocab_list)

# input
while status == 1:
    vocab_in = input('Please Enter a Word: ')   # input English vocab
    if vocab_in is '1':
        print('Process Complete!')
        status = 0
    elif not vocab_in in vocab_list:
        print('World Not Found! Please Enter Another One.')
        continue
    elif vocab_in is '':
        print('Please Enter a Valid Word!')
        continue
    else:
        vocab[vocab_in] = vocab.get(vocab_in,0) + 1

print(vocab)



# Sort the list
for key, val in list(vocab.items()):
    vocab_sort.append((val, key))

vocab_sort.sort(reverse=True)
print(vocab_sort)
