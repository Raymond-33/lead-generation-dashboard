import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Lead Generation & Scoring Dashboard",
    layout="wide"
)

st.title("Lead Generation & Probability Scoring Tool")
st.write(
    "This dashboard helps identify and rank scientific and biotech professionals "
    "based on their likelihood to work with 3D in-vitro models."
)

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("lead_generation_full_dataset.csv")

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")

# Filter by Job Title
job_titles = st.sidebar.multiselect(
    "Select Job Title",
    options=sorted(df["Job Title"].unique())
)

# Filter by Funding Stage
funding_stages = st.sidebar.multiselect(
    "Select Funding Stage",
    options=sorted(df["Funding Stage"].unique())
)

# Filter by Biotech Hub
biotech_hub = st.sidebar.selectbox(
    "Biotech Hub Location",
    options=["All", "Yes", "No"]
)

# Score Range
score_range = st.sidebar.slider(
    "Propensity Score Range",
    min_value=0,
    max_value=100,
    value=(40, 75)
)

# Apply Filters
filtered_df = df.copy()

if job_titles:
    filtered_df = filtered_df[filtered_df["Job Title"].isin(job_titles)]

if funding_stages:
    filtered_df = filtered_df[filtered_df["Funding Stage"].isin(funding_stages)]

if biotech_hub != "All":
    filtered_df = filtered_df[filtered_df["Biotech Hub"] == biotech_hub]

filtered_df = filtered_df[
    (filtered_df["Propensity Score"] >= score_range[0]) &
    (filtered_df["Propensity Score"] <= score_range[1])
]

# Sort by Score (Descending)
filtered_df = filtered_df.sort_values(
    by="Propensity Score",
    ascending=False
).reset_index(drop=True)

# Recalculate Rank
filtered_df["Rank"] = filtered_df.index + 1

# Display Table
st.subheader("Ranked Lead List")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# Download Button
st.download_button(
    label="Download Filtered Data as CSV",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_leads.csv",
    mime="text/csv"
)

# Footer 
st.markdown("---")
st.caption(
    "Note: This is a prototype demo. Data used is sample/mock data for demonstration purposes only."
)
