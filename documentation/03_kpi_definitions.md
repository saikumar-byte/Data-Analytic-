# Step 3: KPI Definition

## Overview

Key Performance Indicators (KPIs) are measurable values that demonstrate how effectively a business is achieving key objectives. This document defines all KPIs used in the Superstore Sales Analytics Dashboard.

## Primary KPIs

### 1. Total Sales

**Definition**: Sum of all sales revenue across all orders, products, regions, and time periods.

**Formula**: `Total Sales = Σ(Sales)`

**Business Question**: What is our total revenue?

**Target Audience**: C-level executives, Sales Directors

**Visualization**: Large KPI card at the top of dashboard

**Interpretation**: 
- Higher is better
- Compare against targets and previous periods
- Indicates overall business size and growth

---

### 2. Total Profit

**Definition**: Sum of all profit (revenue minus costs) across all transactions.

**Formula**: `Total Profit = Σ(Profit)`

**Business Question**: How much profit are we generating?

**Target Audience**: CFO, Finance team, Business Owners

**Visualization**: Large KPI card with color coding (green for positive, red for negative)

**Interpretation**:
- Positive = profitable business
- Negative = loss-making (needs investigation)
- Compare against targets and industry benchmarks

---

### 3. Profit Margin %

**Definition**: Percentage of sales that translates to profit. Measures profitability efficiency.

**Formula**: `Profit Margin % = (Total Profit / Total Sales) × 100`

**Business Question**: How efficiently are we converting sales to profit?

**Target Audience**: Finance team, Operations, Management

**Visualization**: KPI card with percentage format

**Interpretation**:
- **>20%**: Excellent profitability
- **10-20%**: Good profitability
- **5-10%**: Moderate profitability
- **<5%**: Low profitability (needs improvement)
- **Negative**: Loss-making (critical issue)

**Benchmark**: Industry average for retail is typically 5-10%

---

### 4. Sales Growth (Month-over-Month / Year-over-Year)

**Definition**: Percentage change in sales compared to previous period.

**Formulas**:
- **MoM Growth**: `((Current Month Sales - Previous Month Sales) / Previous Month Sales) × 100`
- **YoY Growth**: `((Current Year Sales - Previous Year Sales) / Previous Year Sales) × 100`

**Business Question**: Are we growing? At what rate?

**Target Audience**: Sales team, Management, Investors

**Visualization**: 
- Line chart showing trend
- KPI card showing current period growth

**Interpretation**:
- **Positive Growth**: Business is expanding
- **Negative Growth**: Business is declining (needs attention)
- **Target**: Typically aim for 10-20% YoY growth in retail

---

### 5. Average Order Value (AOV)

**Definition**: Average amount spent per order.

**Formula**: `AOV = Total Sales / Number of Unique Orders`

**Business Question**: How much does a typical customer spend per order?

**Target Audience**: Marketing, Sales, E-commerce teams

**Visualization**: KPI card

**Interpretation**:
- Higher AOV = more revenue per transaction
- Can be improved through upselling, cross-selling, bundling
- Compare across segments, regions, time periods

---

### 6. Total Orders

**Definition**: Count of unique orders placed.

**Formula**: `Total Orders = COUNT(DISTINCT Order ID)`

**Business Question**: How many transactions did we process?

**Target Audience**: Operations, Sales, Management

**Visualization**: KPI card

**Interpretation**:
- Indicates transaction volume
- Compare with sales to understand AOV
- Growth in orders = business expansion

---

### 7. Total Customers

**Definition**: Count of unique customers.

**Formula**: `Total Customers = COUNT(DISTINCT Customer ID)`

**Business Question**: How many customers do we have?

**Target Audience**: Marketing, Customer Success, Management

**Visualization**: KPI card

**Interpretation**:
- Customer base size
- Compare with orders to understand order frequency
- Growth = customer acquisition success

---

### 8. Customer Retention Rate / Repeat Customer Rate

**Definition**: Percentage of customers who have placed more than one order.

**Formula**: `Repeat Customer Rate = (Customers with >1 Order / Total Customers) × 100`

**Business Question**: How loyal are our customers? Are they coming back?

**Target Audience**: Marketing, Customer Success, Retention teams

**Visualization**: KPI card with percentage

**Interpretation**:
- **>40%**: Excellent retention
- **20-40%**: Good retention
- **<20%**: Low retention (needs improvement)
- Higher retention = better customer lifetime value

---

## Secondary KPIs

### 9. Top-Performing Products

**Definition**: Products ranked by sales or profit.

**Business Question**: Which products drive the most revenue/profit?

**Visualization**: Bar chart, Top 10 list

**Use Case**: 
- Focus marketing on top products
- Identify bestsellers
- Inventory planning

---

### 10. Top-Performing Categories

**Definition**: Product categories ranked by sales or profit.

**Business Question**: Which product categories are most successful?

**Visualization**: Horizontal bar chart, pie chart

**Use Case**:
- Category-level strategy
- Resource allocation
- Marketing focus

---

### 11. Worst-Performing Regions

**Definition**: Regions with lowest sales, profit, or negative profit.

**Business Question**: Which regions need improvement?

**Visualization**: Map visualization, bar chart

**Use Case**:
- Identify underperforming markets
- Regional strategy development
- Resource reallocation

---

### 12. Loss-Making Products/Regions

**Definition**: Products or regions with negative profit.

**Business Question**: Where are we losing money?

**Visualization**: 
- Red-highlighted table
- Map with red regions
- Bar chart with negative values

**Use Case**:
- Identify problems
- Pricing strategy review
- Discontinuation decisions

---

### 13. Sales by Customer Segment

**Definition**: Sales breakdown by Consumer, Corporate, and Home Office segments.

**Business Question**: Which customer segment is most valuable?

**Visualization**: Stacked bar chart, pie chart

**Use Case**:
- Segment-specific marketing
- Product development
- Pricing strategies

---

### 14. Average Days to Ship

**Definition**: Average time between order date and ship date.

**Formula**: `Average Days to Ship = AVG(Ship Date - Order Date)`

**Business Question**: How fast are we fulfilling orders?

**Visualization**: KPI card, trend line

**Interpretation**:
- Lower is better (faster fulfillment)
- Impacts customer satisfaction
- Compare across regions, ship modes

---

### 15. Discount Impact

**Definition**: Analysis of how discounts affect profit margins.

**Business Question**: Are our discounts effective? Do they drive profit or reduce it?

**Visualization**: Scatter plot (Discount % vs Profit Margin), correlation analysis

**Use Case**:
- Pricing strategy optimization
- Promotion effectiveness
- Discount level decisions

---

## KPI Dashboard Layout

### Recommended KPI Card Layout

```
┌─────────────────────────────────────────────────────────┐
│  PRIMARY KPIs (Top Row)                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐│
│  │Total Sales│  │Total Profit│ │Profit Margin│ │Sales Growth││
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘│
│                                                          │
│  SECONDARY KPIs (Second Row)                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐│
│  │AOV       │  │Total Orders│ │Customers │ │Retention ││
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘│
└─────────────────────────────────────────────────────────┘
```

## KPI Calculation in Different Tools

### Excel/CSV
- Use SUM, AVERAGE, COUNT functions
- Pivot tables for aggregations

### Tableau
- Calculated fields for formulas
- Quick table calculations for growth
- Built-in functions: SUM(), AVG(), COUNTD()

### Power BI
- DAX measures for all KPIs
- Examples:
  - `Total Sales = SUM(Table[Sales])`
  - `Profit Margin % = DIVIDE([Total Profit], [Total Sales], 0) * 100`
  - `YoY Growth = CALCULATE([Total Sales], SAMEPERIODLASTYEAR(...))`

## Next Steps

After defining KPIs:
- **Step 4**: Create Tableau dashboard with these KPIs
- **Step 5**: Create Power BI dashboard with DAX measures
- **Step 6**: Generate business insights based on KPI analysis
