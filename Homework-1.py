# Smart Patel - 196227 
# CIS 3368 - 25450
# Homework#01 
# references used in this code: https://www.w3schools.com/python/python_mysql_getstarted.asp, https://www.w3schools.com/python/python_mysql_insert.asp 

import mysql.connector

#connected to my awsdb through mysql for database storage
mydb = mysql.connector.connect(
    host= "cis3368-spring23.civhut35a9ka.us-east-1.rds.amazonaws.com",
    user="admin",
    passwd="Welcome3"
)
#used mycursor for using a db in mysql
def initDB():
    mycursor = mydb.cursor()
    mycursor.execute('USE CIS3368db')

#creating a menu options for selecting the entries
def menu():
    print('---MENU---')
    print('a - Add cases')
    print('o - Output all cases')
    print('q - Quit')

#for 'add cases' option added data entry steps for inserting all data
def addCases():
    mycursor = mydb.cursor()
    print("Covid Cases Entry \n")
    countryname=input('Enter Country name:')
    year=int(input('Enter year:'))
    totalcases=int(input('Enter total cases:'))
    deaths=int(input('Enter deaths:'))
    recovered=int(input('Enter recovered:'))

    sql = 'INSERT INTO `covidcases` (`countryname`,`year`,`totalcases`,`deaths`,`recovered`) VALUES (%s,%s,%s,%s,%s)'
    val=(countryname,year,totalcases,deaths,recovered)
    mycursor.execute(sql,val)
    mydb.commit()
    print('Inserted Successfully')
    exit()

def outputAllCases():
    mycursor = mydb.cursor()
    print('All Data')
    mycursor.execute("SELECT * FROM covidcases")
    covidlist=mycursor.fetchall()
    i=0
    for covidcases in covidlist:
        i+=1
        print("id:",covidcases[0])
        print("countryname:",covidcases[1])
        print("year:",covidcases[2])
        print("totalcases:",covidcases[3])
        print("deaths:",covidcases[4])
        print("recovered:",covidcases[5])
    exit()

#runs the option from the menu 
def run():
    menu()
    n = input('Please select your option:')
    if n=='a':
        addCases()
    elif n=='o':
        outputAllCases()
    elif n=='q':
        print('Exit')
    else:
        run()

if __name__ == '__main__':
    initDB()
    run()