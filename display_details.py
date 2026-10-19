import streamlit as st
import pandas as pd
import os


PATH_TO_PREVIOUS_YEAR_EXCEL = os.path.join(os.path.abspath(__file__),'Departmental_Details_of_Computers_and_Other_Accessories_2024-2025.xlsx')


if os.path.exists(PATH_TO_PREVIOUS_YEAR_EXCEL):
    print(f"File exists: {PATH_TO_PREVIOUS_YEAR_EXCEL}")
else:
    raise FileNotFoundError(f"File not found: {PATH_TO_PREVIOUS_YEAR_EXCEL}")


