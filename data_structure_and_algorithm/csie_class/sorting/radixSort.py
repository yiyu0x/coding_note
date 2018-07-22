import tkinter as tk

win = tk.Tk()
win.title("radix sort")
win.geometry('600x800')

txt = tk.Entry(win,width=60)
txt.pack()

def insert_end():
    usr_in = txt.get()
    data = usr_in.split(',')
    s = ''
    for e in data:
        # print(e)
        s += '{} --> {}'.format(e,bin(int(e))[2:].zfill(8)) + '\n'
    show.insert('end',s)
    times = 0
    while(times != 4):
        times += 1
        index00=0
        index01=0
        index10=0
        index11=0

        l00 = []
        l01 = []
        l10 = []
        l11 = []
        for e in data:
            tmp = e
            e = bin(int(e))[2:]
            e = e.zfill(8)
            print(times,"*times*"," ",e)
            if times == 1:
                e = e[-2:]
            else:
                e = e[-2*(times):-2*(times-1)]

            if e == "00" or e == "0":
                index00 += 1
                l00.append(tmp)
            elif e == "01" or e == "1":
                index01 += 1
                l01.append(tmp)
            elif e == "10":
                index10 += 1
                l10.append(tmp)
            elif e == "11":
                index11 += 1
                l11.append(tmp)
            else:
                print("im false" + e[-2:])

        show.insert('end','---------------counting-------------\n')
        show.insert('end','{} {}'.format("00",index00)+'\n')
        show.insert('end','{} {}'.format("01",index01)+'\n')
        show.insert('end','{} {}'.format("10",index10)+'\n')
        show.insert('end','{} {}'.format("11",index11)+'\n')
        # show.insert('end',data)
        show.insert('end','---------------sorting-------------\n')
        show.insert('end','00'+'   '+' '.join(l00)+'\n')
        show.insert('end','01'+'   '+' '.join(l01)+'\n')
        show.insert('end','10'+'   '+' '.join(l10)+'\n')
        show.insert('end','11'+'   '+' '.join(l11)+'\n')

        data = l00 + l01 + l10 + l11
        show.insert('end','\n'+' '.join(data)+'\n')
        del l00[:]
        del l01[:]
        del l10[:]
        del l11[:]

b2 = tk.Button(win,text="OK",command=insert_end)
b2.pack()

show = tk.Text(win,height=300)
show.pack()



win.mainloop()