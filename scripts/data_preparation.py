"""
Data Cleaning and Preparation Script for Superstore Sales Dataset
This script performs comprehensive data cleaning and creates calculated metrics.
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os

def load_data(file_path):
    """Load the Superstore dataset from CSV file."""
    try:
        df = pd.read_csv(file_path)
        print(f"✓ Data loaded successfully: {len(df)} rows, {len(df.columns)} columns")
        return df
    except FileNotFoundError:
        print(f"✗ Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"✗ Error loading data: {str(e)}")
        return None

def check_data_quality(df):
    """Perform initial data quality checks."""
    print("\n" + "="*50)
    print("DATA QUALITY CHECKS")
    print("="*50)
    
    # Check for missing values
    missing_values = df.isnull().sum()
    missing_percentage = (missing_values / len(df)) * 100
    missing_df = pd.DataFrame({
        'Column': missing_values.index,
        'Missing Count': missing_values.values,
        'Missing %': missing_percentage.values
    })
    missing_df = missing_df[missing_df['Missing Count'] > 0]
    
    if len(missing_df) > 0:
        print("\nMissing Values:")
        print(missing_df.to_string(index=False))
    else:
        print("\n✓ No missing values found")
    
    # Check for duplicates
    duplicate_count = df.duplicated().sum()
    print(f"\nDuplicate Rows: {duplicate_count}")
    if duplicate_count > 0:
        print("⚠ Warning: Duplicate rows found")
    else:
        print("✓ No duplicate rows")
    
    # Check data types
    print("\nData Types:")
    print(df.dtypes)
    
    # Check for negative sales/profit
    negative_sales = (df['Sales'] < 0).sum()
    negative_profit = (df['Profit'] < 0).sum()
    print(f"\nNegative Sales: {negative_sales} rows")
    print(f"Negative Profit: {negative_profit} rows")
    
    return df

def clean_data(df):
    """Perform data cleaning operations."""
    print("\n" + "="*50)
    print("DATA CLEANING")
    print("="*50)
    
    df_cleaned = df.copy()
    initial_rows = len(df_cleaned)
    
    # 1. Remove duplicates
    df_cleaned = df_cleaned.drop_duplicates()
    removed_duplicates = initial_rows - len(df_cleaned)
    if removed_duplicates > 0:
        print(f"✓ Removed {removed_duplicates} duplicate rows")
    
    # 2. Convert date columns to datetime
    date_columns = ['Order Date', 'Ship Date']
    for col in date_columns:
        if col in df_cleaned.columns:
            df_cleaned[col] = pd.to_datetime(df_cleaned[col], errors='coerce')
            print(f"✓ Converted {col} to datetime")
    
    # 3. Handle missing values in critical columns
    critical_columns = ['Order ID', 'Customer ID', 'Sales', 'Profit']
    for col in critical_columns:
        if col in df_cleaned.columns:
            missing_count = df_cleaned[col].isnull().sum()
            if missing_count > 0:
                df_cleaned = df_cleaned.dropna(subset=[col])
                print(f"✓ Removed {missing_count} rows with missing {col}")
    
    # 4. Ensure correct data types
    if 'Postal Code' in df_cleaned.columns:
        df_cleaned['Postal Code'] = df_cleaned['Postal Code'].astype(str)
    
    # 5. Standardize categorical values (trim whitespace, capitalize)
    categorical_columns = ['Region', 'Segment', 'Ship Mode', 'Category', 'Sub-Category']
    for col in categorical_columns:
        if col in df_cleaned.columns:
            df_cleaned[col] = df_cleaned[col].str.strip().str.title()
    
    print(f"\n✓ Data cleaning complete: {len(df_cleaned)} rows remaining")
    return df_cleaned

def create_calculated_fields(df):
    """Create calculated metrics and derived fields."""
    print("\n" + "="*50)
    print("CREATING CALCULATED FIELDS")
    print("="*50)
    
    df_calc = df.copy()
    
    # 1. Profit Margin %
    df_calc['Profit Margin %'] = np.where(
        df_calc['Sales'] != 0,
        (df_calc['Profit'] / df_calc['Sales']) * 100,
        0
    )
    print("✓ Created: Profit Margin %")
    
    # 2. Days to Ship
    df_calc['Days to Ship'] = (df_calc['Ship Date'] - df_calc['Order Date']).dt.days
    print("✓ Created: Days to Ship")
    
    # 3. Extract date components
    df_calc['Order Year'] = df_calc['Order Date'].dt.year
    df_calc['Order Month'] = df_calc['Order Date'].dt.month
    df_calc['Order Quarter'] = df_calc['Order Date'].dt.quarter
    df_calc['Order Year-Month'] = df_calc['Order Date'].dt.to_period('M').astype(str)
    df_calc['Order Day of Week'] = df_calc['Order Date'].dt.day_name()
    print("✓ Created: Date components (Year, Month, Quarter, Year-Month, Day of Week)")
    
    # 4. Discount Amount (in dollars)
    df_calc['Discount Amount'] = df_calc['Sales'] * df_calc['Discount']
    print("✓ Created: Discount Amount")
    
    # 5. Sales per Unit
    df_calc['Sales per Unit'] = np.where(
        df_calc['Quantity'] != 0,
        df_calc['Sales'] / df_calc['Quantity'],
        0
    )
    print("✓ Created: Sales per Unit")
    
    # 6. Profit per Unit
    df_calc['Profit per Unit'] = np.where(
        df_calc['Quantity'] != 0,
        df_calc['Profit'] / df_calc['Quantity'],
        0
    )
    print("✓ Created: Profit per Unit")
    
    # 7. Flag for Loss-Making Orders
    df_calc['Is Loss'] = (df_calc['Profit'] < 0).astype(int)
    print("✓ Created: Is Loss flag")
    
    # 8. Order Value Category
    df_calc['Order Value Category'] = pd.cut(
        df_calc['Sales'],
        bins=[0, 100, 500, 1000, float('inf')],
        labels=['Low (<$100)', 'Medium ($100-$500)', 'High ($500-$1000)', 'Very High (>$1000)']
    )
    print("✓ Created: Order Value Category")
    
    return df_calc

def calculate_aggregate_metrics(df):
    """Calculate aggregate business metrics."""
    print("\n" + "="*50)
    print("AGGREGATE METRICS")
    print("="*50)
    
    metrics = {}
    
    # Total Sales
    metrics['Total Sales'] = df['Sales'].sum()
    print(f"Total Sales: ${metrics['Total Sales']:,.2f}")
    
    # Total Profit
    metrics['Total Profit'] = df['Profit'].sum()
    print(f"Total Profit: ${metrics['Total Profit']:,.2f}")
    
    # Overall Profit Margin
    metrics['Overall Profit Margin %'] = (metrics['Total Profit'] / metrics['Total Sales']) * 100
    print(f"Overall Profit Margin: {metrics['Overall Profit Margin %']:.2f}%")
    
    # Average Order Value
    unique_orders = df['Order ID'].nunique()
    metrics['Average Order Value'] = metrics['Total Sales'] / unique_orders
    print(f"Average Order Value: ${metrics['Average Order Value']:,.2f}")
    
    # Total Orders
    metrics['Total Orders'] = unique_orders
    print(f"Total Orders: {metrics['Total Orders']:,}")
    
    # Total Customers
    metrics['Total Customers'] = df['Customer ID'].nunique()
    print(f"Total Customers: {metrics['Total Customers']:,}")
    
    # Repeat Customer Rate
    customer_order_count = df.groupby('Customer ID')['Order ID'].nunique()
    repeat_customers = (customer_order_count > 1).sum()
    metrics['Repeat Customer Rate %'] = (repeat_customers / len(customer_order_count)) * 100
    print(f"Repeat Customer Rate: {metrics['Repeat Customer Rate %']:.2f}%")
    
    # Average Days to Ship
    metrics['Average Days to Ship'] = df['Days to Ship'].mean()
    print(f"Average Days to Ship: {metrics['Average Days to Ship']:.2f} days")
    
    return metrics

def calculate_growth_metrics(df):
    """Calculate year-over-year and month-over-month growth."""
    print("\n" + "="*50)
    print("GROWTH METRICS")
    print("="*50)
    
    # Yearly Sales
    yearly_sales = df.groupby('Order Year')['Sales'].sum().sort_index()
    print("\nYearly Sales:")
    for year, sales in yearly_sales.items():
        print(f"  {year}: ${sales:,.2f}")
    
    # YoY Growth
    if len(yearly_sales) > 1:
        yoy_growth = ((yearly_sales - yearly_sales.shift(1)) / yearly_sales.shift(1)) * 100
        print("\nYear-over-Year Growth:")
        for year, growth in yoy_growth.items():
            if not pd.isna(growth):
                print(f"  {year}: {growth:.2f}%")
    
    # Monthly Sales (last 12 months)
    monthly_sales = df.groupby('Order Year-Month')['Sales'].sum().sort_index()
    print(f"\nMonthly Sales (showing last 12 months):")
    for month, sales in monthly_sales.tail(12).items():
        print(f"  {month}: ${sales:,.2f}")
    
    return yearly_sales, monthly_sales

def save_cleaned_data(df, output_path):
    """Save cleaned data to CSV file."""
    try:
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        df.to_csv(output_path, index=False)
        print(f"\n✓ Cleaned data saved to: {output_path}")
        return True
    except Exception as e:
        print(f"\n✗ Error saving data: {str(e)}")
        return False

def main():
    """Main execution function."""
    print("="*50)
    print("SUPERSTORE DATA CLEANING & PREPARATION")
    print("="*50)
    
    # File paths
    input_file = 'data/raw/SampleSuperstore.csv'
    output_file = 'data/processed/superstore_cleaned.csv'
    
    # Load data
    df = load_data(input_file)
    if df is None:
        print("\n✗ Cannot proceed without data file.")
        print(f"Please download the dataset and place it at: {input_file}")
        return
    
    # Data quality checks
    df = check_data_quality(df)
    
    # Clean data
    df_cleaned = clean_data(df)
    
    # Create calculated fields
    df_final = create_calculated_fields(df_cleaned)
    
    # Calculate aggregate metrics
    metrics = calculate_aggregate_metrics(df_final)
    
    # Calculate growth metrics
    yearly_sales, monthly_sales = calculate_growth_metrics(df_final)
    
    # Save cleaned data
    save_cleaned_data(df_final, output_file)
    
    print("\n" + "="*50)
    print("DATA PREPARATION COMPLETE!")
    print("="*50)
    print(f"\nFinal Dataset:")
    print(f"  Rows: {len(df_final):,}")
    print(f"  Columns: {len(df_final.columns)}")
    print(f"  Date Range: {df_final['Order Date'].min()} to {df_final['Order Date'].max()}")
    print(f"\nReady for dashboard creation in Tableau and Power BI!")

if __name__ == "__main__":
    main()
