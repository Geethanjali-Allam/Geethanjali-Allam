import sqlite3
import pandas as pd


conn = sqlite3.connect(r'C:\Users\geeth\OneDrive\Desktop\capstone\geethanjali-allam\db.sqlite3')

cursor = conn.cursor()
cursor.execute('SELECT * FROM Management_employee')
rows = cursor.fetchall()
df = pd.DataFrame(rows, columns=[col[0] for col in cursor.description])
df.to_excel('output2.xlsx', index=False)
conn.close()