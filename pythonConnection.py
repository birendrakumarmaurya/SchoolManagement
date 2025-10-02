import mysql.connector

# Connect to MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",        # change if you set another username
        password="sunbeam",  # replace with your MySQL root password
        database="schools"   # create this DB first or remove this line
    )

    if conn.is_connected():
        print("✅ Connected to MySQL successfully!")

    conn.close()

except mysql.connector.Error as e:
    print(f"❌ Error: {e}")
