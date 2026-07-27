# =========================================
# AMAZON ORDERS WEB APP
# =========================================
import pandas as pd
import altair as alt
import streamlit as st

st.title("Amazon Orders Data Analysis")

# --------- FILE UPLOAD ---------
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # --------- CHECK REQUIRED COLUMNS ---------
    required_cols = {"Total Charged", "Tax Charged", "Order Date"}
    missing = required_cols - set(df.columns)
    if missing:
        st.error(f"Missing expected column(s): {', '.join(missing)}")
        st.stop()

    # --------- CLEAN DATA (order matters) ---------
    for col in ["Total Charged", "Tax Charged"]:
        df[col] = (
            df[col].astype(str)
            .str.replace(r'[$,]', '', regex=True)
            .replace('', '0')
            .astype(float)
        )

    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

    # Fill remaining NaNs only in columns that aren't dates/money
    other_cols = df.columns.difference(["Order Date", "Total Charged", "Tax Charged"])
    df[other_cols] = df[other_cols].fillna(0)

    # Drop rows where the date failed to parse (can't be grouped/plotted)
    n_bad_dates = df["Order Date"].isna().sum()
    if n_bad_dates:
        st.warning(f"{n_bad_dates} row(s) had an unreadable Order Date and were excluded from the date chart.")

    # --------- SHOW DATA ---------
    st.subheader("Data Preview")
    st.write(df)

    # --------- METRICS ---------
    st.subheader("Statistics")

    total_charged = df["Total Charged"].sum()
    total_tax = df["Tax Charged"].sum()

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Spending", f"${total_charged:,.2f}")
        st.metric("Average Spending", f"${df['Total Charged'].mean():,.2f}")
        st.metric("Median Spending", f"${df['Total Charged'].median():,.2f}")
    with col2:
        st.metric("Max Spending", f"${df['Total Charged'].max():,.2f}")
        st.metric("Min Spending", f"${df['Total Charged'].min():,.2f}")
        st.metric("Total Tax Paid", f"${total_tax:,.2f}")

    if total_charged != 0:
        st.write("Tax Ratio:", round(total_tax / total_charged, 4))
    else:
        st.write("Tax Ratio: N/A (total charged is $0)")

    # --------- GROUP DATA ---------
    daily_totals = (
        df.dropna(subset=["Order Date"])
        .groupby(df["Order Date"].dt.date)["Total Charged"]
        .sum()
        .reset_index()
    )
    daily_totals.columns = ["Order Date", "Total Charged"]

    # --------- PLOT (Altair — pure JS rendering, no native DLLs) ---------
    st.subheader("Total Charged Over Time")

    bars = alt.Chart(daily_totals).mark_bar().encode(
        x=alt.X("Order Date:T", title="Date"),
        y=alt.Y("Total Charged:Q", title="Total Charged ($)"),
        tooltip=["Order Date:T", "Total Charged:Q"],
    )

    labels = bars.mark_text(dy=-8, fontSize=10).encode(
        text=alt.Text("Total Charged:Q", format=".2f")
    )

    st.altair_chart((bars + labels).properties(height=450), use_container_width=True)
