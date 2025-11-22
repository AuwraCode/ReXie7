import streamlit as st
from pathlib import Path
import pandas as pd

#Import modules
from src.data_loader import load_raw_data, save_processed_data
from src.preprocessing import clean_price_data, filter_target_car, encode_categorical_features

#Website configuration
st.set_page_config(page_title="JDM Price Forecaster", page_icon="🚗")

#Header
st.title("🇯🇵 JDM Price Forecaster")
st.write("Select your dream car to prepare data for AI analysis")

#Loading data
#Using cache for performance 
@st.cache_data
def get_data():
    project_root = Path.cwd()
    raw_data_path = project_root / 'data' / 'raw' / 'cars_datasets.csv'

    if not raw_data_path.exists():
        return None

    df = load_raw_data(raw_data_path)
    df = clean_price_data(df)
    return df

df = get_data()

if df is None:
    st.error("Error: No data in folder data/raw/!")
    st.stop()

#User Interface (Sidebar)
st.sidebar.header("⚙️ Configuration")

#A. Mark selection
available_marks = df["mark"].value_counts().index.tolist()
selected_mark = st.sidebar.selectbox("Select brand:", available_marks)

#B. Model selection
mark_mask = df["mark"] == selected_mark
available_models = df[mark_mask]["model"].value_counts().index.tolist()

selected_model = st.sidebar.selectbox("Select model:", available_models)

#Main window
st.subheader(f"Selected: {selected_mark.upper()} {selected_model.upper()}")

#Filtering 
df_target = filter_target_car(df, selected_mark, selected_model)

#Showing statistics (Metric)
col1, col2, col3 = st.columns(3)
col1.metric("Offer count", len(df_target))
col2.metric("Average price", f"{int(df_target['price'].mean() * 1000):,} JPY")
col3.metric("Average mileage", f"{int(df_target['mileage'].mean())}km")

#Table preview
st.dataframe(df_target.head(), hide_index= True)

#Save button
if st.button("💾 Save data for AI training"):
    project_root = Path.cwd()

    #Encoding
    df_ready_for_ai = encode_categorical_features(df_target)

    #Define file name
    filename = f"processed_{selected_mark}_{selected_model}.csv"
    save_path = project_root / 'data' / 'processed' / filename

    #Saving encoded version
    save_processed_data(df_target, save_path)
    st.success(f"Done! File saved as: {filename}")

    #Preview
    st.write("Preview of data sent to AI")
    st.dataframe(df_ready_for_ai.head(), hide_index= True)