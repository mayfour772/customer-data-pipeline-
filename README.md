# Customer Data Pipeline

A beginner-friendly Data Engineering practice project for learning Git, GitHub and VS Code.

## Project structure

- `data/customers.csv` — sample source customer data
- `scripts/etl_pipeline.py` — extracts, transforms and loads customer records
- `sql/customer_analysis.sql` — example business analysis queries
- `requirements.txt` — Python dependencies

## Run the pipeline

This example uses only Python's standard library, so no third-party package is required.

From the project root, run:

```bash
python scripts/etl_pipeline.py
```

The script creates `data/customers_processed.csv`.

## Practice tasks

1. Add a new customer row to the source CSV.
2. Update the ETL script to add a `customer_segment` field.
3. Add a SQL query to find the top customers by orders.
4. Track your changes with Git and push them to GitHub.
