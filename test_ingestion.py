from src.components.data_ingestion import load_raw_data

data_path = "data/raw"

customers, orders, order_items, payments = load_raw_data(data_path)

print("Customers:", customers.shape)
print("Orders:", orders.shape)
print("Order Items:", order_items.shape)
print("Payments:", payments.shape)