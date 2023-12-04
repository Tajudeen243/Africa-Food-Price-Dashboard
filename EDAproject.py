import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_csv("datasets/africa_food_prices.csv")

# Data Cleaning and Transformation

# Drop multiple Columns
df.drop(columns = ["mp_commoditysource","Unnamed: 0"], inplace = True)

# Group by 'country' and fill missing 'state' values with most frequent state in each country
df['state'] = df.groupby('country')['state'].transform(lambda x: x.fillna(x.mode()[0]
                                                                          if not x.mode().empty else "Unknown"))

# Main content of the dashboard
st.title("African Food Prices Dashboard")

# 1. Most common commodities purchased
st.header("Most Common Commodities Purchased")
common_commodities = df['market'].value_counts().nlargest(10)
st.bar_chart(common_commodities, color="#d4af37")

# 2. Prices variation between different market types
st.header("Prices Variation Between Different Market Types")
market_type_prices = df.groupby('market_type')['price'].mean()
st.bar_chart(market_type_prices)

# 3. Seasonal pattern in food prices
st.header("Seasonal Pattern in Food Prices")
monthly_prices = df.groupby('month')['price'].mean()
plt.plot(monthly_prices.index, monthly_prices.values)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

# 4. Notable differences in prices between countries
st.header("Notable Differences in Prices Between Countries")
country_prices = df.groupby('country')['price'].mean()
st.bar_chart(country_prices)

# 5. Relationship between quantity exchanged and price paid
st.header("5. Relationship Between Quantity Exchanged and Price Paid")
sns.scatterplot(data=df, x='quantity', y='price')
st.pyplot()

st.markdown("---")
st.markdown("*Dashboard created by Muhammad Tajudeen*")