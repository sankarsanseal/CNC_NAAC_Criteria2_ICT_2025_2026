import streamlit as st
import pandas as pd
import os


PATH_TO_PREVIOUS_YEAR_EXCEL = os.path.join(os.path.dirname(os.path.abspath(__file__)),'Departmental_Details_of_Computers_and_Other_Accessories_2024-2025.xlsx')

PATH_TO_NEXT_YEAR_EXCEL = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'Departmental_Details_of_Computers_and_Other_Accessories_2025_2026.xlsx')


if os.path.exists(PATH_TO_PREVIOUS_YEAR_EXCEL):
    print(f"File exists: {PATH_TO_PREVIOUS_YEAR_EXCEL}")
else:
    raise FileNotFoundError(f"File not found: {PATH_TO_PREVIOUS_YEAR_EXCEL}")



ict_departmental_df = pd.read_excel(PATH_TO_PREVIOUS_YEAR_EXCEL, 
                                    sheet_name='Table 1', 
                                    engine='openpyxl',
                                    skiprows=0,
                                    header=1
                                    )

ict_departmental_df = ict_departmental_df.sort_values(by='Name of the Department').reset_index(drop=True)

if os.path.exists(PATH_TO_NEXT_YEAR_EXCEL):
    new_ict_departmental_df = pd.read_excel(PATH_TO_NEXT_YEAR_EXCEL, 
                                    sheet_name='Table 1', 
                                    engine='openpyxl',
                                    skiprows=None,
                                    header=0
                                    )
    new_ict_departmental_df = new_ict_departmental_df.sort_values(by='Name of the Department').reset_index(drop=True)
else:
    new_ict_departmental_df = pd.DataFrame(columns=ict_departmental_df.columns)


new_ict_departmental_df[['Name of the Department']] = ict_departmental_df[['Name of the Department']].dropna().copy()

st.set_page_config(page_title="ICT Departmental Details", layout="wide")

selected_department = st.selectbox("Select Department", 
                options=ict_departmental_df['Name of the Department'].dropna().unique(), 
                key="department_select"
                )

st.write("Details of the year 2024-2025 for the selected department:")

st.dataframe(ict_departmental_df.loc[ict_departmental_df['Name of the Department'] 
                    == selected_department], hide_index=True, 
                    use_container_width=True
                    )


st.write("Details of the year 2025-2026 for the selected department:")

checkbox_prev_year = st.checkbox("The details are same as previous year", key="same_as_previous_year", value=True)

if checkbox_prev_year:
    new_ict_departmental_df[new_ict_departmental_df['Name of the Department'] == selected_department] = ict_departmental_df[ict_departmental_df['Name of the Department'] == selected_department]

else:
    new_ict_departmental_df.iloc[new_ict_departmental_df['Name of the Department'] == selected_department] = pd.Series([selected_department] +
                                                                        [None] * (len(new_ict_departmental_df.columns) - 1), 
                                                                        index = new_ict_departmental_df.columns,)
    

st.data_editor(new_ict_departmental_df.loc[new_ict_departmental_df['Name of the Department'] == selected_department], 
hide_index=True, 
                    use_container_width=True
                    )

st.table(new_ict_departmental_df)

with pd.ExcelWriter(PATH_TO_NEXT_YEAR_EXCEL, engine='openpyxl') as writer:
    new_ict_departmental_df.to_excel(writer, sheet_name="Table 1", index=False)

# new_ict_departmental_df.to_excel(
#     PATH_TO_NEXT_YEAR_EXCEL,
#     sheet_name="Table 1",
#     # index=False,
#  engine='openpyxl')
