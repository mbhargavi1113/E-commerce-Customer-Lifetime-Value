import sys
import pandas as pd

from src.logger import logging
from src.exception import CustomException


def load_raw_data(data_path: str):
    try:
        logging.info("Starting data ingestion for Olist E-Commerce dataset")

        customers = pd.read_csv(
            f"{data_path}/olist_customers_dataset.csv"
        )

        orders = pd.read_csv(
            f"{data_path}/olist_orders_dataset.csv"
        )

        order_items = pd.read_csv(
            f"{data_path}/olist_order_items_dataset.csv"
        )

        payments = pd.read_csv(
            f"{data_path}/olist_order_payments_dataset.csv"
        )

        logging.info(
            f"Customers dataset loaded: {customers.shape[0]} rows, "
            f"{customers.shape[1]} columns"
        )

        logging.info(
            f"Orders dataset loaded: {orders.shape[0]} rows, "
            f"{orders.shape[1]} columns"
        )

        logging.info(
            f"Order items dataset loaded: {order_items.shape[0]} rows, "
            f"{order_items.shape[1]} columns"
        )

        logging.info(
            f"Payments dataset loaded: {payments.shape[0]} rows, "
            f"{payments.shape[1]} columns"
        )

        logging.info("Data ingestion completed successfully")

        return customers, orders, order_items, payments

    except Exception as e:
        logging.error("Error occurred during data ingestion")
        raise CustomException(e, sys)