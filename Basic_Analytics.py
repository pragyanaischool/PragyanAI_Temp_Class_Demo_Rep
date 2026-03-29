import streamlit as st # for Streamlit UI
import pandas as pd # Pandas - Data Processing
import io # Buffer and others
import matplotlib.pyplot as plt # Creating and Displaying Plots - Charts - Fig
import seaborn as sns # Creating and Displaying Plots - Charts - Fig
# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="PragyanAI Student Program Pricing Analytics Dashboard", layout="wide")
# -----------------------------
# Title
# -----------------------------
st.title("PragyanAI Student Program Pricing & Scholarship Analytics Dashboard")

st.write("Analyze pricing, discounts, and student conversion behavior.") # Print

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/student_PRICING_SCHOLARSHIP_Analysis_Project_12.csv")
    return df

df = load_data()

# -----------------------------
# Show Data
# -----------------------------
st.subheader("Dataset Preview")
st.dataframe(df.head()) # Display the Sample View of Data

st.write("Basic Info about Data")
buffer = io.StringIO()
df.info(buf=buffer)
st.text(buffer.getvalue()) # Print Text Data
