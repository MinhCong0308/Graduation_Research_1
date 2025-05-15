import json
import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="Graduation_Research_1",
    user="postgres",
    password="03082004"
)
cur = conn.cursor()

# Open and load the JSON file
with open('G:/Graduation_Research_1/crawler/product.json') as json_file:
    data = json.load(json_file)

# Insert each record into the table
for record in data:
    cur.execute("""
        INSERT INTO laptop (prod_name, brand, cpu, gpu, ram, screen_size, screen_fresh_rate, N
                            screen_resolution, battery, battery_capacity, os, weight, price) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (record['prod_name'], record['brand'], record['cpu'], record['gpu'], record['ram'], 
          record['screen_size'], record['screen_fresh_rate'], record['screen_resolution'], 
          record['battery'], record['battery_capacity'], record['os'], 
          record['weight'], record['cost']))

# Commit changes and close connection
conn.commit()
cur.close()
conn.close()
