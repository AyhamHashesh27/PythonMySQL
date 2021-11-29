import mysql.connector as MySQLConnector

mydb = MySQLConnector.connect(host='localhost', user='root', password='password', database='university')
print('Connected!')

mycursor = mydb.cursor()

mycursor.execute("select * from student;")

students = mycursor.fetchall()

for student in students:
  print(student)