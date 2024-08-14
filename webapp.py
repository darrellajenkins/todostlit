import streamlit as st
import web_funcs


def add_todo():
	task = st.session_state["add_todo"] + "\n"
	todos.append(task)
	web_funcs.write(todos)
	st.session_state["add_todo"] = ""  # Clear the input field - added by Claude.


todos = web_funcs.get()
st.title("My TODO App")
st.subheader("A fun, easy way to track your tasks!")
# st.write("...")  # Example of additional function.
# st.checkbox("Study Python.")  # Example of additional function.

for index, todo in enumerate(todos):
	checkbox = st.checkbox(todo, key=todo)
	if checkbox:
		todos.pop(index)
		web_funcs.write(todos)
		del st.session_state[todo]
		st.rerun()


st.text_input(label="Enter a task:", placeholder="Which task do you need to focus on today?",
			  on_change=add_todo, key="add_todo")
