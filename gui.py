import functions
import FreeSimpleGUI as sg
label = sg.Text("Type in a to-do")
inputbox = sg.InputText(tooltip="Enter todo",key="todo")
add = sg.Button("Add")
windo = sg.Window("TO-DO APP",
                  layout=[[label, inputbox, add]],
                  font=('Helvetica',20))
while True:
    event,value = windo.read()
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break


windo.close()
