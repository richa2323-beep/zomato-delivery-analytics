import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Visual style setup
sns.set_style('whitegrid')
os.makedirs('reports', exist_ok=True)

# 1. Load Data
df = pd.read_csv('data/restaurant_orders.csv')

print("="*60)
print("         RESTAURANT DELIVERY PERFORMANCE REPORT         ")
print("="*60)

# 2. Key Business Metrics (KPIs)
total_gross_revenue = df['order_value_inr'].sum()
total_commission = df['platform_commission_inr'].sum()
total_discounts = df['discount_applied_inr'].sum()
net_platform_profit = total_commission - total_discounts
avg_delivery_time = df['delivery_time_mins'].mean()
avg_rating = df['customer_rating'].mean()

print(f"Total Gross Merchandise Value (GMV): Rs. {total_gross_revenue:,.2f}")
print(f"Total Platform Commission Earned:   Rs. {total_commission:,.2f}")
print(f"Total Discounts Subsidized:          Rs. {total_discounts:,.2f}")
print(f"Net Platform Margin:                 Rs. {net_platform_profit:,.2f}")
print(f"Average Delivery Time:               {avg_delivery_time:.1f} mins")
print(f"Average Customer Satisfaction:       {avg_rating:.2f} / 5.0")
print("="*60)

# 3. City-Wise Performance
city_perf = df.groupby('city').agg(
    total_orders=('order_id', 'count'),
    revenue=('order_value_inr', 'sum'),
    avg_rating=('customer_rating', 'mean')
).reset_index()
print("\n--- CITY-LEVEL BREAKDOWN ---")
print(city_perf)

# 4. Chart 1: Revenue by Cuisine (Bar Chart)
cuisine_rev = df.groupby('cuisine')['order_value_inr'].sum().sort_values(ascending=False).reset_index()
plt.figure(figsize=(9, 5))
sns.barplot(data=cuisine_rev, x='order_value_inr', y='cuisine', palette='crest')
plt.title("Total GMV by Cuisine Category", fontsize=13, fontweight='bold')
plt.xlabel("Total Order Value (INR)")
plt.ylabel("Cuisine")
plt.tight_layout()
plt.savefig('reports/cuisine_revenue.png', dpi=300)
plt.close()

# 5. Chart 2: Delivery Time vs Customer Rating (Boxplot)
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='customer_rating', y='delivery_time_mins', palette='coolwarm_r')
plt.title("Impact of Delivery Time on Customer Rating", fontsize=13, fontweight='bold')
plt.xlabel("Customer Rating (1 to 5 Stars)")
plt.ylabel("Delivery Time (Minutes)")
plt.tight_layout()
plt.savefig('reports/delivery_vs_rating.png', dpi=300)
plt.close()

# 6. Chart 3: Payment Method Preference (Pie Chart)
pay_counts = df['payment_mode'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(pay_counts, labels=pay_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title("Payment Method Share", fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('reports/payment_share.png', dpi=300)
plt.close()

print("\nSUCCESS: All 3 charts successfully saved inside 'reports/' folder!")