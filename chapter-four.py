import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="☕ Chai Sales Dashboard",
    page_icon="☕",
    layout="wide"
)

# ---------------- DARK THEME ----------------
st.markdown("""
<style>
.stApp {
    background-color: #0F172A;
    color: white;
}

h1 {
    color: #38BDF8;
    text-align: center;
}

h2, h3 {
    color: white;
}

div[data-testid="stFileUploader"] {
    background-color: #1E293B;
    padding: 10px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown(
    "<h1>☕ Chai Sales Dashboard</h1>",
    unsafe_allow_html=True
)

st.write("Upload your CSV file and explore chai sales insights.")

# ---------------- FILE UPLOAD ----------------
file = st.file_uploader(
    "📂 Upload CSV File",
    type=["csv"]
)

if file:

    # Read CSV
    df = pd.read_csv(file)

    # ---------------- DATA PREVIEW ----------------
    st.subheader("📋 Data Preview")
    st.dataframe(df, use_container_width=True)

    # ---------------- SUMMARY ----------------
    st.subheader("📊 Summary Statistics")
    st.dataframe(df.describe(), use_container_width=True)

    # ---------------- FILTER ----------------
    st.subheader("🏙️ Filter by City")

    cities = df["City"].unique()

    selected_city = st.selectbox(
        "Select City",
        cities
    )

    filtered_data = df[df["City"] == selected_city]

    st.subheader(f"📍 Data for {selected_city}")
    st.dataframe(filtered_data, use_container_width=True)

    # ---------------- KPI CARDS ----------------
    st.subheader("🚀 Key Performance Indicators")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div style="
        background:#2563EB;
        padding:20px;
        border-radius:15px;
        text-align:center;">
            <h3>☕ Total Cups Sold</h3>
            <h1>{filtered_data['Cups_Sold'].sum()}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="
        background:#16A34A;
        padding:20px;
        border-radius:15px;
        text-align:center;">
            <h3>💰 Total Revenue</h3>
            <h1>₹{filtered_data['Revenue'].sum():,.0f}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style="
        background:#DC2626;
        padding:20px;
        border-radius:15px;
        text-align:center;">
            <h3>📈 Avg Revenue</h3>
            <h1>₹{filtered_data['Revenue'].mean():,.0f}</h1>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ---------------- REVENUE TREND ----------------
    st.subheader("📈 Revenue Trend")

    revenue_chart = (
        filtered_data
        .groupby("Date")["Revenue"]
        .sum()
    )

    st.line_chart(revenue_chart)

    # ---------------- CUPS SOLD ----------------
    st.subheader("☕ Cups Sold Trend")

    cups_chart = (
        filtered_data
        .groupby("Date")["Cups_Sold"]
        .sum()
    )

    st.bar_chart(cups_chart)

    # ---------------- CHAI DISTRIBUTION ----------------
    st.subheader("🥧 Chai Type Distribution")

    chai_distribution = (
        filtered_data["Chai_Type"]
        .value_counts()
    )

    st.bar_chart(chai_distribution)

    # ---------------- REVENUE BY CHAI ----------------
    st.subheader("💸 Revenue by Chai Type")

    revenue_by_chai = (
        filtered_data
        .groupby("Chai_Type")["Revenue"]
        .sum()
    )

    st.bar_chart(revenue_by_chai)

    # ---------------- TOP SELLING CHAI ----------------
    st.subheader("🏆 Top Selling Chai")

    top_chai = (
        filtered_data
        .groupby("Chai_Type")["Cups_Sold"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    st.dataframe(
        top_chai,
        use_container_width=True
    )

    # ---------------- FOOTER ----------------
    st.markdown("---")
    st.markdown(
        "<h4 style='text-align:center;color:#94A3B8;'>☕ Chai Sales Analytics Dashboard</h4>",
        unsafe_allow_html=True
    )

else:
    st.info("👆 Upload a CSV file to start analysis.")