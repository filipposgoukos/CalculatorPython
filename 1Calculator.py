from tkinter import*


def clear():
    global result
    result = ''
    var.set('')

def press(num):
    global result
    result = result + str(num)
    var.set(result)

def equalpress():
    try:
        global result
        total = str(eval(result))
        var.set(total)
        result = ''
    except:
        var.set('error')
        result = ''

def backspace():
    global result
    result = txt.get()[:-1]
    if result == "":
        result = ""
    var.set(result)

window = Tk()
var = StringVar()
result = ''
window.geometry("270x170")

window.title('Calculator')

txt = Entry(window,width=20, text = var)
txt.place(x=80, y=0)

btn1 = Button(window, text = '1', width = 5, command = lambda: press(1))
btn1.place(x=50, y=20)

btn2 = Button(window, text = '2', width = 5, command = lambda: press(2))
btn2.place(x=95, y=20)

btn3 = Button(window, text= '3', width = 5, command = lambda: press(3))
btn3.place(x=140, y=20)

btn4 = Button(window, text = '+', width = 5, command = lambda: press('+'))
btn4.place(x=185, y=20)

btn5 = Button(window, text = '4', width = 5, command = lambda: press(4))
btn5.place(x=50, y=45)

btn6 = Button(window, text = '5', width = 5, command = lambda: press(5))
btn6.place(x=95, y=45)

btn7 = Button(window, text = '6', width = 5, command = lambda: press(6))
btn7.place(x=140, y=45)

btn8 = Button(window, text = '-', width = 5, command = lambda: press('-'))
btn8.place(x=185, y=45)

btn9 = Button(window, text = '7', width = 5, command = lambda: press(7))
btn9.place(x=50, y=70)

btn10 = Button(window, text = '8', width = 5, command = lambda: press(8))
btn10.place(x=95, y=70)

btn11 = Button(window, text = '9', width = 5, command = lambda: press(9))
btn11.place(x=140, y=70)

btn12 = Button(window, text = 'x', width = 5, command = lambda: press("*"))
btn12.place(x=185, y=70)

btn13 = Button(window, text = '=', width = 5)
btn13.place(x=50, y=95)

btn14 = Button(window, text = '0', width = 5, command = lambda: press(0))
btn14.place(x=95, y=95)

btn15 = Button(window, text = ' clear ', width = 5, command = clear)
btn15.place(x=140, y=95)

btn16 = Button(window, text = ' / ', width = 5, command = lambda: press('/'))
btn16.place(x=185, y=95)

btn17 = Button(window, text = ' . ', width = 5, command = lambda: press('.'))
btn17.place(x=50, y=120)

btn18 = Button(window, text = '**', width = 5, command = lambda: press('**'))
btn18.place(x=95, y=120)

btn19 = Button(window, text = '(', width = 5, command = lambda: press('('))
btn19.place(x=140, y=120)

btn20 = Button(window, text = ')', width = 5, command = lambda: press(')'))
btn20.place(x=185, y=120)

btn21 = Button(window, text = '<-', width = 5, command = backspace)
btn21.place(x=230, y=20)


















































































































































window.mainloop()