import functions
import FreeSimpleGUI as sg
label = sg.Text("Type in a to-do")
inputbox = sg.InputText(tooltip="Enter todo")
add = sg.Button("Add")
windo = sg.Window("TO-DO APP", layout=[[label], [inputbox, add]])
windo.read()
windo.close()
