import pandas as pd


df = pd.read_csv('preprocessed_user.csv')

distinct_values = df['user_name'].unique()
new_df= pd.DataFrame({'user_name': distinct_values})
new_df['password']='12345'
new_df.to_csv("user_detail.csv", index=False)