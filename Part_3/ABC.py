import sqlite3
from sqlite3 import Error
import sys
import argparse

sys.builtin_module_names

def create_connection(db_file):
   
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor=conn.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        print("Connection Established " + sqlite3.version)
    except Error as e:
        print(e)
    return conn
    
# if __name__ == '__main__':
#     create_connection(r"Part_3/ABC.sqlite")
    

def close_connection(conn):
     conn.close
     print("The connection with the database has been closed. ")

"""
insert: define functions here
"""

def select_questionOne(conn, other):
    """
    Query Sites by address
    :param conn: the connection object
    :param other: Address given in query
    :return:
    """
    print("in question one")
 
    cur=conn.cursor()

    wrapped_other = ("%%"+other+"%%",)

    cur.execute("SELECT * FROM Site WHERE address LIKE ?", wrapped_other)
    
    records = cur.fetchall()


    if((len(records)) != 0):
        for row in records: 
            print(row)
    else:
        print ("No matching rows returned.") 
   
    
    close_connection(conn)

def select_questionTwo(conn, schedulerSystemInput):
    """
    Query DigitalDisplay, Specializes, TechnicalSupport by schedularSystem
    :param conn: the connection object
    :param schedularSystemInput: schedularSystem entered in query
    :return:
    """
    cur=conn.cursor()
    cur.execute("SELECT serialNo, DigitalDisplay.modelNo, name FROM DigitalDisplay, Specializes, TechnicalSupport WHERE DigitalDisplay.modelNo=Specializes.modelNo AND Specializes.empId=TechnicalSupport.empId AND schedulerSystem = ?", (schedulerSystemInput,))
    records = cur.fetchall()

    if((len(records)) != 0):
        for row in records: 
            print(row)
    else:
        print ("No matching rows returned.") 
         
  
    close_connection(conn)

def select_questionThree(conn, other):
    """
    Query DigitalDisplay, Specializes, TechnicalSupport 
    :param conn: the connection object
    :return:
    """
    cur=conn.cursor()
    cur.execute("SELECT COUNT(DISTINCT name) AS cnt, name AS Name FROM Salesman WHERE (empId, name, gender) IN (SELECT empId, name, gender FROM SalesMan WHERE Name = Name) GROUP BY name ORDER BY name ASC") 
    records = cur.fetchall()

    if((len(records)) != 0):
        for row in records: 
            print(row)
           
    else:
        print ("Empty Table.") 
         
   
    close_connection(conn)




def main(question_num, other):
    database = (r"Part_3/ABC.sqlite")
    conn= create_connection(database)
    print("in main, question_num = " + question_num)
    
    if(question_num=='1'):
        print('calling question one')
        if other is None:
            #error message here
            print("Missing parameter.")
            return 1
        select_questionOne(conn, other)

    elif(question_num=='2'):
        if other is None: 
            print("Missing parameter.")
            return 1
        select_questionTwo(conn, other)
    elif(question_num=='3'):
        select_questionThree(conn, other)
    else:
        close_connection(conn)
        return 1
            
        
if __name__ == '__main__':
    print(sys.argv)
    if (len(sys.argv) >= 3):
        main(sys.argv[1], sys.argv[2])
        if (len(sys.argv) > 3):
            main(sys.argv[1], sys.argv[2:])
       

    else:
        main(sys.argv[1], None)
    

