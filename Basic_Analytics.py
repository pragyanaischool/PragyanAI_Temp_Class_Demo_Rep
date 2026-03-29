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

# -----------------------------
# KPIs
# -----------------------------
st.subheader(" Key Metrics")

col1, col2, col3, col4 = st.columns(4)

total_students = len(df)
conversion_rate = df["Converted"].mean() * 100
avg_price = df["Final_Price"].mean()
total_revenue = df["Revenue"].sum()

col1.metric("Total Students", total_students)
col2.metric("Conversion Rate (%)", f"{conversion_rate:.2f}")
col3.metric("Avg Final Price", f"₹{avg_price:,.0f}")
col4.metric("Total Revenue", f"₹{total_revenue:,.0f}")
