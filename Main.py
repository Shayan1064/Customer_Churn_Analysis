import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("Customer_Churn.csv")
# print(df.head())



df['TotalCharges'] = df['TotalCharges'].replace(" ", "0")
df["TotalCharges"]=df["TotalCharges"].astype('float')


# print(df.info())

# print(df.isnull().sum())
# print(df.duplicated().sum())

def converter(value):
    if value==0:
        return "No"
    else:
        return "Yes"
    
df['SeniorCitizen']=df["SeniorCitizen"].apply(converter)

# print(df.head())

churn_counts = df['Churn'].value_counts()
print(churn_counts)

colors = ['#2E8B57' if label == 'No' else '#C0392B' for label in churn_counts.index]

plt.figure(figsize=(8,5))
bars = plt.bar(churn_counts.index, churn_counts.values, color=colors, width=0.6)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

total = len(df)

for bar in bars:
    height = bar.get_height()
    percentage = (height / total) * 100
    plt.text(bar.get_x() + bar.get_width()/2,
             height,
             f'{height:,}\n({percentage:.1f}%)',
             ha='center',
             va='bottom',
             fontsize=11,
             fontweight='bold')

plt.title("Customer Churn Distribution", fontsize=14, fontweight='bold')
plt.xlabel("Churn Status", fontsize=12)
plt.ylabel("Number of Customers", fontsize=12)

plt.tight_layout()
plt.show()


plt.figure(figsize=(9,4))
plt.hist(df['tenure'], bins=30, color='#2E8B57', edgecolor='black')  # bins = number of bars
plt.title("Distribution of Customer Tenure")
plt.xlabel("Tenure (months)")
plt.ylabel("Number of Customers")
plt.show()

categorical_cols = ['gender','SeniorCitizen','Partner','Dependents','PhoneService','MultipleLines',
                    'InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport',
                    'StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod']

for col in categorical_cols:
    plt.figure(figsize=(6,4))
    sns.countplot(data=df, x=col, hue='Churn', palette='Set2')
    plt.title(f'{col} vs Churn')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

tenure_churn = df.groupby('tenure')['Churn'].value_counts(normalize=True).unstack()
tenure_churn.plot(kind='line', figsize=(8,5))
plt.title("Churn Rate by Tenure")
plt.ylabel("Churn Rate")
plt.show()


payment_churn = df.groupby('PaymentMethod')['Churn'].value_counts(normalize=True).unstack()
payment_churn.plot(kind='bar', stacked=True, figsize=(8,5), colormap='Set3')
plt.title("Churn by Payment Method")
plt.show()


contract_churn = df.groupby('Contract')['Churn'].value_counts(normalize=True).unstack()
contract_churn.plot(kind='bar', stacked=True, figsize=(6,4), colormap='Paired')
plt.title("Churn by Contract Type")
plt.show()


service_cols = ['OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies']

for col in service_cols:
    service_churn = df.groupby(col)['Churn'].value_counts(normalize=True).unstack()
    service_churn.plot(kind='bar', stacked=True, figsize=(6,4), colormap='Accent')
    plt.title(f"{col} vs Churn")
    plt.show()

high_churn_risk = df[(df['Contract']=='Month-to-month') & 
                     (df['PaymentMethod']=='Electronic check') & 
                     (df['tenure']<12)]
print(high_churn_risk.head())

df_encoded = pd.get_dummies(df, drop_first=True)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df_encoded[['tenure','MonthlyCharges','TotalCharges']] = scaler.fit_transform(df_encoded[['tenure','MonthlyCharges','TotalCharges']])
