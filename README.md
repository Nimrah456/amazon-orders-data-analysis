# Amazon Orders Data Analysis Dashboard 📊

An interactive data analysis dashboard built with **Python, Pandas, Streamlit, and Altair** to explore Amazon order history and understand spending patterns.

The application allows users to upload their order-history data in CSV format, view spending statistics, analyze tax payments, and visualize daily spending trends.

## ✨ Features

- **CSV Upload:** Upload order-history data through an interactive interface.
- **Data Cleaning:** Clean monetary values and convert order dates into a usable format.
- **Spending Analysis:** Calculate total, average, median, minimum, and maximum spending.
- **Tax Analysis:** Calculate total tax paid and the ratio of tax to total spending.
- **Data Preview:** View the uploaded data directly in the dashboard.
- **Spending Visualization:** Explore daily spending trends using an interactive bar chart.
- **Date Validation:** Identify invalid order dates and exclude them from the spending chart.

## 🛠️ Technologies Used

- **Python** — Core programming language
- **Pandas** — Data processing, cleaning, and analysis
- **Streamlit** — Interactive web application
- **Altair** — Data visualization

## 📁 Project Structure

```text
amazon-orders-data-analysis/
│
├── app (1).py
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

Follow these steps to run the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/Nimrah456/amazon-orders-data-analysis.git
```

### 2. Navigate to the Project Directory

```bash
cd amazon-orders-data-analysis
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 4. Install the Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run "app (1).py"
```

The application will open in your browser. If it does not open automatically, follow the local URL displayed in the terminal.

## 📄 Input Data Requirements

Upload a CSV file containing Amazon order-history data.

The application requires the following column names:

| Column | Description |
|---|---|
| `Total Charged` | Total amount charged for an order |
| `Tax Charged` | Tax amount charged for an order |
| `Order Date` | Date associated with the order |

**Important:** The column names must match the names above. Monetary values can contain dollar signs and commas, which the application removes during data cleaning.

Use a CSV file containing these fields to ensure compatibility with the dashboard.

## 📈 Insights You Can Explore

The dashboard calculates and displays:

- Total spending across the uploaded orders
- Average spending per record
- Median spending per record
- Highest and lowest spending values
- Total tax paid
- Tax-to-spending ratio
- Daily spending trends over time

These metrics can help users explore their purchasing patterns and better understand their order history.

## 🎯 Project Objectives

This project was developed to gain practical experience in:

- Processing real-world tabular data
- Cleaning and transforming data with Pandas
- Calculating descriptive statistics
- Creating interactive data visualizations
- Building a simple data-driven web application
- Presenting raw data in a user-friendly format

## 🔮 Future Improvements

Potential enhancements include:

- Adding monthly, quarterly, and yearly spending summaries
- Introducing filters for dates and spending ranges
- Comparing spending across product categories
- Adding downloadable reports and visualizations
- Improving the dashboard layout and user experience

## 🔒 Data Privacy

Use sample or anonymized order-history data when sharing screenshots or demonstrating the application publicly. Avoid uploading personal order information to public repositories.

## 👩‍💻 Author

**Nimrah Noor**

GitHub: [Nimrah456](https://github.com/Nimrah456)

---

⭐ If you find this project useful, feel free to explore the repository and share feedback.
