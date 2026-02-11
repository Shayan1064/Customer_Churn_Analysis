Customer Churn Analysis
Project Overview

This project analyzes customer churn for a telecom company to understand which customers are likely to leave and identify factors influencing churn. Using Python, we clean, visualize, and preprocess data to uncover actionable insights for business decision-making and retention strategies.

Dataset

File: Customer_Churn.csv

Includes customer demographics, services subscribed, account info (tenure, contract, payment method, charges), and the target column Churn (Yes/No).

Technologies Used

Python: pandas, numpy

Visualization: matplotlib, seaborn

Data Preprocessing: StandardScaler, get_dummies

Key Steps

Data Cleaning

Converted TotalCharges to numeric

Handled missing values and cleaned categorical columns

Exploratory Data Analysis

Counted churned vs non-churned customers

Visualized churn distribution (green = stayed, red = churned)

Explored churn across features like tenure, contract type, payment method, and services

High-Risk Customers

Identified customers most likely to churn: month-to-month contracts, Electronic Check payments, and tenure < 12 months

Preprocessing for Modeling

Encoded categorical features

Scaled numerical features (tenure, MonthlyCharges, TotalCharges)

Insights

Month-to-month contracts and electronic check payments increase churn risk

Customers with short tenure (<12 months) are more likely to leave

Services like Online Security and Tech Support impact retention

Next Steps

Build predictive models to classify churn

Create interactive dashboards in Power BI or Tableau

Focus retention strategies on high-risk customer groups
