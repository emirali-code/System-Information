import tkinter as tk
import platform


first="Sistem   :" ,platform.system()
second="İsim   :", platform.node()
three="İşletim Sistemi   :", platform.platform()
four="İşlemci   :" ,platform.processor()
five="Bit   :" ,platform.machine()
six="Genel   :" ,platform.uname()

i=tk.Tk()
i.configure(background='gray')
i.title("Sistem Bilgisi")
greet = tk.Label(i,text=("--------------------------------"),bg='gray',fg='Navy blue',font='20')
greet.pack(side='bottom')
greet = tk.Label(i,text=(first),fg='green',bg='gray',font='20')
greet.pack()
greet = tk.Label(i,text=(second),fg='black',bg='gray',font='10')
greet.pack()
greet = tk.Label(i,text=(three),fg='black',bg='gray',font='10')
greet.pack()
greet = tk.Label(i,text=(four),fg='black',bg='gray',font='10')
greet.pack()
greet = tk.Label(i,text=(five),fg='black',bg='gray',font='10')
greet.pack()
greet = tk.Label(i,text=(six),fg='black',bg='gray',font='10')
greet.pack()
greet = tk.Label(i,text=("""############"""),fg='red',bg='gray',font='20')
greet.pack(side='right')
greet = tk.Label(i,text=("""############"""),fg='red',bg='gray',font='20')
greet.pack(side='left')
greet = tk.Label(i,text=("""Powered by Emyounoone"""),bg='gray',fg='Navy blue',font='20')
greet.pack(side='bottom')


i.mainloop()


