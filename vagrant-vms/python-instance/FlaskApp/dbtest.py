#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("10.0.0.66","hamed","test","BucketList" )
#db = MySQLdb.connect("10.0.0.66","hamed","test","hamed" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

#sql = "select * from tbl_user"
#cursor.execute('''INSERT INTO tbl_user (username) VALUES ("test")''')
#cursor.callproc('GetAllProducts')

# testing store procedure
#cursor.callproc('pro1',('hello','hi','test'))

# another test
cursor.execute('''SELECT * FROM tbl_user''')


data = cursor.fetchall()
#print data
#db.commit()

# execute SQL query using execute() method.
#cursor.execute("show tables")

# Fetch a single row using fetchone() method.
#data = cursor.fetchone()

#print "Database version : %s " % data
print data
# disconnect from server
cursor.close()
db.close()
