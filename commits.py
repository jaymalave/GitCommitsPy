import sqlite3

conn = sqlite3.connect('commits.db')
cursor = conn.cursor()

date = input("Enter the date: ")
commits = int(input("Enter the no. of commits: "))

cursor.execute('INSERT INTO commits(DATE, COMMITS) VALUES (?, ?)', (  date  ,  commits   ))

conn.commit()   
print("success")

conn.close()

