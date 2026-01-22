# Step 4: Tableau Dashboard Creation

## Overview

This guide provides step-by-step instructions for creating a professional, interactive Tableau dashboard for the Superstore Sales Analytics project.

## Prerequisites

- Tableau Desktop installed
- Cleaned dataset (`superstore_cleaned.csv`) ready
- Basic understanding of Tableau interface

## Dashboard Structure

### Layout Overview

```
┌─────────────────────────────────────────────────────────────┐
│  DASHBOARD TITLE: Superstore Sales Analytics                │
├─────────────────────────────────────────────────────────────┤
│  FILTERS (Top)                                               │
│  [Region] [Category] [Segment] [Date Range]                 │
├─────────────────────────────────────────────────────────────┤
│  KPI CARDS (Row 1)                                           │
│  [Sales] [Profit] [Margin] [Growth]                          │
├─────────────────────────────────────────────────────────────┤
│  SALES TREND (Row 2 - Left)    │  CATEGORY PERFORMANCE      │
│  [Line Chart]                  │  [Bar Chart]               │
├─────────────────────────────────────────────────────────────┤
│  REGIONAL MAP (Row 3 - Left)   │  TOP 10 PRODUCTS          │
│  [Map Visualization]           │  [Horizontal Bar Chart]    │
└─────────────────────────────────────────────────────────────┘
```

## Step-by-Step Dashboard Creation

### Step 1: Connect to Data

1. Open Tableau Desktop
2. Click "Connect to Data" → "Text file" or "Excel"
3. Navigate to `data/processed/superstore_cleaned.csv`
4. Click "Open"
5. Verify all columns are loaded correctly

### Step 2: Create Calculated Fields

#### 2.1 Profit Margin %
1. Right-click in Data pane → "Create Calculated Field"
2. Name: `Profit Margin %`
3. Formula: `SUM([Profit]) / SUM([Sales]) * 100`
4. Click OK

#### 2.2 Sales Growth (YoY)
1. Create Calculated Field: `Sales YoY Growth`
2. Formula:
```tableau
(SUM([Sales]) - LOOKUP(SUM([Sales]), -1)) / LOOKUP(SUM([Sales]), -1) * 100
```
3. Use Table Calculation: "Year over Year Growth"

#### 2.3 Sales Growth (MoM)
1. Create Calculated Field: `Sales MoM Growth`
2. Use Quick Table Calculation: "Percent Difference"
3. Set Compute Using: "Table (across)"

#### 2.4 Profit/Loss Flag
1. Create Calculated Field: `Is Profit`
2. Formula: `SUM([Profit]) > 0`
3. This creates a boolean for color coding

### Step 3: Create KPI Cards

#### 3.1 Total Sales Card
1. Drag `Sales` to Text mark
2. Change mark type to "Text"
3. Format: Currency ($)
4. Add label: "Total Sales"
5. Format font size: Large (24-36pt)
6. Add background color (light blue)

#### 3.2 Total Profit Card
1. Drag `Profit` to Text mark
2. Format: Currency ($)
3. Add conditional formatting:
   - If `SUM([Profit]) > 0`: Green
   - If `SUM([Profit]) < 0`: Red
4. Add label: "Total Profit"

#### 3.3 Profit Margin Card
1. Drag `Profit Margin %` to Text mark
2. Format: Percentage (1 decimal place)
3. Add conditional formatting based on value
4. Add label: "Profit Margin %"

#### 3.4 Sales Growth Card
1. Drag `Sales YoY Growth` to Text mark
2. Format: Percentage (1 decimal place)
3. Add arrow indicator (↑ for positive, ↓ for negative)
4. Add label: "YoY Growth"

**Tip**: Create a dashboard sheet with 4 columns, each containing one KPI card.

### Step 4: Create Sales Trend Line Chart

**Purpose**: Shows sales performance over time, identifies trends and seasonality.

**Business Question**: How are sales trending over time? Are there seasonal patterns?

1. Create new worksheet: "Sales Trend"
2. Drag `Order Date` to Columns (as continuous, by month)
3. Drag `Sales` to Rows
4. Change mark type to "Line"
5. Add `Profit` as dual axis (optional, for comparison)
6. Format:
   - X-axis: Show month/year labels
   - Y-axis: Currency format
   - Add gridlines for readability
7. Add tooltip:
   - Month: `ATTR([Order Year-Month])`
   - Sales: `SUM([Sales])`
   - Growth: `[Sales MoM Growth]`

**Insights**: Stakeholders can identify:
- Upward/downward trends
- Seasonal patterns (holidays, end of quarter)
- Growth acceleration or deceleration
- Anomalies or outliers

### Step 5: Create Category Performance Bar Chart

**Purpose**: Compares performance across product categories and sub-categories.

**Business Question**: Which categories drive the most sales and profit?

1. Create new worksheet: "Category Performance"
2. Drag `Category` to Columns
3. Drag `Sales` to Rows
4. Change mark type to "Bar"
5. Add `Profit` to Color (gradient: green to red)
6. Add `Sub-Category` to Detail (for drill-down)
7. Sort by Sales (descending)
8. Add labels: Show Sales and Profit on bars
9. Format:
   - Color legend: Profit (green = high, red = low/negative)
   - Bar labels: Currency format

**Alternative**: Create stacked bar with Sub-Category breakdown

**Insights**: Stakeholders can identify:
- Best and worst performing categories
- Profitability by category
- Opportunities for category expansion
- Categories needing attention

### Step 6: Create Regional Map Visualization

**Purpose**: Geographic visualization of sales and profit by region/state.

**Business Question**: Which regions perform best? Are there geographic patterns?

1. Create new worksheet: "Regional Performance"
2. Double-click `State` (Tableau auto-generates map)
3. Drag `Sales` to Size
4. Drag `Profit` to Color
5. Add `Region` to Detail
6. Format:
   - Color: Profit (diverging: green to red)
   - Size: Proportional to Sales
   - Tooltip: Show State, Region, Sales, Profit, Margin
7. Add labels: State names (if readable)

**Alternative**: Use Region instead of State for higher-level view

**Insights**: Stakeholders can identify:
- Geographic sales distribution
- Regional profitability differences
- Underperforming regions
- Expansion opportunities

### Step 7: Create Top 10 Products Chart

**Purpose**: Highlights best-selling products for focus and promotion.

**Business Question**: Which products generate the most revenue?

1. Create new worksheet: "Top Products"
2. Drag `Product Name` to Rows
3. Drag `Sales` to Columns
4. Sort by Sales (descending)
5. Add filter: Top 10 by Sales
6. Format as horizontal bar chart
7. Add `Profit` to Color
8. Add labels: Sales amount
9. Sort: Descending

**Insights**: Stakeholders can identify:
- Best-selling products
- Products to promote
- Inventory priorities
- Product profitability

### Step 8: Create Interactive Filters

#### 8.1 Region Filter
1. Right-click `Region` → "Show Filter"
2. Format as dropdown or multi-select
3. Position at top of dashboard

#### 8.2 Category Filter
1. Show filter for `Category`
2. Format as checkbox list
3. Allow multiple selections

#### 8.3 Segment Filter
1. Show filter for `Segment`
2. Format as dropdown

#### 8.4 Date Range Filter
1. Show filter for `Order Date`
2. Format as date range picker
3. Set default to last 12 months

**Tip**: Apply filters to all sheets using "Apply to Worksheets" → "All Using This Data Source"

### Step 9: Create Dashboard Layout

1. Create new dashboard: "Superstore Analytics"
2. Set dashboard size: 1200x800 (or custom)
3. Add sheets in this order:
   - **Row 1**: KPI Cards (4 columns)
   - **Row 2**: Sales Trend (full width)
   - **Row 3**: Category Performance (left) | Top Products (right)
   - **Row 4**: Regional Map (full width)
4. Add filters to top of dashboard
5. Format:
   - Background: Light gray or white
   - Title: "Superstore Sales Analytics Dashboard"
   - Add subtitle with last updated date

### Step 10: Add Tooltips and Insights

#### Enhanced Tooltips
For each visualization, add informative tooltips:

**Sales Trend Tooltip**:
```
Month: <Order Year-Month>
Sales: $<Sales>
Profit: $<Profit>
Margin: <Profit Margin %>%
MoM Growth: <Sales MoM Growth>%
```

**Category Tooltip**:
```
Category: <Category>
Sub-Category: <Sub-Category>
Sales: $<Sales>
Profit: $<Profit>
Margin: <Profit Margin %>%
```

**Map Tooltip**:
```
State: <State>
Region: <Region>
Sales: $<Sales>
Profit: $<Profit>
Orders: <COUNT(Order ID)>
```

### Step 11: Color Scheme

**Recommended Color Palette**:
- **Profit Positive**: Green (#4CAF50 or #2E7D32)
- **Profit Negative**: Red (#F44336 or #C62828)
- **Sales**: Blue (#2196F3)
- **Neutral**: Gray (#757575)
- **Background**: Light gray (#F5F5F5) or white

**Apply Colors**:
- Profit-based visualizations: Green to Red gradient
- Sales-based: Blue gradient
- KPI cards: Light background with dark text

### Step 12: Final Formatting

1. **Consistent Fonts**: Use same font family throughout (Arial, Calibri, or Tableau default)
2. **Alignment**: Align all elements properly
3. **Spacing**: Consistent padding and margins
4. **Legends**: Position consistently, make readable
5. **Titles**: Add descriptive titles to each chart
6. **Annotations**: Add key insights as annotations (optional)

## Dashboard Features Summary

### Interactivity
- ✅ Region filter (dropdown)
- ✅ Category filter (multi-select)
- ✅ Segment filter (dropdown)
- ✅ Date range filter
- ✅ Tooltips on hover
- ✅ Click to filter (cross-filtering)
- ✅ Highlight actions

### Visualizations
- ✅ KPI cards (4 primary metrics)
- ✅ Sales trend line chart
- ✅ Category performance bar chart
- ✅ Regional map
- ✅ Top 10 products chart

### Business Value
- ✅ Real-time KPI monitoring
- ✅ Trend identification
- ✅ Performance comparison
- ✅ Geographic insights
- ✅ Product prioritization

## Why Each Chart is Used

| Chart | Business Question | Insight Type |
|-------|------------------|--------------|
| **KPI Cards** | What are our key metrics? | High-level performance |
| **Line Chart** | How are sales trending? | Time-series trends |
| **Bar Chart** | Which categories perform best? | Comparative analysis |
| **Map** | Where do we sell most? | Geographic distribution |
| **Top 10** | What products drive revenue? | Product prioritization |

## Export and Sharing

1. **Export as Image**: Dashboard → Export → Image
2. **Export as PDF**: Dashboard → Export → PDF
3. **Publish to Tableau Public**: File → Save to Tableau Public (free account)
4. **Publish to Tableau Server**: File → Save to Tableau Server (if available)

## Next Steps

After creating the Tableau dashboard:
- **Step 5**: Create equivalent Power BI dashboard
- **Step 6**: Generate business insights
- **Step 7**: Prepare portfolio materials
