import functions
import FreeSimpleGUI as sg
import time
sg.theme("DarkBlack")
clock = sg.Text('',key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo",key="todo")
# key assigns the key of value for dict that will be created,stored eg {todo: input}
add = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),key="todos",
                      enable_events=True, size = [45,10])
edit = sg.Button("Edit")
Complete = sg.Button("Complete")
exit = sg.Button("Exit")
# button_labels = ["Close", "Apply"]
# layout = []
# for bl in button_labels:
#    layout.append([sg.Button(bl)])
# above cmds for auto generating these options

window = sg.Window("TO-DO APP",
            layout = [[clock], [label], [input_box, add], [list_box, edit,Complete], [exit]],
                  font = ('Helvetica',20))
while True:
    event,value = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))


    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = value['todos'][0]
                new_todo = value['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Select an item first!",font=("Helvetica", 20) )

        case "Complete":
            try:
                todo_to_complete = value['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("select an item first!", font=("Helvetica", 20))
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break


window.close()
