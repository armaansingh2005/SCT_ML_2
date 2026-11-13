# 🛍️ K-Means Clustering – Retail Customer Segmentation

## 📌 Project Overview

This project implements an unsupervised Machine Learning algorithm, **K-Means Clustering**, to perform Retail Customer Segmentation based on customer purchasing behavior.

The model groups customers into different clusters using two important features:
- Number of Purchases
- Total Amount Spent

The project helps understand customer purchasing patterns and identify different customer segments based on their spending habits.

Developed as part of the **SkillCraft Technology – Machine Learning Internship (Task 2)**.

## 🎯 Project Objectives

- Implement the K-Means Clustering algorithm.
- Analyze customer purchasing behavior.
- Segment customers into meaningful groups.
- Identify customers based on purchasing frequency and spending.
- Visualize customer clusters using scatter plots.
- Predict the cluster of a new customer.

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn

## 📊 Dataset Description

The project uses a sample Retail Customer Purchase History dataset containing 15 customer records.

| Feature | Description |
|---|---|
| Customer_ID | Unique customer identification |
| Number_of_Purchases | Total number of purchases made |
| Total_Spent | Total amount spent by the customer |
| Cluster | Customer group assigned by K-Means |

## ⚙️ Project Workflow

1. **Data Creation:** Create a customer purchase history dataset.
2. **Data Preparation:** Convert the dataset into a Pandas DataFrame.
3. **Feature Selection:** Select Number of Purchases and Total Spent.
4. **Model Creation:** Initialize the K-Means Clustering algorithm.
5. **Clustering:** Divide customers into 3 different clusters.
6. **Cluster Centers:** Calculate the center points of each cluster.
7. **Visualization:** Display customer segments using a scatter plot.
8. **New Customer Prediction:** Predict the cluster for a new customer based on purchasing information.

## 🤖 Machine Learning Algorithm

### K-Means Clustering

K-Means is an unsupervised Machine Learning algorithm used to divide data points into groups called clusters based on their similarities.

**Model Configuration:**

- Algorithm: K-Means Clustering
- Number of Clusters (K): 3
- Random State: 42
- Initialization: 10

The algorithm groups customers according to their purchasing frequency and total spending.

## 📈 Visualization

The project generates a scatter plot representing:

- Customer distribution across different clusters.
- Purchasing frequency on the X-axis.
- Total spending on the Y-axis.
- Different colors representing customer clusters.
- Cluster centers represented by X-shaped markers.

## 🔍 New Customer Prediction

The project also includes an interactive prediction feature.

Users can enter:
- Number of purchases.
- Total amount spent.

The trained K-Means model predicts which customer cluster the new customer belongs to.

## 🚀 Installation & Execution

### 1. Clone the Repository

```bash
git clone https://github.com/armaansingh2005/SCT_ML_2.git
```

### 2. Navigate to the Project Directory

```bash
cd SCT_ML_2
```

### 3. Install Required Libraries

```bash
pip install pandas matplotlib scikit-learn
```

### 4. Run the Python File

```bash
python "k-means cluster algo.py"
```

### 5. Enter Customer Details

Enter the number of purchases and total amount spent when prompted to receive the predicted customer cluster.

## 💡 Key Learning Outcomes

- Understanding Unsupervised Machine Learning.
- Practical implementation of K-Means Clustering.
- Customer segmentation techniques.
- Working with Pandas DataFrames.
- Understanding cluster centers.
- Data visualization using Matplotlib.
- Making predictions for new customer data.

## 🔮 Future Improvements

- Use real-world retail customer datasets.
- Apply the Elbow Method to determine the optimal number of clusters.
- Implement feature scaling for better clustering.
- Develop an interactive customer segmentation dashboard.
- Compare K-Means with hierarchical clustering and DBSCAN.
- Generate personalized marketing recommendations for different customer segments.

## 👨‍💻 Author

**Armaan Singh**

B.Tech – Artificial Intelligence & Machine Learning  
Dronacharya College of Engineering, Gurugram

## 🏢 Internship Details

- **Organization:** SkillCraft Technology
- **Domain:** Machine Learning
- **Task:** Task 2
- **Project:** K-Means Clustering – Retail Customer Segmentation

---

⭐ If you find this project useful, consider giving the repository a star!
