# a = int(input("Entyer a number"))
# i=0
# while i<a:
#     print(a+1)
#     i+=1

# name = input("Enter your name")
# print(name)

# r= 5
# for i in range(1, r+1):
#    print("*"*i)

# Recommended: install if not already done (run in terminal once)
# pip install sqlalchemy pandas pymysql

from sqlalchemy import create_engine
import pandas as pd

# Replace these with your actual details
engine = create_engine(
    "mysql+pymysql://your_username:your_password@localhost/your_database_name"
)

# Example query - change table name as needed
df = pd.read_sql("SELECT * FROM your_table LIMIT 10", engine)

print(df)
