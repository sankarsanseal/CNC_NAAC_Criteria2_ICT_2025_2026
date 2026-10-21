import streamlit as st
import pandas as pd
import os

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
                    ttl="10m"
                )

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
        st.session_state[f"col1_{col}"] = selected_row.iloc[0][col]


col3.text("Session 2025-2026",)


checked_status = col2.checkbox(
    "Copy from previous year",
    key="checkbox_2025_2026",
)

if checked_status:
    if len(df_neon) == 1 :
        for i, col, value in enumerate(zip(df_sheet.columns, df_neon.itertuples()), start = 1):
            col3.text_area(f"{col}", value = str(value), key = f"col3_{col.replace(" ", "_")}", )
    else:
        for i, col in enumerate(df_sheet.columns):
            col3.text_input(f"{col}", value =  str(selected_row.iloc[0][col]) if selected_row is not None else None, key = f"col3_{col.replace(" ", "_")}")

else:
    for i, col in enumerate(df_sheet.columns):
        if i == 0:
            col3.text_input(f"{col}", value = str(selected_row.iloc[0][col]) if selected_row is not None else None, key = f"col3_{col.replace(" " , "_")}")
        else:
            col3.text_input(f"{col}", value =  None, key = f"col3_{col.replace(" ", "_")}")
 



