
# 🧾 Vendor Performance Analysis – Retail Inventory & Sales

_Analyzing vendor efficiency and profitability to support strategic purchasing and inventory decisions using SQL, Python, and Power BI._

---

## 📌 Table of Contents
- <a href="#overview">Overview</a>
- <a href="#business-problem">Business Problem</a>
- <a href="#dataset">Dataset</a>
- <a href="#tools--technologies">Tools & Technologies</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#data-cleaning--preparation">Data Cleaning & Preparation</a>
- <a href="#exploratory-data-analysis-eda">Exploratory Data Analysis (EDA)</a>
- <a href="#research-questions--key-findings">Research Questions & Key Findings</a>
- <a href="#dashboard">Dashboard</a>
- <a href="#how-to-run-this-project">How to Run This Project</a>
- <a href="#final-recommendations">Final Recommendations</a>
- <a href="#author--contact">Author & Contact</a>

---
<h2><a class="anchor" id="overview"></a>Overview</h2>

This project evaluates vendor performance and retail inventory dynamics to drive strategic insights for purchasing, pricing, and inventory optimization. A complete data pipeline was built using SQL for ETL, Python for analysis and Power BI for visualization.

---
<h2><a class="anchor" id="business-problem"></a>Business Problem</h2>

Effective inventory and sales management are critical in the retail sector. This project aims to:
- Identify underperforming brands needing pricing or promotional adjustments
- Determine vendor contributions to sales and profits
- Analyze the cost-benefit of bulk purchasing
- Investigate inventory turnover inefficiencies
- Statistically validate differences in vendor profitability

---
<h2><a class="anchor" id="dataset"></a>Dataset</h2>

- Multiple CSV files located in `/data/` folder (sales, vendors, inventory)
- Summary table created from ingested data and used for analysis

---

<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>

- SQL (Common Table Expressions, Joins, Filtering)
- Python (Pandas, Matplotlib, Seaborn)
- Power BI (Interactive Visualizations)
- GitHub

---
<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

```
vendor-performance-analysis/
│
├── README.md
├── .gitignore
├── requirements.txt
├── Vendor Performance Report.pdf
│
├── notebooks/                  # Jupyter notebooks
│   ├── Exploratory_data_analysis.ipynb
│   ├── Vendor_performance_analysis.ipynb
│
├── scripts/                    # Python scripts for ingestion and processing
│   ├── csv_to_sql.py
│
├── dashboard/                  # Power BI dashboard file
│   └── vendor_performance_dashboard.pbix
```

---
<h2><a class="anchor" id="data-cleaning--preparation"></a>Data Cleaning & Preparation</h2>

- Removed transactions with:
  - Gross Profit ≤ 0
  - Profit Margin ≤ 0
  - Sales Quantity = 0
- Created summary tables with vendor-level metrics
- Converted data types, handled outliers, merged lookup tables

---
<h2><a class="anchor" id="exploratory-data-analysis-eda"></a>Exploratory Data Analysis (EDA)</h2>

**Negative or Zero Values Detected:**
- Gross Profit: Min -175,969.74 (loss-making sales)
- Profit Margin: Min -23.78 (sales at zero or below cost)
- Unsold Inventory: Indicating slow-moving stock

**Outliers Identified:**
- High Freight Costs 
- Large Purchase/Actual Prices

**Correlation Analysis:**
- Weak between Delivery Days Delay & Fulfillment Rate (-0.83)
- Strong between Purchase Qty & Sales Qty (0.999)
- Strong between Profit Margin & Sales Revenue (0.86)

---
<h2><a class="anchor" id="research-questions--key-findings"></a>Research Questions & Key Findings</h2>

1. **Brands for Promotions**: 9 brands with low sales but high profit margins
2. **Top Vendors**: Top 10 vendors = 4% of purchases → Highly fragmented
3. **Bulk Purchasing Impact**: 5.87% lower unit cost vs higher cost in lower orders 
4. **Inventory Turnover**: $6.27B worth of unsold inventory
5. **Vendor Profitability**:
   - High Vendors: Mean Margin = 18.5%
   - Low Vendors: Mean Margin = 8.5%

---
<h2><a class="anchor" id="dashboard"></a>Dashboard</h2>

- Power BI Dashboard shows:
  - Vendor-wise Sales and Margins
  - Inventory Turnover
  - Bulk Purchase Savings
  - Performance Heatmaps

![Vendor Performance Dashboard]("D:\VISHAL\Portfolio Project\Vendor Performance Analysis\images\dasdboard.png")

---
<h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>

1. Clone the repository:
```bash
git clone https://github.com/yourusername/vendor-performance-analysis.git
```
3. Load the CSVs and ingest into database:
```bash
python scripts/csv_to_sql.py
```
4. Open and run notebooks:
   - `notebooks/Exploratory_data_analysis.ipynb`
   - `notebooks/Vendor_performance_analysis.ipynb`
5. Open Power BI Dashboard:
   - `dashboard/vendor_performance_dashboard.pbix`

---
<h2><a class="anchor" id="final-recommendations"></a>Final Recommendations</h2>

- Consolidate & Strengthen Key Vendor Relationships
- Audit & Optimize Underperforming Vendors 
- Align Procurement with Demand
- Implement a Vendor Scorecard
- Reduce Inventory Risk
- Strengthen Contractual Accountability

---
<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>

**Vishal**  
Data Analyst  
📧 Email: vishal.ds7428@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/vishaldstech/)
