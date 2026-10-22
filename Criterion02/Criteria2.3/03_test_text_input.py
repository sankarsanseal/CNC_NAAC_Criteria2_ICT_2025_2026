import streamlit as st


container1 = st.container(border = True,)

checked = container1.checkbox("click here", value = False, key ="checkbox1")

st.write(st.session_state.selected_department)



if checked:
    container1.text_input("Testing the text input", value = st.session_state.selected_department, key = "text_input_if")

else:
    container1.text_input("Testing the text input", value = "else Changed", key = "text_input_else")
    container1.text_input("Testing the text input", value = st.session_state["selected_department"], key = "text_input1")
