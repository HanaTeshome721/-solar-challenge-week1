import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from utils import load_data, get_combined_dataframe


try:
    st.set_page_config(page_title="Solar Dashboard", layout="wide")
    # Your actual app logic here
    st.title("Solar Dashboard")
    # e.g., load data, create plots, etc.

except Exception as e:
    st.error(f"An error occurred: {e}")
    st.exception(e)

# Load and prepare data
data_dict = load_data()
df = get_combined_dataframe(data_dict)

# Sidebar: Country and Metric Filters
st.sidebar.title("Filters")
available_countries = df["Country"].unique().tolist()
selected_countries = st.sidebar.multiselect("Select countries", available_countries, default=available_countries)

metrics = ["GHI", "DNI", "DHI"]
selected_metric = st.sidebar.selectbox("Select Metric", metrics)

# Filter Data
filtered_df = df[df["Country"].isin(selected_countries)]

st.title("☀️ Solar Radiation Dashboard")
st.markdown("### Explore solar radiation metrics (GHI, DNI, DHI) across selected countries.")

# Boxplot
st.subheader(f"📊 Boxplot of {selected_metric}")
fig, ax = plt.subplots()
sns.boxplot(data=filtered_df, x="Country", y=selected_metric, palette="Set2", ax=ax)
st.pyplot(fig)

# Summary Table
st.subheader(f"📋 Summary Table for {selected_metric}")
summary = (
    filtered_df.groupby("Country")[selected_metric]
    .agg(["mean", "median", "std"])
    .rename(columns={"mean": "Mean", "median": "Median", "std": "Std Dev"})
    .round(2)
)
st.dataframe(summary)

# Top Regions Table (if available)
if "Station" in df.columns:
    st.subheader(f"🏆 Top 5 Regions by {selected_metric}")
    top_regions = (
        filtered_df.groupby(["Country", "Station"])[selected_metric]
        .mean()
        .reset_index()
        .sort_values(by=selected_metric, ascending=False)
        .head(5)
    )
    st.table(top_regions)

# Bar Chart Ranking
st.subheader("📈 Average GHI by Country")
avg_ghi = (
    df.groupby("Country")["GHI"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

fig2, ax2 = plt.subplots()
sns.barplot(data=avg_ghi, x="Country", y="GHI", palette="coolwarm", ax=ax2)
ax2.set_title("Average GHI")
st.pyplot(fig2)

# Download filtered data
st.sidebar.download_button(
    label="📥 Download Filtered CSV",
    data=filtered_df.to_csv(index=False).encode(),
    file_name="filtered_solar_data.csv",
    mime="text/csv"
)
