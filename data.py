import pandas as pd
import matplotlib.pyplot as plt
# Pandas is imported to assist with reading csv files and matplotlib is imported to handle visualizations
# Assign .read_csv() function to variable for ease of access
df = pd.read_csv('sales_data.csv')
# Utilize .head() function to 'preview' the first 5 items in the dataframe
print(df.head())
# .isnull() function locates missing values within each column, .sum() totals the missing values together to indicate how many missing values are in each column
print(df.isnull().sum())
# .fillna fills missing values with argument(0) and inplace directly edits the dataframe so that the df variable does not need to be reassigned with the new information
df.fillna(0, inplace=True)
# The sum of all total_sales is assigned to total_revenue
total_revenue = df["Sales_Amount"].sum()
print("Total Revenue:", total_revenue)
# Group the dataframe by product id and find the sum of each product's quantity_sold column. It then returns the product with the largest quantity sold
best_seller = df.groupby("Product_ID")["Quantity_Sold"].sum().idxmax()
print("Best Selling Product:", best_seller)
# Group the dataframe by Sale_Date and find the sum of Total_Sales for each date, returns the date with the largest Total_Sales sum
highest_revenue_day = df.groupby("Sale_Date")["Sales_Amount"].sum().idxmax()
print("Highest Revenue Day:", highest_revenue_day)
# Visualization -- Grouping the dataframe by sales date, find the sum of Total_Sales then plot it on the graph, specifies line for line plot, and the size of the graph
# Specify the title using plt.title, x-axis labeling with .xlabel and y-axis labeling with ylabel, generate graph with plt.show()
df.groupby("Sale_Date")["Sales_Amount"].sum().plot(kind="line", figsize=(10,5))
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.show()