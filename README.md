# E-commerce Customer Lifetime Value

## Project Overview

This project focuses on predicting the Customer Lifetime Value (CLV) of e-commerce customers.

The aim is to estimate how much value a customer is expected to bring to the business based on their previous purchases and buying behavior.

This can help an e-commerce business identify valuable customers and make better decisions about customer retention, marketing, and customer engagement.

## Dataset

For this project, I am using the Brazilian E-Commerce Public Dataset by Olist.

The dataset contains information about e-commerce orders, customers, products, sellers, payments, reviews, and product categories.

The datasets used in this project include:

- Customers
- Orders
- Order Items
- Order Payments
- Order Reviews
- Products
- Sellers
- Geolocation
- Product Category Translation

These datasets will be combined and processed to understand customer purchasing behavior and create features for predicting Customer Lifetime Value.

## Project Structure

```text
Predictive Analytics Project/
│
├── data/
│   └── raw/
│
├── notebooks/
│   └── 01_eda.ipynb
│
├── src/
│   ├── __init__.py
│   ├── logger.py
│   ├── exception.py
│   │
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   └── pipeline/
│       ├── train_pipeline.py
│       └── predict_pipeline.py
│
├── artifacts/
│
├── logs/
│
├── requirements.txt
├── README.md
└── .gitignore