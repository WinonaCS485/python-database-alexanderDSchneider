import pymysql.cursors 

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='eb1391ck',
                             password='putty1562',
                             db='eb1391ck_university',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        f_name = input("Enter a first name to search: ")
        # l_name = input("Enter a last name to search:")
        
        print(f_name)
        # Select all Students 
       #  sql = "SELECT * from Student WHERE firstName LIKE %f_name'"
        sql = "SELECT * from Student where firstName = " + "'" + f_name + "'"
        # execute the SQL command
        cursor.execute(sql)
        
        # get the results
        for result in cursor:
            print (result)
        
      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()
        

finally:
    connection.close()


