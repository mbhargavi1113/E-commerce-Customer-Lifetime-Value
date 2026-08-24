# E-commerce-Customer-Lifetime-Value

## Project Overview

This project focuses on predicting the Customer Lifetime Value (CLV) of e-commerce customers. The aim is to estimate how much value a customer is expected to bring to the business in the long term based on their previous purchases and buying behavior.

This can help an e-commerce business understand which customers are more valuable and make better decisions about customer retention and marketing.

## Dataset

For this project, I am using the **Online Retail Dataset** from the **UCI Machine Learning Repository**.

The dataset contains transaction information from an online retail store, including details such as invoices, products, quantities, prices, customer IDs, and transaction dates.

The purchase history will be used to understand customer behavior and create the features required for predicting Customer Lifetime Value.

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
├── requirements.txt
├── README.md
└── .gitignore
