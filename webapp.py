import streamlit as st


# Streamlit location:  https://darrellajenkins-todostlit-webapp-oukbnt.streamlit.app/


def get():
    """For specific use with the web based todo app."""
    with open('webtodos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write(todos_arg):
    """For specific use with the web based todo app."""
    with open('webtodos.txt', 'w') as file:
        file.writelines(todos_arg)
    return todos_arg


def add_todo():
    task = st.session_state["add_todo"] + "\n"
    todos.append(task)
    write(todos)
    st.session_state["add_todo"] = ""


todos = get()
st.title("My TODO App")
st.subheader("A fun, easy way to track your tasks!")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Enter a task:", placeholder="Which task do you need to focus on today?",
              on_change=add_todo, key="add_todo")
