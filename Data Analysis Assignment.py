import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

user_details = pd.read_excel("Data Analyst Intern Assignment - Excel.xlsx", sheet_name='UserDetails.csv')
cooking_sessions = pd.read_excel("Data Analyst Intern Assignment - Excel.xlsx", sheet_name='CookingSessions.csv')
order_details = pd.read_excel("Data Analyst Intern Assignment - Excel.xlsx", sheet_name='OrderDetails.csv')

user_details = user_details.drop_duplicates()
cooking_sessions = cooking_sessions.drop_duplicates()
order_details = order_details.drop_duplicates()

cooking_sessions['Session Start'] = pd.to_datetime(cooking_sessions['Session Start'])
cooking_sessions['Session End'] = pd.to_datetime(cooking_sessions['Session End'])

user_cooking_data = pd.merge(user_details, cooking_sessions, on='User ID', how='inner')
final_data = pd.merge(user_cooking_data, order_details, on='User ID', how='inner')

print("Columns in Final Data:", final_data.columns)

if 'Dish Name_x' in final_data.columns:
    final_data['Dish Name'] = final_data['Dish Name_x']
    final_data['Dish Name'] = final_data['Dish Name'].str.strip()
    popular_dishes = final_data['Dish Name'].value_counts().head(10)

    plt.figure(figsize=(10, 6))
    popular_dishes.plot(kind='bar', color='skyblue')
    plt.title('Top 10 Popular Dishes')
    plt.xlabel('Dish Name')
    plt.ylabel('Frequency')
    plt.xticks(rotation=25)
    plt.show()

else:
    print("Column 'Dish Name' not found. Please verify the dataset.")

sessions_orders_correlation = final_data[['Total Orders', 'Duration (mins)']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(sessions_orders_correlation, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap: Cooking Sessions vs Orders')
plt.show()
