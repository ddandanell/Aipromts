# Analysis Report: Q3 Sales Performance

## 1. Executive Summary
Q3 revenue grew 14% YoY, driven primarily by Electronics (+32%) and Home & Garden (+18%). The Northeast region underperformed vs. target by 11%.

## 2. Data Overview
- Period: January–September 2024
- Records: 8,640 rows across 4 product categories and 6 regions
- Data quality: 2.3% missing values in `units_sold` (imputed with category median)

## 3. Key Findings
- **Top category**: Electronics — $2.4M revenue (+32% YoY)
- **Lowest performer**: Apparel — $0.8M revenue (-5% YoY)
- **Best region**: Southwest — 118% of target
- **Underperforming region**: Northeast — 89% of target

## 4. Trends & Patterns
- Clear seasonal spike in Electronics in July (back-to-school effect)
- Home & Garden peaks in May–June; normalized by September
- Apparel decline correlates with reduced promotional activity (p < 0.01)

## 5. Recommendations
1. Increase Electronics inventory ahead of Q4 holiday season
2. Launch targeted promotions in the Northeast to close gap
3. Review Apparel promotional calendar for Q4

## 6. Data Quality Notes
- 2.3% missing values in `units_sold` imputed with category median
- 14 duplicate transaction records removed before analysis
