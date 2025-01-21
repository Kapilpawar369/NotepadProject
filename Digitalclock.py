import tkinter as tk #iska mtlb h ki hum tkinter module to tk ki trh use kr skte h hmre program me 
from time import strftime #strftime ek function jisko humm direct use kr skte aur iski help se hum time aur date ko apne hisaab se adjust kr skte h
root=tk.Tk() #ab hum ek root window bnayenge tkinter module ki help se root window hamre program ka main window jisme hum hmre elements ko display krenge yha humne root nam ka ek object create kiya tkinter class se
root.title("Digital Clock") #fir  hum root window ka title set krenge title vo h jo ki upr dikahi deta h
def time(): # ab hum ek function define krenge jo ki time and date ko update krenga aur lable me dispaly krenga aur lable vo elment h jo image aur text ko show krta h
    string=strftime("%H:%M:%S %p \n %D") #ab hum ek string variable banayenge jo ki strftime function se current time aur date ko forwaerd krenga strftimw function mw hum (%H=,%M,%S,%P=am/pm,%D=date,%Y)
    label.config(text=string) # yha humne label object ke config meth0d se text attribute ko string variable se assign krenge
    label.after(1000,time) #fir hum label object ka after method se time function ko 1000 milisecond bar fir se call krenge isse hamra time function her second update hota rhenga aur label me current time and date dikhaynga

label=tk.Label(root,font=('calibri',50,'bold'),background='yellow',foreground='black')
label.pack(anchor='center') #isse hum label object ko root window me place kr rhe h hum is methid me anchor attribute ko center string se assign kr rhe h jo ki label object ko window me centre me allign krenga
time() #call time function
root.mainloop() #fir hum rooot window ko mainloop method se run krenge mainloop method tkinter module ka ek method h jo ki window ko loop mw rkhta h  aur user input ka wait krta h
