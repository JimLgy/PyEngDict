import re
import itertools as it

'''NOTE: 
    1. 原txt文件里的奇怪方块字符是\x7f!!!
    2. 把词性加进去！！！'''

fname = "go.txt"
fh = open(fname, encoding = 'utf8')

vocab_char1 = ['\sn\.','\sv\.','\sv\.aux\.','\sAbbr\.','\sadj\.','\scontr\.',\
               '\svar\.','\spl\.','\sadv\.']
vocab_char2 = ['-n\.','-v\.','-v\.aux\.','-Abbr\.','-adj\.','-contr\.',\
               '-var\.','-pl\.','-adv\.']
vocab_char = vocab_char1 + vocab_char2
char_property = {}


rexpression = str()
rexpression1 = str()
rexpression2 = str()

for char in vocab_char1:
    rexpression1 += char + '\s|'        # regex with no '-'
#print(rexpression1[0:len(rexpression1)-1])
for char in vocab_char2:
    rexpression2 += char + '\s|'        # regex with '-'
#print(rexpression2[0:len(rexpression2)-1])    

seg_split2 = []
seg_split3 = []
seg_split4 = []
final_output = []

for line in fh:
    line = line.rstrip()
    wordsplit = line.split()
    for char in vocab_char:
        for word in wordsplit:
            if re.search(char,word):
                char_property[char] = wordsplit.index(word)
    
    if re.search(rexpression2[0:len(rexpression2)-1],line):
        print(re.findall(rexpression2[0:len(rexpression2)-1],line))
        seg_split1 = re.split(rexpression2[0:len(rexpression2)-1],line)  # seg after first split   
    else:
        seg_split1 = re.split(rexpression1[0:len(rexpression1)-1],line)
#    if len(seg_split1) > 1:
#        print('working1')
#        for element in seg_split1:
#            if re.search(rexpression1[0:len(rexpression1)-1],element):
#                print('working2')
#                seg_split2 += re.split(rexpression1[0:len(rexpression1)-1],element)
#            else:
#                seg_split2 = seg_split1
#    else:
#        print('working3')
#        seg_split2 = re.split(rexpression1[0:len(rexpression1)-1],line)
#        seg_split2 = re.split(rexpression1[0:len(rexpression1)-1],line)
     # 如何保留被split的字符，比如保留-v.
#print(seg)
#print('The word characteristics are', char_property)
print('There are', len(seg_split1), 'elements in seg_split1')
#print('There are', len(seg_split2), 'elements in seg_split2')
#for e in seg_split1:
#    print('-------------------------------------------------------------------')
#    print(e)


for e in seg_split1:
#    match = re.findall('\.\s[0-9]+',e)
#    print(match)
    count_meaning = 1
    seg_split3.append(re.sub('\(.*\)\s1','TAPoint',e))

#    for meaning in seg_split3:
#        print('-------------------------------------------------------------------')

#print(seg_split3)
for e in seg_split3:
    seg_split4.append(re.sub('\.\s[0-9]+','.\nTAPoint',e))
    
for e in seg_split4:
    if e[0] is '1':
        seg_split4[seg_split4.index(e)] = 'TAPoint' + e[1:len(e)]
#print(seg_split4)

#current_index = 0
for e in seg_split4:
    replace_count = it.count(1)
#    final_output.append(re.sub('TAPoint',lambda x: '{{{}}}'.format(next(replace_count)),e))
    final_output.append(re.sub('TAPoint',lambda x: '{}.'.format(next(replace_count)),e))
for e in final_output:   
    print('-------------------------------------------------------------------')
    print(e)