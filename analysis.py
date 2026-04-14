# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import seaborn as sns

# # # Optional styling
# # sns.set()

# # # Load dataset
# # df = pd.read_csv("healthcare_dataset.csv")

# # print(df.head())

# # # ---------------------------
# # # 1. Age Distribution
# # # ---------------------------
# # plt.figure()
# # plt.hist(df['Age'], bins=20)
# # plt.title("Age Distribution")
# # plt.xlabel("Age")
# # plt.ylabel("Count")
# # plt.savefig("age_distribution.png")
# # plt.show()

# # # ---------------------------
# # # 2. Most Frequent Diagnoses (FIXED)
# # # ---------------------------
# # counts = df['Medical Condition'].value_counts()

# # plt.figure()
# # plt.bar(counts.index, counts.values)
# # plt.title("Most Frequent Diagnoses")
# # plt.xlabel("Disease")
# # plt.ylabel("Count")
# # plt.xticks(rotation=45)
# # plt.savefig("diagnosis.png")
# # plt.show()

# # # ---------------------------
# # # 3. Billing Amount Over Time
# # # ---------------------------
# # df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
# # df = df.sort_values(by='Date of Admission')

# # plt.figure()
# # plt.plot(df['Date of Admission'], df['Billing Amount'])
# # plt.title("Billing Amount Over Time")
# # plt.xlabel("Date")
# # plt.ylabel("Billing Amount")
# # plt.xticks(rotation=45)
# # plt.savefig("time_trend.png")
# # plt.show()

# # # ---------------------------
# # # 4. Relationship Between Vitals
# # # ---------------------------
# # plt.figure()
# # plt.scatter(df['Age'], df['Billing Amount'])
# # plt.title("Age vs Billing Amount")
# # plt.xlabel("Age")
# # plt.ylabel("Billing Amount")
# # plt.savefig("relationship.png")
# # plt.show()

# # # ---------------------------
# # # Insights (Report)
# # # ---------------------------
# # print("\n--- Insights ---")
# # print("Average Age:", df['Age'].mean())
# # print("Most Common Disease:", df['Medical Condition'].mode()[0])
# # print("Max Billing:", df['Billing Amount'].max())

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

# Load dataset
df = pd.read_csv("healthcare_dataset.csv")

print(df.head())

# Convert date column
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])

# ---------------------------
# 1. Age Group Distribution (Clean)
# ---------------------------
bins = [0, 20, 40, 60, 80, 100]
labels = ["0-20", "20-40", "40-60", "60-80", "80+"]

df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

age_counts = df['Age Group'].value_counts().sort_index()

plt.figure()
plt.bar(age_counts.index.astype(str), age_counts.values)
plt.title("Age Group Distribution")
plt.xlabel("Age Groups")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.savefig("age_group.png")
plt.show()

# ---------------------------
# 2. Average Billing by Diagnosis (Meaningful Insight)
# ---------------------------
diagnosis_billing = df.groupby('Medical Condition')['Billing Amount'].mean().sort_values(ascending=False)

plt.figure()
plt.bar(diagnosis_billing.index, diagnosis_billing.values)
plt.title("Average Billing by Diagnosis")
plt.xlabel("Medical Condition")
plt.ylabel("Average Billing")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("diagnosis_better.png")
plt.show()

# ---------------------------
# 3. Monthly Billing Trend (Clean X-axis)
# ---------------------------
monthly = df.groupby(df['Date of Admission'].dt.to_period('M'))['Billing Amount'].mean()

# convert period to timestamp
monthly.index = monthly.index.to_timestamp()

plt.figure()
plt.plot(monthly.index, monthly.values)

# show fewer ticks (yearly)
plt.xticks(monthly.index[::12], rotation=45)

plt.title("Average Monthly Billing Trend")
plt.xlabel("Year")
plt.ylabel("Average Billing")
plt.tight_layout()
plt.savefig("monthly_trend.png")
plt.show()

# ---------------------------
# 4. Age vs Billing (Clean Scatter)
# ---------------------------
sample_df = df.sample(500)

plt.figure()
plt.scatter(sample_df['Age'], sample_df['Billing Amount'])
plt.title("Age vs Billing (Sampled Data)")
plt.xlabel("Age")
plt.ylabel("Billing Amount")
plt.tight_layout()
plt.savefig("clean_scatter.png")
plt.show()

# ---------------------------
# Insights (Report)
# ---------------------------
print("\n--- Insights ---")
print("Average Age:", round(df['Age'].mean(), 2))
print("Most Common Disease:", df['Medical Condition'].mode()[0])
print("Average Billing:", round(df['Billing Amount'].mean(), 2))
print("Highest Billing Disease:", diagnosis_billing.idxmax())