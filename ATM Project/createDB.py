import mysql.connector

con=mysql.connector.connect(host="localhost",
                    user="root",
                    passwd="ironman")
cur=con.cursor()
cdb="create database NareshIT"
cur.execute(cdb)
print("Database Created as {NareshIT} Successfully....Verify")
