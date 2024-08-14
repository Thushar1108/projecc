import streamlit as st
import functions
todos = functions.get_todos()
def add_todos():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
st.title("To-do App")
st.subheader("This is my todo app")
st.write("This app will increase your efficiency!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
st.text_input(label='',placeholder="Enter a todo...", key='new_todo', on_change=add_todos)