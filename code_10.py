'''
a = [1, 11, 21, 1211, 111221,
Found in: http://www.pythonchallenge.com/pc/return/sequence.txt
len(a[30]) = ?

# using groupby will help you a lot here.
total_lists = [list(g) for k,g in groupby(list(stri))            ]
'''

# idea is to group all similar elements together if they occur together

def rec_sequence(string, ctr):
    final_ls = []

    def sequence(a):
        ind = 0
        ctr = 0
        while ind!=len(a):
            ls = []
            ref = a[ind]
            ls.append(ref)
            for ind_, elem_ in enumerate(a[ind+1:]):
                if elem_ == ref:
                    ls.append(elem_)
                else:
                    final_ls.append(ls)
                    ind += ind_
                    break
            ind += 1
        return final_ls

    ls = sequence(list(string))
    ls_ = [ele for row in ls for ele in row]
    ls.extend([list(string)[::-1][:(len(list(string)) - len(ls_))]])
    string_n = ''
    for row in ls:
        string_n += str(len(row))+str(row[0])
    print(string_n)
    print("\n", len(string_n)) # 5808 leads to next challenge.
    ctr += 1
    if ctr==31:
        return 0
    rec_sequence(string_n, ctr)

x = rec_sequence('1', 1)


