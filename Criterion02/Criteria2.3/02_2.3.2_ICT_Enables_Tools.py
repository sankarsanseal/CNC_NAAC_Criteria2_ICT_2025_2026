import streamlit as st
import pandas as pd
from  sqlalchemy import text as sqltext 

from streamlit_gsheets import GSheetsConnection


st.header(f"Selected Department: {st.session_state.selected_department}")


# Create a connection object.
conn_gsheet = st.connection("gsheets", type=GSheetsConnection)

df_sheet = conn_gsheet.read(skiprows =  0,header=1)




# Initialize connection.
conn_neon = st.connection("neon", type="sql", )

# Perform query.
df_neon = conn_neon.query(
                    'SELECT * FROM ict_2025_2026 where name_of_dept= :dept;', 
                    params={'dept': st.session_state.selected_department}, 
                    ttl="1"
                )



ict_data_dict = {}

# Print results.

container_ict_count = st.container(border = True)


col1, col2, col3 = container_ict_count.columns(3, gap="small")

selected_row = None

col1.text("Session 2024-2025",)

row = df_sheet.loc[df_sheet["Name of the Department"] == st.session_state.selected_department]




if st.session_state.selected_department is not None:
    selected_row = row

    selected_row.reset_index()


    for i, col in enumerate(df_sheet.columns, start = 1):
        col1.text(f"{col}: {selected_row.iloc[0][col]}",)
        # st.session_state[f"col1_{col.replace(" ", "_")}"] = selected_row.iloc[0][col]


col3.text("Session 2025-2026",)


data_submit_form = col3.form(key = "save_ict_detials")


checked_status = col2.checkbox(
    "First load data of session 2025-2026 session if not available then load the data from previous year",
    key="checkbox_2025_2026",
    value = False if selected_row is None else None,
    wrap = True,
)

if checked_status:

    if len(df_neon) == 1 :
        for i, (col, sql_col) in enumerate(zip(df_sheet.columns, df_neon.columns)): 
            col_name = col.replace(" ", "_").replace("?","_").replace(",","_")
            ict_data_dict[col]=data_submit_form.text_input(
                            f"{col}", 
                            value = df_neon.loc[0][sql_col], 
                            key = f"col3_{col_name}_checked_but_sql", 
                            required = True
                            )
    else:
        for i, col in enumerate(df_sheet.columns):
            col_name = col.replace(" ", "_").replace("?","_").replace(",","_")
            ict_data_dict[col]=data_submit_form.text_input(
                            f"{col}", 
                            value =  str(selected_row.iloc[0][col]) if selected_row is not None else None, 
                            key = f"col3_{col_name}_checked_but_gsheet",
                            required = True
                            )

else:
    for i, col in enumerate(df_sheet.columns):
        col_name = col.replace(" ", "_").replace("?","_").replace(",","_")
        if i == 0:
            ict_data_dict[col]=data_submit_form.text_input(
                            f"{col}", 
                            value = selected_row.iloc[0][col] if selected_row is not None else None, 
                            key = f"col3_{col_name}_unchecked" if selected_row is not None else f"col3_{col_name}_unchecked_none_department",
                            required = True
                            )
        else:
            ict_data_dict[col]=data_submit_form.text_input(
                            f"{col}", 
                            value =  None, 
                            key = f"col3_{col_name}_unchecked",
                            required = True,
                            )




form_submitted = data_submit_form.form_submit_button(label = "Update ICT details of 2025-2026 session",)

if form_submitted:
    # st.write(ict_data_dict)
    if len(df_neon) == 0:
        st.write("No rows yet.")
        try:
            # Open a transactional session block (Handles auto-commits/rollbacks)
            with conn_neon.session as session:
                # The SQL insert statement string wrapping parameterized keys
                insert_query = sqltext(
                    """INSERT INTO ICT_2025_2026 (
                    name_of_dept, 
                    no_of_desktop, 
                    no_of_laptops, 
                    no_of_printer, 
                    is_there_computer_lab, 
                    no_of_projector_or_screen, 
                    no_of_desktops_with_lan, 
                    no_of_smartboards, 
                    no_of_halls_with_ICT
                    ) 
                    VALUES (
                    :name_of_dept, 
                    :no_of_desktop,
                    :no_of_laptops,
                    :no_of_printer, 
                    :is_there_computer_lab, 
                    :no_of_projector_or_screen, 
                    :no_of_desktops_with_lan, 
                    :no_of_smartboards, 
                    :no_of_halls_with_ICT
                    );"""
                )
                
                # Execute query passing parameters securely inside a dictionary mapping
                session.execute(
                    insert_query, 
                    params={  
                        "name_of_dept" : ict_data_dict["Name of the Department"], 
                    "no_of_desktop" : ict_data_dict["Number of Desktops"],
                    "no_of_laptops" : ict_data_dict["Number of Laptops"],
                    "no_of_printer" : ict_data_dict["Number of Printers"], 
                    "is_there_computer_lab" : ict_data_dict["Does your department have a computer lab? If yes, mention the number of available computers"], 
                    "no_of_projector_or_screen" : ict_data_dict["Number of Projectors and Screens"], 
                    "no_of_desktops_with_lan" : ict_data_dict["Number of Desktops with LAN facility"], 
                    "no_of_smartboards" : ict_data_dict["Number of Smartboards"], 
                    "no_of_halls_with_ICT" : ict_data_dict["Number of Seminar Halls with ICT"]
                    }
                )
                
                # Explicitly commit changes to the remote Neon cloud instance
                session.commit()
                
            st.success(f"Successfully added for {ict_data_dict["Name of the Department"]} for the session 2025-2026")
            
        except Exception as e:
            st.error(f"Database insertion failed: {e}")

    elif len(df_neon) == 1:
        try:
            # Open a transactional session block (Handles auto-commits/rollbacks)
            with conn_neon.session as session:
                # The SQL insert statement string wrapping parameterized keys
                update_query = sqltext(
                    """UPDATE ICT_2025_2026 SET 
                    no_of_desktop = :no_of_desktop, 
                    no_of_laptops = :no_of_laptops , 
                    no_of_printer = :no_of_printer , 
                    is_there_computer_lab = :is_there_computer_lab , 
                    no_of_projector_or_screen = :no_of_projector_or_screen , 
                    no_of_desktops_with_lan = :no_of_desktops_with_lan , 
                    no_of_smartboards = :no_of_smartboards , 
                    no_of_halls_with_ICT = :no_of_halls_with_ICT 
                    WHERE name_of_dept = :name_of_dept;"""
                )
                
                # Execute query passing parameters securely inside a dictionary mapping
                session.execute(
                    update_query, 
                    params={  
                        "name_of_dept" : ict_data_dict["Name of the Department"], 
                    "no_of_desktop" : ict_data_dict["Number of Desktops"],
                    "no_of_laptops" : ict_data_dict["Number of Laptops"],
                    "no_of_printer" : ict_data_dict["Number of Printers"], 
                    "is_there_computer_lab" : ict_data_dict["Does your department have a computer lab? If yes, mention the number of available computers"], 
                    "no_of_projector_or_screen" : ict_data_dict["Number of Projectors and Screens"], 
                    "no_of_desktops_with_lan" : ict_data_dict["Number of Desktops with LAN facility"], 
                    "no_of_smartboards" : ict_data_dict["Number of Smartboards"], 
                    "no_of_halls_with_ICT" : ict_data_dict["Number of Seminar Halls with ICT"]
                    }
                )
                
                # Explicitly commit changes to the remote Neon cloud instance
                session.commit()
                
            st.success(f"Successfully updated for {ict_data_dict["Name of the Department"]} for the session 2025-2026")
            
        except Exception as e:
            st.error(f"Database insertion failed: {e}")

    else:
        st.error("There are duplicate rows.")
#     name_of_dept VARCHAR,
#   no_of_desktop VARCHAR,
#   no_of_laptops VARCHAR,
#   no_of_printer VARCHAR,
#   is_there_computer_lab VARCHAR,
#   no_of_projector_or_screen VARCHAR,
#   no_of_desktops_with_lan VARCHAR,
#   no_of_smartboards VARCHAR,
#   no_of_halls_with_ICT VARCHAR, 


 



