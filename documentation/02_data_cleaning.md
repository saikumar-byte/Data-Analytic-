# Step 2: Data Cleaning & Preparation

## Overview

Data cleaning is a critical step to ensure accurate analysis and reliable insights. This document outlines all data cleaning steps performed on the Superstore dataset.

## Data Cleaning Steps

### 1. Missing Values Handling

#### Check for Missing Values
```python
# Check missing values in each column
missing_values = df.isnull().sum()
missing_percentage = (missing_values / len(df)) * 100
```

#### Handling Strategy
- **Postal Code**: May have missing values. If missing, can be filled with state-level average or left as null if not critical for analysis
- **Other Columns**: Typically no missing values in Superstore dataset, but always verify

**Action**: Remove rows with critical missing values (Order ID, Customer ID, Sales, Profit) or impute based on business logic.

### 2. Duplicate Records

#### Check for Duplicates
```python
# Check for duplicate rows
duplicate_rows = df.duplicated().sum()
```

#### Handling Strategy
- Remove exact duplicate rows
- Check for duplicate Order IDs with different details (data quality issue)
- Verify if duplicates are legitimate (same customer, multiple orders)

**Action**: Remove exact duplicates, investigate and resolve data quality issues.

### 3. Date Formatting

#### Standardize Date Columns
```python
# Convert Order Date and Ship Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
```

#### Extract Date Components
- Year, Month, Quarter, Day of Week
- Days to Ship (Ship Date - Order Date)
- Year-Month for time-series analysis

**Action**: Ensure consistent date format (YYYY-MM-DD) and create time-based dimensions.

### 4. Data Type Corrections

#### Ensure Correct Data Types
- **Sales, Profit, Discount**: Float
- **Quantity**: Integer
- **Postal Code**: String (to preserve leading zeros if any)
- **Order Date, Ship Date**: DateTime

**Action**: Convert columns to appropriate data types for accurate calculations.

### 5. Outlier Detection & Handling

#### Check for Outliers
```python
# Check for negative sales or profit (may indicate returns)
negative_sales = df[df['Sales'] < 0]
negative_profit = df[df['Profit'] < 0]

# Check for unrealistic values
high_discounts = df[df['Discount'] > 1]  # Discount > 100%
```

#### Handling Strategy
- **Negative Sales/Profit**: May represent returns. Decide whether to exclude or flag
- **Unrealistic Discounts**: Cap at 100% or investigate data quality
- **Extreme Values**: Use IQR method or domain knowledge to identify outliers

**Action**: Flag outliers for review, exclude if data quality issues, or cap extreme values.

### 6. Inconsistent Categorical Values

#### Standardize Categories
- **Region**: Ensure consistent naming (West, East, Central, South)
- **Segment**: Standardize (Consumer, Corporate, Home Office)
- **Ship Mode**: Standardize shipping mode names
- **Category/Sub-Category**: Check for typos or variations

**Action**: Standardize all categorical values to ensure consistent grouping.

## Calculated Fields Creation

### 1. Profit Margin

**Formula**: `Profit Margin % = (Profit / Sales) * 100`

**Business Use**: Measures profitability efficiency. Higher margin = more efficient profit generation.

```python
df['Profit Margin %'] = (df['Profit'] / df['Sales']) * 100
# Handle division by zero
df['Profit Margin %'] = df['Profit Margin %'].replace([np.inf, -np.inf], 0)
```

### 2. Year-over-Year (YoY) Growth

**Formula**: `YoY Growth % = ((Current Year Sales - Previous Year Sales) / Previous Year Sales) * 100`

**Business Use**: Measures annual growth rate, indicates business expansion.

```python
# Calculate YoY growth
yearly_sales = df.groupby(df['Order Date'].dt.year)['Sales'].sum()
yoy_growth = ((yearly_sales - yearly_sales.shift(1)) / yearly_sales.shift(1)) * 100
```

### 3. Month-over-Month (MoM) Growth

**Formula**: `MoM Growth % = ((Current Month Sales - Previous Month Sales) / Previous Month Sales) * 100`

**Business Use**: Identifies short-term trends and seasonal patterns.

```python
# Calculate MoM growth
monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()
mom_growth = ((monthly_sales - monthly_sales.shift(1)) / monthly_sales.shift(1)) * 100
```

### 4. Average Order Value (AOV)

**Formula**: `AOV = Total Sales / Number of Unique Orders`

**Business Use**: Measures customer spending per order, indicates customer value.

```python
# Calculate AOV
total_sales = df['Sales'].sum()
unique_orders = df['Order ID'].nunique()
aov = total_sales / unique_orders

# Or per customer
customer_aov = df.groupby('Customer ID')['Sales'].sum() / df.groupby('Customer ID')['Order ID'].nunique()
```

### 5. Customer Retention / Repeat Customers

**Formula**: 
- `Repeat Customer Rate = (Customers with >1 Order / Total Customers) * 100`
- `Customer Lifetime Value = Sum of all sales per customer`

**Business Use**: Measures customer loyalty and long-term value.

```python
# Identify repeat customers
customer_order_count = df.groupby('Customer ID')['Order ID'].nunique()
repeat_customers = (customer_order_count > 1).sum()
total_customers = len(customer_order_count)
retention_rate = (repeat_customers / total_customers) * 100

# Customer Lifetime Value
customer_lifetime_value = df.groupby('Customer ID')['Sales'].sum()
```

### 6. Days to Ship

**Formula**: `Days to Ship = Ship Date - Order Date`

**Business Use**: Measures fulfillment efficiency, impacts customer satisfaction.

```python
df['Days to Ship'] = (df['Ship Date'] - df['Order Date']).dt.days
```

### 7. Discount Impact on Profit

**Formula**: `Discount Impact = Profit with Discount - Estimated Profit without Discount`

**Business Use**: Analyzes discount effectiveness and optimal discount levels.

```python
# Estimate profit without discount (simplified)
df['Estimated Sales without Discount'] = df['Sales'] / (1 - df['Discount'])
df['Discount Impact'] = df['Profit'] - (df['Estimated Sales without Discount'] * df['Profit Margin %'] / 100)
```

## Data Quality Checks

### Post-Cleaning Validation

1. **Row Count**: Verify expected number of rows after cleaning
2. **Date Range**: Confirm date range is logical
3. **Sales/Profit Totals**: Verify totals match expected values
4. **Negative Values**: Check if negative profits are legitimate (returns)
5. **Calculated Fields**: Verify formulas produce expected results

## Output: Clean Dataset

After cleaning, the dataset should have:

- ✅ No missing critical values
- ✅ No duplicate rows
- ✅ Consistent date formats
- ✅ Correct data types
- ✅ Standardized categorical values
- ✅ All calculated fields populated
- ✅ Outliers identified and handled

## Next Steps

After data cleaning:
- **Step 3**: Define KPIs based on cleaned data
- **Step 4**: Create Tableau dashboard
- **Step 5**: Create Power BI dashboard
