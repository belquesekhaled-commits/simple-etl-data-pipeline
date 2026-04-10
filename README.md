# Simple ETL Data Pipeline

A beginner-friendly **Data Engineering** project that demonstrates a simple ETL pipeline using **Python, Pandas, and SQLite**.

## Project Idea
This project takes raw e-commerce sales data from a CSV file, cleans and transforms it, then loads the final data into a SQLite database.

## ETL Flow
**Extract** → Read raw CSV data  
**Transform** → Clean missing values, remove duplicates, standardize columns, calculate total sales  
**Load** → Store the cleaned data in SQLite and export a cleaned CSV file

## Tools Used
- Python
- Pandas
- SQLite
- SQL

## Project Structure
```bash
simple-etl-data-pipeline/
├── data/
│   ├── raw_sales_data.csv
│   └── cleaned_sales_data.csv
├── sql/
│   └── analysis_queries.sql
├── etl.py
├── requirements.txt
├── sales.db
├── .gitignore
└── README.md
```

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the ETL script:
   ```bash
   python etl.py
   ```

## Output
After running the script, you will get:
- `cleaned_sales_data.csv`
- `sales.db` with a table called `sales_cleaned`

## Sample SQL Questions
- What is the total sales amount by category?
- Which city has the highest total sales?
- How many orders were placed per month?

## Why this project?
This project is small, clear, and perfect for a beginner Data Engineer portfolio on GitHub because it shows:
- ETL understanding
- Data cleaning
- Basic database loading
- Python + SQL workflow

## Author
**Belquese Khaled Sahm**