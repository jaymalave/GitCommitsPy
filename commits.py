import sqlite3

conn = sqlite3.connect('commits.db')
cursor = conn.cursor()

def add():
 date = input("Enter the date: ")
 commits = int(input("Enter the no. of commits: "))

 cursor.execute('INSERT INTO commits(DATE, COMMITS) VALUES (?, ?)', (  date  ,  commits   ))

 conn.commit()   
 print("Commits Added!")

def view():
  for row in cursor.execute('SELECT * FROM commits'):
      date = row[0]
      commits = row[1]
      print(date, ':', commits)

def search():
   query = input("Enter the date you want to know the commits of: ")

   for row in cursor.execute('SELECT * FROM commits WHERE DATE = ?', (query,)):
      date = row[0]
      commits = row[1]
      print(date, ':', commits)



def close():
  conn.close()

ask = input("Press 'v' to view the commit stats, 's' to search for a particular date or 'a' to add one: ")

if ask == 'v':
    view()
    close()

if ask == 'a':
    add()
    close()

if ask == 's':
  search()
  close()




