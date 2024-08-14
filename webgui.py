import streamlit as st
import functions
todos = functions.get_todos()
def add_todos():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
# st.set_page_config(layout="wide")
st.title("To-do App")
st.subheader("This is my todo app")
st.write("This app will increase your <b>productivity</b>.", unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
st.text_input(label='',placeholder="Enter a todo...", key='new_todo', on_change=add_todos)


from PIL import Image
with st.expander("start camera"):
    cam_input = st.camera_input("camera")
if cam_input:
    img = Image.open(cam_input)
    # convert image to grayscale
    gray_img = img.convert("L")
    st.image(gray_img)