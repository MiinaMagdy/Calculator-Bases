from tkinter import *

root = Tk()
root.geometry("590x400")

def digit_b(mod):
    if mod < 10:
        return chr(mod + ord('0'))
    else:
        return chr(mod - 10 + ord('A'))

def digit_dec(c):
    if ord(c) <= ord('9'):
        return ord(c) - ord('0')
    else:
        return 10 + c - ord('A')

def convert_b(dec, base):
    s = ''
    while dec:
        s += digit_b(dec % base)
        dec /= base
    return s[::-1]

def convert_dec(rep, base):
    ans = 0
    for ch in rep:
        ans = ans * base + digit_dec(ch)
    return ans

def addStrings(s, t, base):
    res = ''
    sz = max(len(s), len(t))
    s = s[::-1]
    t = t[::-1]
    carry = '0'
    e, f, i = 0, 0, 0
    while i < sz or carry != '0':
        e = 0 if i >= len(s) else digit_dec(s[i])
        f = 0 if i >= len(t) else digit_dec(t[i])
        tmp = digit_dec(carry) + e + f
        carry = digit_b(tmp // base)
        res += digit_b(tmp % base)
        i += 1
    res = res[::-1]
    while len(res) > 1 and res[0] == '0':
        res = res[1:len(res)]
    return res

def multiStrings(s, t, base):
    res = ''
    s = s[::-1]
    t = t[::-1]
    i = 0
    while i < len(t):
        tmp = i * '0'
        carry = '0'
        j = 0
        while j < len(s):
            m = (digit_dec(t[i])) * (digit_dec(s[j])) + (digit_dec(carry))
            carry = digit_b(m // base)
            tmp += digit_b(m % base)
            j += 1
        tmp += carry
        tmp = tmp[::-1]
        res = addStrings(res, tmp, base)
        i += 1
    while len(res) > 1 and res[0] == '0':
        res = res[1:len(res)]
    return res

def complement(rep, base, is_r = True):
    res = ''
    i = 0
    while i < len(rep):
        res += chr((base - 1) - (ord(rep[i]) - ord('0')) + ord('0'))
        i += 1
    return addStrings(res, "1", base) if is_r else res

def is_less(s, t):
    i = 0
    while i < len(s):
        if (s[i] > t[i]):
            return False
        if (s[i] < t[i]):
            return True
        i += 1
    return False

def minusStrings(s, t, base):
    while (len(t) < len(s)): 
        t = "0" + t;
    while (len(s) < len(t)): 
        s = "0" + s;
    less = is_less(s, t)
    t_comp = complement(t, base)
    s_add_t_comp = addStrings(s, t_comp, base)
    if len(s_add_t_comp) > len(s):
        s_add_t_comp = s_add_t_comp[1 : len(s_add_t_comp)]
    return "-" + complement(s_add_t_comp, base) if less else s_add_t_comp

def enabling0(event):
    myEntry0.config(state=NORMAL)
    if myEntry0.get() == 'Base':
        myEntry0.delete(0, END)

def enabling1(event):
    myEntry1.config(state=NORMAL)
    if myEntry1.get() == 'Number 1':
        myEntry1.delete(0, END)

def enabling2(event):
    myEntry2.config(state=NORMAL)
    if myEntry2.get() == 'Number 2':
        myEntry2.delete(0, END)

def enablingo(event):
    myOperator.config(state=NORMAL)
    if myOperator.get() == 'operator':
        myOperator.delete(0, END)

myEntry0 = Entry(root, width=20)
myEntry0.insert(0, 'Base')
myEntry0.config(state=DISABLED)
myEntry0.bind('<Button-1>', enabling0)
myEntry0.grid(row=0, column=4)

myEntry1 = Entry(root, width=20)
myEntry1.insert(0, 'Number 1')
myEntry1.config(state=DISABLED)
myEntry1.bind('<Button-1>', enabling1)
myEntry1.grid(row=0, column=0)

myEntry2 = Entry(root, width=20)
myEntry2.insert(0, 'Number 2')
myEntry2.config(state=DISABLED)
myEntry2.bind('<Button-1>', enabling2)
myEntry2.grid(row=0, column=2)

myOperator = Entry(root, width=10)
myOperator.insert(0, 'operator')
myOperator.config(state=DISABLED)
myOperator.bind('<Button-1>', enablingo)
myOperator.grid(row=0, column=1)

def myDelete():
    myLabel.grid_forget()

def myClick():
    global myLabel
    s = myEntry1.get()
    t = myEntry2.get()
    oper = myOperator.get()
    base = int(myEntry0.get())
    res = 'Empty'
    if oper == '-':
        res = minusStrings(s, t, base)
    elif oper == '+':
        res = addStrings(s, t, base)
    elif oper == '*':
        res = multiStrings(s, t, base)

    print(res)
    try:
        myDelete()
        myLabel = Label(root, text=res)
        myLabel.grid(row=2, column=1)
    except:
        myLabel = Label(root, text=res)
        myLabel.grid(row=2, column=1)

myButton = Button(root, text='Click Me!', command=myClick)

myButton.grid(row=1, column= 1)

root.mainloop()
