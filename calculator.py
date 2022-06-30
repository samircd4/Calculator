import PySimpleGUI as sg #import GUI module

# Design layout
sg.theme('DarkTeal9')
keypad = (4,2)
layout = [
    [sg.InputText(default_text="", size=(20,10), key=("input"))],
    [
    sg.Button("7", size=keypad, key=("7")),
    sg.Button("8", size=keypad, key=("8")),
    sg.Button("9", size=keypad, key=("9")),
    sg.Button("/", size=keypad, key=("/"))
    ],
    [
    sg.Button("4", size=keypad, key=("4")),
    sg.Button("5", size=keypad, key=("5")),
    sg.Button("6", size=keypad, key=("6")),
    sg.Button("x", size=keypad, key=("*"))    
    ],
    [
    sg.Button("1", size=keypad, key=("1")),
    sg.Button("2", size=keypad, key=("2")),
    sg.Button("3", size=keypad, key=("3")),
    sg.Button("-", size=keypad, key=("-"))
    ],
    [
    sg.Button(".", size=keypad, key=(".")),
    sg.Button("0", size=keypad, key=("0")),
    sg.Button("=", size=keypad, key=("=")),
    sg.Button("+", size=keypad, key=("+"))
    ]
]
window = sg.Window("Simple Calculator", layout=layout, resizable=False, font=('calibri', 20, 'bold'))
#Input Function
def update(inp):
    input_elem = window["input"]
    current_value = input_elem.get()
    input_elem.update(current_value + inp)
#Calculate Function
def calculate(inp):
    input_elem = window["input"]
    current_value = input_elem.get()
    try:
        ans = eval(current_value)
        input_elem.update(ans)
    except:
        input_elem.update("")


while True:
    inp, values = window.read()
    if inp == sg.WIN_CLOSED:
        # print("Window closed")
        break
    if inp in "123456789.0/*-+":
        update(inp)    
    if inp == "=":
        calculate(inp)
        

window.close()
