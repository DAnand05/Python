import sqlite3

db=sqlite3.connect("student.db")
cursor=db.cursor()

'''cursor.execute("create table register(id integer primary key,name text,branch text,address text)")
'''

while True:
    choice = input("Do you want to create a new file? (Enter 'insert', 'delete' or 'exit'): ")
    if choice == "insert":
            id=int(input("Enter the id : "))
            name=input("Enter the name : ")
            age=int(input("Enter the age : "))
            cursor.execute(f"insert into register values({id},'{name}',{age})")
            print(cursor.lastrowid)
    elif choice == "delete":
            id=int(input("Enter the id to delete data : "))
            cursor.execute(f"delete from register where id={id}")
    elif choice == "exit":
            break
    else:
            print("Invalid choice. Please enter 'insert', 'delete' or 'exit'.")
'''cursor.execute("select * from register")
cursor.execute("insert into register values(1,'Anand',24)")
cursor.executemany("insert into register values(?,?,?)",[(2,"Deep",23),(3,"Diksha",26),(4,"Ajay",24)])
print(cursor.lastrowid)'''

db.commit()
'''if db:
    print("DB connectivity established")'''

db.close()