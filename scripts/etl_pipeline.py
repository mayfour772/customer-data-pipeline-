"""A tiny example ETL script for the customer data project."""

import csv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_ROOT / "data" / "customers.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "customers_processed.csv"


def extract():
    """Read customer records from the source CSV."""
    with INPUT_FILE.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def transform(rows):
    """Add full name and customer segment."""
    transformed = []

    for row in rows:
        row["full_name"] = (
            f'{row["first_name"]} {row["last_name"]}'
        )

        orders = int(row["total_orders"])

        if orders >= 5:
            row["customer_segment"] = "Premium"
        else:
            row["customer_segment"] = "Regular"

        transformed.append(row)

   



def load(rows):
    """Write transformed records to a new CSV file."""
    fieldnames = list(rows[0].keys()) if rows else []
    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    source_rows = extract()
    clean_rows = transform(source_rows)
    load(clean_rows)
    print(f"Processed {len(clean_rows)} customers.")
    print(f"Output saved to: {OUTPUT_FILE}")
