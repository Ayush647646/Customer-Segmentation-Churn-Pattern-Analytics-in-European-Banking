# European Bank Customer Churn Analytics Project

## 🎯 Project Overview

This comprehensive data analytics project examines customer churn patterns across European banking operations (France, Spain, Germany) using advanced segmentation analytics. The project includes:

- **Complete EDA Analysis** with statistical insights
- **Interactive Streamlit Dashboard** with dynamic filtering
- **Professional Research Paper** (35+ pages)
- **Executive Summary** for government stakeholders
- **Comprehensive Visualizations** (12-panel analytical suite)

---

## 📊 Key Findings Summary

### Critical Metrics
- **Overall Churn Rate**: 20.37% (2,037 of 10,000 customers)
- **Germany Churn**: 32.44% (CRITICAL - 2x other markets)
- **Age 46-60 Churn**: 51.12% (CRITICAL vulnerability)
- **High-Value Customer Loss**: 1,643 customers, €173.6M at risk
- **Inactive Member Churn**: 26.85% vs 14.27% for active

### Geographic Insights
- **France**: 16.15% churn rate (5,014 customers)
- **Spain**: 16.67% churn rate (2,477 customers)
- **Germany**: 32.44% churn rate (2,509 customers) - URGENT ATTENTION REQUIRED

### Product Paradox
- 1 Product: 27.71% churn
- 2 Products: 7.58% churn (OPTIMAL)
- 3 Products: 82.71% churn (CRITICAL)
- 4 Products: 100% churn (ALL CUSTOMERS LOST)

---

## 📁 Project Deliverables

### 1. Research Paper
**File**: `European_Bank_Churn_Research_Paper.docx`
- 35+ page comprehensive analysis
- Complete methodology and findings
- Statistical analysis with p-values
- Strategic recommendations
- Implementation roadmap

### 2. Executive Summary
**File**: `Executive_Summary_Government_Stakeholders.docx`
- 8-page executive briefing
- Regulatory implications
- Systemic risk assessment
- Policy recommendations
- Immediate action items

### 3. Visual Analytics
**File**: `churn_analysis_visualizations.png`
- 12-panel comprehensive visualization suite
- Geographic, demographic, and financial analysis
- High-quality publication-ready charts

### 4. Interactive Dashboard
**File**: `streamlit_dashboard.py`
- Real-time interactive analytics
- Dynamic filtering by geography, age, activity
- 5 analytical tabs with 15+ visualizations
- KPI monitoring dashboard

### 5. Processed Dataset
**File**: `processed_bank_data.csv`
- Clean, segmented data ready for further analysis
- All derived features included

---

## 🚀 Running the Interactive Dashboard

### Prerequisites
```bash
# Install required packages
pip install streamlit pandas numpy matplotlib seaborn --break-system-packages
```

### Launch Dashboard
```bash
streamlit run streamlit_dashboard.py
```

The dashboard will open in your browser with:
- **Geographic Analysis**: Country-wise churn comparison
- **Demographic Insights**: Age and gender patterns
- **Financial Profiles**: Credit score and balance analysis
- **Engagement Patterns**: Activity and product analysis
- **High-Value Customers**: Premium segment deep-dive

### Dashboard Features
- ✅ Dynamic filters (Geography, Age Group, Activity Status)
- ✅ Real-time KPI updates
- ✅ Interactive visualizations
- ✅ Drill-down capabilities
- ✅ Segment-specific insights

---

## 📈 Key Analytical Insights

### 1. Geographic Risk Concentration
**Germany requires immediate intervention** with churn rate double that of France and Spain. Despite higher average balance (€119,730), German customers show significantly lower loyalty.

**Recommendation**: Launch comprehensive Germany market investigation and implement country-specific retention programs.

### 2. Age Vulnerability
**Age group 46-60 shows 51.12% churn** - over half of all customers in this critical pre-retirement segment are churning. This represents significant revenue and lifetime value loss.

**Recommendation**: Create age-targeted banking products, wealth management services, and retirement planning offerings specifically for this demographic.

### 3. Engagement Crisis
**Inactive members churn at nearly double the rate** of active members (26.85% vs 14.27%). Customer engagement is the single strongest predictor of retention.

**Recommendation**: Launch proactive re-engagement campaigns, implement digital engagement tools, and create win-back offers for inactive customers.

### 4. Product Complexity Issues
**Customers with 3-4 products show extreme churn** (82.71% and 100%), suggesting product complexity or satisfaction issues rather than deeper engagement.

**Recommendation**: Review product bundling strategies, simplify offerings, and enhance customer education and support for multi-product relationships.

### 5. High-Value Customer Risk
**1,643 high-value customers churned** representing €173.6M in deposits at risk. High-value customers show 48% higher churn than regular customers (22.25% vs 15.06%).

**Recommendation**: Establish premium customer success program with dedicated relationship managers, exclusive benefits, and proactive engagement.

---

## 🔬 Methodology

### Data Quality
- ✅ 10,000 customer records
- ✅ Zero missing values
- ✅ No duplicate records
- ✅ Complete data validation

### Segmentation Dimensions
1. **Geographic**: France, Spain, Germany
2. **Age Groups**: <30, 30-45, 46-60, 60+
3. **Credit Score**: Low (<580), Medium (580-670), High (670+)
4. **Tenure**: New (0-2yr), Mid (3-5yr), Long (6-10yr)
5. **Balance**: Zero, Low (<€100K), High (€100K+)
6. **High-Value**: Balance >€100K OR Salary >€100K

### Statistical Validation
All findings validated with independent samples t-tests:
- Age difference: p<0.001 (highly significant)
- Balance difference: p<0.001 (highly significant)
- Credit score difference: p<0.01 (significant)

---

## 🎓 Technical Details

### Analysis Framework
- **Language**: Python 3.x
- **Core Libraries**: pandas, numpy, matplotlib, seaborn, scipy
- **Dashboard**: Streamlit
- **Statistical Methods**: Independent t-tests, chi-square tests
- **Visualization**: 12-panel comprehensive suite

### Code Structure
- Object-oriented design with ChurnAnalyzer class
- Modular analysis pipeline
- Professional error handling
- Comprehensive documentation

---

## 📧 Contact & Support

For questions about the analysis methodology, findings, or recommendations:

**Project Type**: Professional Data Analytics
**Domain**: Banking & Financial Services
**Geographic Scope**: European Union (France, Spain, Germany)
**Data Source**: European Banking Dataset (2025)

---

## ✅ Quality Assurance

- ✓ Data validated for completeness and accuracy
- ✓ Statistical significance testing performed
- ✓ Cross-validation of findings
- ✓ Peer review of methodology
- ✓ Professional documentation standards
- ✓ Reproducible analysis pipeline

---

## ✅ Live Dashboard

- https://customer-segmentation-churn-pattern-analytics.streamlit.app/

---

**Analysis Date**: February 2026
**Report Version**: 1.0
**Status**: Final Deliverable

---

*This project demonstrates professional-grade data analytics capabilities in customer behavior analysis, predictive modeling, and strategic business intelligence.*
