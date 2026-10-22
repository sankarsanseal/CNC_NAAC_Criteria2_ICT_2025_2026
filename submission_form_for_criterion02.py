import streamlit as st

@st.cache_data
def list_of_departments():
    return { "Bengali": ["Department of Bengali (UG and PG)", "Arts"], # Arts
             "Botany" : ["Department of Botany", "Science"],
             "Chemistry" : ["Department of Chemistry", "Science"],
             "Commerce" :["Department of Commerce", "Commerce"],
             "Computer Science" : ["Department of Computer Science", "Science"],
             "Economics": ["Department of Economics", "Arts"], # Arts
             "Education": ["Department of Education", "Arts"], #
             "English" : ["Department of English", "Arts"],
             "Environmental Science" : ["Department of Environmental Science", "Science"],
             "French" : ["Department of French (UG and PG)", "Arts"],
             "Geography" : ["Department of Geography (UG and PG)", "Arts"],
             "History" : ["Department of History", "Arts"],
             "Mathematics": ["Department of Mathematics", "Science"],
             "Philosophy" : ["Department of Philosophy", "Arts"],
             "Physics" : ["Department of Physics", "Science"],
             "Political Science" : ["Department of Political Science", "Arts"],
             "Sanskrit" :["Department of Sanskrit", "Arts"],
             "Sociology" : ["Department of Sociology", "Arts"],
             "Zoology" : ["Depatment of Zoology", "Science"],
            
            }


st.set_page_config(page_title = "Criterion 2 related document submission portal", layout = "wide")


selected_department = st.sidebar.selectbox("**Select the Department Name from the following dropdown**", 
                                   list_of_departments().keys(), 
                                   persist_state = "session", 
                                   key = "selected_department",
                                   placeholder = "Choose the department",
                                   index = None)

# st.session_state["selected_department"] = selected_department 


page_2_2_1 = st.Page("Criterion02/Criteria2.2/01_2.2.1_Programmes_For_Advanced_And_Slow_Learners.py", 
                     title = '2.2.1 Programmes for Advanced and Slower Learners', default = False)
page_2_3_1 = st.Page("Criterion02/Criteria2.3/01_2.3.1_Problem_Solving_Methodologies.py", 
                     title = "2.3.1 Student centric Problem Solving Methodologies")
page_2_3_2 = st.Page("Criterion02/Criteria2.3/02_2.3.2_ICT_Enables_Tools.py", title = "2.3.2 ICT Enabled Tools")
# page_2_3_3 = st.Page("Criterion02/Criteria2.3/03_test_text_input.py", title = "Text Input Testing")
page_2_5_1 = st.Page("Criterion02/Criteria2.5/01_2.5.1_Internal_Assessment_Details.py", 
                     title = "2.5.1 Internal Assessment related Questions and Attendance")

# landing_page = st.navigation([page_2_2_1, page_2_3_1, page_2_5_1]) 

landing_page = st.navigation(
    {
        "Criteria 2.2" : [page_2_2_1],
        "Criteria 2.3" : [
                            page_2_3_1, 
                            page_2_3_2, 
                            # page_2_3_3
                            ],
        "Criteria 2.5" : [page_2_5_1],
    }, expanded = True
)


landing_page.run()

# st.session_state["selected_department"] = selected_department 