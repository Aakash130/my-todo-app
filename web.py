import streamlit as st
import functions  # Make sure you have this module with required functions

# Initialize session state for new todo
if 'new_todo' not in st.session_state:
    st.session_state['new_todo'] = ""

# Get todos from file
todos = functions.get_todo()

def add_todo():
    todo = st.session_state['new_todo']
    if todo.strip():  # Only add if not empty
        todos.append(todo + "\n")
        functions.write_todo(todos)
        st.session_state['new_todo'] = ""  # Clear input after adding

def complete_todo():
    # This function would handle completed todos
    pass  # You'll need to implement this based on your needs

st.title("My Todo App")
st.subheader("This is my todo App")

# Display todos with checkboxes
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:  # If checkbox is checked
        todos.pop(index)
        functions.write_todo(todos)
        st.rerun()  # Refresh to show updated list

# Add new todo input
st.text_input(label="",
              placeholder="Add new Todo...",
              on_change=add_todo,
              key='new_todo')