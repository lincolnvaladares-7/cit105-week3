# cit105-week3
CIT 105 Week 3 CSV Parsing and Reporting Assignment
# CIT 105 Week 3 CSV Parsing and Reporting Assignment

This project reads order data from `orders.csv`, processes valid orders, and records damaged or invalid rows without stopping the program.

## Results

- Total Revenue: $48,016.30
- Valid Orders: 182
- Unique Customers: 171
- Highest Single Order: $1,377.00
- Rejected Rows: 18

## Rejected Rows

A total of **18 rows were rejected**.

Distinct reasons found in the data:

- Not enough values to unpack
- Too many values to unpack
- Invalid quantity: could not convert string to integer
- Invalid price: could not convert string to float
- Quantity must be greater than zero

Rejected rows and their specific error messages are saved in `rejected.csv`.
