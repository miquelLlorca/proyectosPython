import os
import pandas as pd
import streamlit as st
from streamlit_extras import dataframe_explorer


def execute_code(code, params=None):
    try:
        local_vars = {}
        global_vars = {}
        if params:
            global_vars.update(params)
        exec(code, global_vars, local_vars)
    except Exception as e:
        st.error(f"An error occurred: {e}")
        
ORDER = "Order in the DSM-5"
CHAPTER = "DSM-5 Chapter	DSM-5 Disorder"
SYMPTOM_TXT = "Constituent symptom (wording from DSM-5)"
SYMPTOM_ID = "Unique symptom number (index for duplicate symptoms; sort by this column to see the groups of symptoms that have been coded as redundant)"
SPECIFIER = "Specifier ( 0 = primary diagnosis, 1 = specifier)"
REPEATS = "Repeats at all (0 = no, 1 = yes)"
REPEATS_IN_CHAPTER = "Repeats within a chapter (0=no, 1=yes)"
N_DIAGNOSIS = "Number of diagnoses symptom appears in (count)"
REPEATS_BETWEEN_CHAPTERS = "Repeats between chapters (0=no, 1=yes)"
N_CHAPERS = "Number of chapters symptom appears in (count)"      
        
keys = {
    "ORDER": ORDER,
    "CHAPTER": CHAPTER,
    "SYMPTOM_TXT": SYMPTOM_TXT,
    "SYMPTOM_ID": SYMPTOM_ID,
    "SPECIFIER": SPECIFIER,
    "REPEATS": REPEATS,
    "REPEATS_IN_CHAPTER": REPEATS_IN_CHAPTER,
    "N_DIAGNOSIS": N_DIAGNOSIS,
    "REPEATS_BETWEEN_CHAPTERS": REPEATS_BETWEEN_CHAPTERS,
    "N_CHAPERS": N_CHAPERS
}

##########################################################################################################################################################################
##########################################################################################################################################################################
##########################################################################################################################################################################

st.set_page_config(layout="wide")


df = pd.read_excel("data.xlsx")


filtered_df = dataframe_explorer.dataframe_explorer(df, case=False)
st.dataframe(filtered_df, use_container_width=True)

st.text(keys.keys())
st.text("")

# Text area for users to input code
code = st.text_area("Enter your Python code here:")


params = {
    "filtered_df": filtered_df,
    "df": df
}

# Button to execute the code
if st.button("Execute"):
    execute_code(code, {**params, **keys})
    
# st.dataframe(filtered_df, use_container_width=True)
