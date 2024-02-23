import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("my todo app")
st.subheader("this is my todo app")
st.write("are you ready to increase your productivity")
for todo in todos:
    check_box = st.checkbox(todo,key=todo)#each todo has a different key
    if check_box:
        todos.remove(todo)
        functions.write_todos(todos)
        del st.session_state[todo] #delete also the todo from the session state dictionary
        st.experimental_rerun()#rerun the code to see the changes
st.text_input(label="",placeholder="add a todo .....",on_change=add_todo, key="new_todo")
#st.session_state