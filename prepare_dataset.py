import numpy as np
import pandas as pd
import os

np.random.seed(101)
n = 2000

cities = ['Bengaluru', 'Delhi NCR', 'Mumbai', 'Hyderabad']
cuisines = ['North Indian', 'Biryani', 'Pizza/Fast Food', 'Chinese', 'South Indian', 'Desserts']
payment_methods = ['UPI', 'Credit Card', 'Debit Card', 'Cash on Delivery']

data = {
    'order_id': [f"ORD{20260000 + i}" for i in range(n)],
    'city': np.random.choice(cities, size=n, p=[0.35, 0.30, 0.20, 0.15]),
    'cuisine': np.random.choice(cuisines, size=n, p=[0.25, 0.25, 0.20, 0.15, 0.10, 0.05]),
    'order_value_inr': np.round(np.random.gamma(shape=5, scale=90, size=n), 0),
    'discount_applied_inr': np.random.choice([0, 50, 100, 150, 200], size=n, p=[0.3, 0.3, 0.2, 0.1, 0.1]),
    'delivery_time_mins': np.random.normal(38, 12, size=n).astype(int),
    'customer_rating': np.random.choice([1, 2, 3, 4, 5], size=n, p=[0.05, 0.08, 0.17, 0.40, 0.30]),
    'payment_mode': np.random.choice(payment_methods, size=n, p=[0.60, 0.20, 0.10, 0.10])
}

df = pd.DataFrame(data)

# Business logic: minimum order value constrain
df['order_value_inr'] = df['order_value_inr'].apply(lambda x: max(x, 149.0))
df['delivery_time_mins'] = df['delivery_time_mins'].apply(lambda x: max(x, 15))

# Commission revenue (average 22% platform cut)
df['platform_commission_inr'] = np.round(df['order_value_inr'] * 0.22, 2)

# Save to CSV
os.makedirs('data', exist_ok=True)
df.to_csv('data/restaurant_orders.csv', index=False)
print("SUCCESS: 2,000 records successfully generated in 'data/restaurant_orders.csv'!")