
# Read File input
File = 'rosalind_gc.txt'
file = open(File, 'r')

# Change File Lines to List element
fr =  file.readlines()

# Bace Count Dictionary
dict = {'G':0, 'C':0, 'A':0, 'T':0}

# for loop File lines
for i in fr:
    if i[0] is '>':
        head = i[1:14]
        GC = dict['G'] + dict['C']
        all = dict['G'] + dict['C'] + dict['A'] + dict['T']
        
        
        if all == 0:
            pass

        else:
            GC_ratio = GC/all*100
            ratio = round(GC_ratio / 1.0000, 6)
            dict = {'G':0, 'C':0, 'A':0, 'T':0}
            print(str(head) + ' ' +str(ratio))

       
    
# sequence string for loop in file lines
    elif i[0] is not '>':
        for k in i:
            if k is 'G':
                dict[k] = dict[k] + 1
            if k is 'C':
                dict[k] = dict[k] + 1
            if k is 'A':
                dict[k] = dict[k] + 1
            if k is 'T':
                dict[k] = dict[k] + 1
   
'''
#line count
def count_line(File):
    file = open(File)
    line_num = 0
    while (file.readline()):
        line_num += 1
    return line_num


s=""

for k in range(1, count_line(File)):
    s += fr[k]


#s_raw = str(fr[1:])
#s = s_raw.replace('\n', '')
'''
     
