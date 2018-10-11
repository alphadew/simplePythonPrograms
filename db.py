import pymysql
db=pymysql.connect("localhost","root","cetmca","pylearn")
cursor=db.cursor()
cursor.execute("select version()")
data=cursor.fetchone()
print(data)
