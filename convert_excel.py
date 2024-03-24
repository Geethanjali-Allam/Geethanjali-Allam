import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect(r'C:\Users\geeth\OneDrive\Desktop\capstone\geethanjali-allam\db.sqlite3')

# Execute SQL query to fetch data
cursor = conn.cursor()
cursor.execute('SELECT * FROM Management_employee')

# Fetch all rows
rows = cursor.fetchall()

# Create a DataFrame from the fetched data
df = pd.DataFrame(rows, columns=[col[0] for col in cursor.description])

# Export DataFrame to Excel
df.to_excel('output2.xlsx', index=False)

# Close the database connection
conn.close()