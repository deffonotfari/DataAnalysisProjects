import pandas as pd
import matplotlib.pyplot as plt

df_student_dropout = pd.read_csv("students_dropout_academic_success.csv")
print(df_student_dropout.head())
print(df_student_dropout.columns)

# Count occurrences
target_counts = df_student_dropout['target'].value_counts()
marital_counts = df_student_dropout['Marital Status'].value_counts()

# Create subplots for side-by-side pie charts
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Pie chart for target
target_counts.plot.pie(ax=axes[0], autopct='%1.1f%%', startangle=90, ylabel='', title='Student Target Classes')

plt.tight_layout()
plt.show()
