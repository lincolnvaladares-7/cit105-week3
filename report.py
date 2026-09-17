import csv

orders = {}
customers = set()
rejected = []

with open('orders.csv', mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    
    for line_num, row in enumerate(csv_reader, start=2):
        try:
            order_id, customer, item, qty, price = row
            
            qty = int(qty)
            price = float(price)
            
            if qty <= 0:
                raise ValueError("Quantity must be greater than zero")
            
            # Store valid data using order_id as the key
            # Mapping order_id to a dictionary or list of details
            orders[order_id] = {'customer': customer, 'item': item, 'qty': qty, 'price': price}
            
            # Add customer name to the unique set
            customers.add(customer)
                
        except ValueError as e:
            rejected.append((line_num, row, str(e)))
# --- Calculations ---

# 1. Total revenue = sum of qty × price for valid orders
total_revenue = sum(order['qty'] * order['price'] for order in orders.values())

# 2. Valid orders count
valid_orders_count = len(orders)

# 3. Unique customers count
unique_customers_count = len(customers)

# 4. Highest single order value (largest qty × price)
if orders:
    highest_single_order = max(order['qty'] * order['price'] for order in orders.values())
else:
    highest_single_order = 0.0

# 5. Rejected rows count
rejected_rows_count = len(rejected)


# --- Write Results to summary.txt ---

with open('summary.txt', mode='w', encoding='utf-8') as summary_file:
    summary_file.write(f"Total Revenue: ${total_revenue:,.2f}\n")
    summary_file.write(f"Valid Orders: {valid_orders_count}\n")
    summary_file.write(f"Unique Customers: {unique_customers_count}\n")
    summary_file.write(f"Highest Single Order: ${highest_single_order:,.2f}\n")
    summary_file.write(f"Rejected Rows: {rejected_rows_count}\n")
# --- Write Rejections to rejected.csv ---
# --- Write Rejections to rejected.csv ---

# Open rejected.csv in write mode
with open('rejected.csv', mode='w', newline='', encoding='utf-8') as rejected_file:
    csv_writer = csv.writer(rejected_file)

    # Write a clean, flat header row
    csv_writer.writerow(['Line Number', 'Order ID', 'Customer', 'Item', 'Qty', 'Price', 'Reason'])

    # Loop through the rejected collection
    for line_num, original_row, reason in rejected:
        # Write the rejected row
        csv_writer.writerow([line_num] + original_row + [reason])



   