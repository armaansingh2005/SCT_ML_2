# K-Means Clustering - Retail Customer Segmentation

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Create customer purchase history dataset
data = {
    'Customer_ID': range(1, 16),
    'Number_of_Purchases': [
        2, 3, 4, 5, 3,
        10, 12, 11, 13, 9,
        20, 22, 19, 25, 21
    ],
    'Total_Spent': [
        500, 700, 900, 1000, 800,
        2500, 2800, 2600, 3000, 2300,
        5500, 6000, 5200, 6500, 5800
    ]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

print("Customer Purchase History:")
print(df)

# Select features for clustering
X = df[['Number_of_Purchases', 'Total_Spent']]

# Create K-Means model
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

# Apply K-Means clustering
df['Cluster'] = kmeans.fit_predict(X)

# Display results
print("\nCustomer Groups:")
print(df)

# Display cluster centers
print("\nCluster Centers:")
print(kmeans.cluster_centers_)

# Visualize the clusters
plt.figure(figsize=(8, 6))

plt.scatter(
    df['Number_of_Purchases'],
    df['Total_Spent'],
    c=df['Cluster'],
    s=100
)

# Plot cluster centers
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    marker='X',
    s=200,
    label='Cluster Centers'
)

plt.xlabel("Number of Purchases")
plt.ylabel("Total Amount Spent")
plt.title("Retail Customer Segmentation using K-Means")
plt.legend()
plt.show()

# Predict group for a new customer
purchases = int(input("\nEnter number of purchases: "))
spent = float(input("Enter total amount spent: "))

new_customer = [[purchases, spent]]

cluster = kmeans.predict(new_customer)

print("New customer belongs to Cluster:", cluster[0])