# Sales Analytics Dashboard Project

## 📊 Project Overview

This project demonstrates end-to-end data analytics capabilities using a popular Kaggle sales dataset. The project includes data cleaning, KPI definition, dashboard creation in both Tableau and Power BI, and actionable business insights.

**Dataset**: Superstore Sales Dataset (Kaggle)
- **Why this dataset**: One of the most popular datasets on Kaggle with 100K+ downloads, commonly used in real-world analytics portfolios, and provides comprehensive business metrics (sales, profit, regions, categories, customer segments).

## 🎯 Business Context

The Superstore dataset represents a retail business with operations across multiple regions, selling various product categories to different customer segments. This dataset is ideal for demonstrating:
- Sales performance analysis
- Profitability analysis
- Regional performance comparison
- Product category optimization
- Customer segment analysis
- Time-series trend analysis

## 📁 Project Structure

```
├── README.md                          # This file
├── data/
│   ├── raw/                          # Original dataset (download from Kaggle)
│   └── processed/                    # Cleaned and prepared data
├── notebooks/
│   └── data_cleaning.ipynb          # Data cleaning and preparation
├── scripts/
│   └── data_preparation.py          # Python script for data cleaning
├── documentation/
│   ├── 01_dataset_selection.md      # Dataset selection and understanding
│   ├── 02_data_cleaning.md          # Data cleaning steps
│   ├── 03_kpi_definitions.md        # KPI definitions and calculations
│   ├── 04_tableau_dashboard.md      # Tableau dashboard guide
│   ├── 05_powerbi_dashboard.md       # Power BI dashboard guide
│   └── 06_business_insights.md       # Business insights and recommendations
├── portfolio/
│   ├── resume_bullets.md            # Resume bullet points
│   └── interview_qa.md              # Interview questions and answers
└── requirements.txt                  # Python dependencies
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Tableau Desktop (for Tableau dashboard)
- Power BI Desktop (for Power BI dashboard)
- Kaggle account (for dataset download)

### Installation

1. Clone this repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the dataset:
   - Go to [Kaggle Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
   - Download `SampleSuperstore.csv`
   - Place it in `data/raw/` folder

4. Run data cleaning script:
   ```bash
   python scripts/data_preparation.py
   ```

## 📈 Key Features

- **Data Cleaning**: Comprehensive data preparation with missing value handling, duplicate removal, and calculated metrics
- **KPI Dashboard**: Real-time KPIs including Sales, Profit, Margin, Growth metrics
- **Interactive Visualizations**: Region, category, and time-based filters
- **Business Insights**: Actionable recommendations for pricing, inventory, and regional strategies
- **Dual Platform**: Implementations in both Tableau and Power BI

## 🛠️ Technologies Used

- **Python**: Data cleaning and preparation (Pandas, NumPy)
- **Tableau**: Interactive dashboard creation
- **Power BI**: Business intelligence dashboard with DAX measures
- **Excel/CSV**: Data storage and manipulation

## 📊 Dashboard Features

### KPIs Tracked
- Total Sales
- Total Profit
- Profit Margin %
- Sales Growth (MoM/YoY)
- Average Order Value
- Customer Retention Rate

### Visualizations
- Sales trend over time (Line chart)
- Category & Sub-category performance (Bar chart)
- Regional sales & profit (Map visualization)
- Top 10 products by sales
- Profit vs Loss analysis

## 📝 Documentation

See the `documentation/` folder for detailed guides on:
1. Dataset selection and understanding
2. Data cleaning methodology
3. KPI definitions and calculations
4. Tableau dashboard creation
5. Power BI dashboard creation
6. Business insights and recommendations

## 💼 Portfolio Materials

Check `portfolio/` folder for:
- Resume bullet points for Data Analyst roles
- Interview questions and answers based on this project

## 📄 License

This project is for educational and portfolio purposes.

## 👤 Author

Created as part of a comprehensive data analytics portfolio project.

---

**Note**: This project demonstrates real-world data analytics skills and is suitable for showcasing in job applications for Data Analyst, Business Analyst, and Business Intelligence roles.
