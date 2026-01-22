# Quick Start Guide

## 🚀 Get Started in 5 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Download Dataset
1. Go to [Kaggle Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
2. Download `SampleSuperstore.csv`
3. Place it in `data/raw/SampleSuperstore.csv`

### Step 3: Run Data Cleaning
```bash
python scripts/data_preparation.py
```

This will:
- Clean the data
- Create calculated fields
- Save cleaned data to `data/processed/superstore_cleaned.csv`
- Display summary metrics

### Step 4: Create Dashboards

#### Tableau
1. Open Tableau Desktop
2. Connect to `data/processed/superstore_cleaned.csv`
3. Follow guide in `documentation/04_tableau_dashboard.md`

#### Power BI
1. Open Power BI Desktop
2. Get Data → Text/CSV → Select `data/processed/superstore_cleaned.csv`
3. Follow guide in `documentation/05_powerbi_dashboard.md`

### Step 5: Review Insights
- Read `documentation/06_business_insights.md` for analysis framework
- Fill in specific numbers after running your analysis
- Use insights for portfolio and interviews

## 📚 Documentation Order

1. **01_dataset_selection.md** - Understand the dataset
2. **02_data_cleaning.md** - Learn cleaning methodology
3. **03_kpi_definitions.md** - Understand KPIs
4. **04_tableau_dashboard.md** - Build Tableau dashboard
5. **05_powerbi_dashboard.md** - Build Power BI dashboard
6. **06_business_insights.md** - Generate insights

## 💼 Portfolio Materials

- **resume_bullets.md** - Copy relevant bullets to your resume
- **interview_qa.md** - Prepare for interview questions

## 🎯 Project Checklist

- [ ] Dataset downloaded and placed in `data/raw/`
- [ ] Data cleaning script run successfully
- [ ] Tableau dashboard created
- [ ] Power BI dashboard created
- [ ] Business insights documented
- [ ] Resume bullets selected
- [ ] Interview questions reviewed

## 💡 Tips

- **Start with data cleaning** - Everything depends on clean data
- **Build one dashboard first** - Master one tool, then try the other
- **Document as you go** - Note your findings and decisions
- **Customize insights** - Fill in actual numbers from your analysis
- **Practice explaining** - Be ready to discuss your project

## 🆘 Troubleshooting

**Data file not found?**
- Ensure file is named exactly `SampleSuperstore.csv`
- Check it's in `data/raw/` folder
- Verify file path in script matches your structure

**Python errors?**
- Ensure Python 3.8+ is installed
- Install all requirements: `pip install -r requirements.txt`
- Check for missing dependencies

**Dashboard issues?**
- Refer to tool-specific documentation
- Check data types are correct
- Verify calculated fields/formulas

## 📞 Next Steps

After completing the project:
1. Add to your portfolio/GitHub
2. Update your resume with project bullets
3. Practice explaining the project
4. Prepare for interview questions
5. Consider adding to LinkedIn

Good luck! 🎉
