import pandas as pd



df = pd.read_csv('product_detail.csv')

# # Remove duplicates based on all columns
# df = df.drop_duplicates()
# df= df.drop(columns=['product_link'])
# df['discount_percentage'] = df['discount_percentage'].str.replace('%', '')
# df['rating'] = df['rating'].str.replace(',', '').astype(float)
# df['rating_count'] = df['rating_count'].str.replace(',', '').astype(int)
# # Print the distinct DataFrame
# print(df.iloc[1281])
df['category']= df['category'].str.split(',').str[0]
df.to_csv("product_detail1.csv", index=False)
