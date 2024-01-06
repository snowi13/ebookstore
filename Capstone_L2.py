#eBookstore database where staff can enter, update, delete, search book data.

from datetime import date
import time
import sqlite3

db = sqlite3.connect('ebookstore_db')

cursor = db.cursor()

cursor.execute('CREATE TABLE book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, quantity INTEGER)')
db.commit()

id1 = 3001
title1 = 'A Tale of Two Cities'
author1 = 'Charles Dickens'
quantity1 = 30

id2 = 3002
title2 = "Harry Potter and the Philosopher's Stone"
author2 = 'J.K. Rowling'
quantity2 = 40

id3 = 3003
title3 = "The Lion, the Witch and the Wardrobe"
author3 = 'C.S. Lewis'
quantity3 = 25

id4 = 3004
title4 = "The Lord of the Rings"
author4 = 'J.R.R. Tolkien'
quantity4 = 37

id5 = 3005
title5 = "Alice in Wonderland"
author5 = 'Lewis Carroll'
quantity5 = 12


book_record = [(id1, title1, author1, quantity1),(id2, title2, author2, quantity2),(id3, title3, author3, quantity3),(id4, title4, author4, quantity4),(id5, title5, author5, quantity5)]

cursor.executemany('INSERT INTO book(id, title, author, quantity) VALUES(?,?,?,?)', book_record)

db.commit()

while True:

    menu = input('''\nPlease select one option below:
1. Enter book
2. Update book
3. Delete book
4. Search books
5. Display all books                
0. Exit
: ''')
    
    time.sleep(.5)
    
    if menu == '1': #enter books
        
        title = ''
        author = ''
        quantity = ''
     
        while True: #check input against existing ids, if ID exists or ivalid input, re-prompt until valid. 
                    #when valid, populate fields with above empty variables to be filled with data in subsequent inputs
            try:

                id = int(input("\nPlease enter a new id:\n"))
                time.sleep(.5)
                cursor.execute('INSERT INTO book(id, title, author, quantity) VALUES(?,?,?,?)', (id, title, author, quantity))
                db.commit()

            except sqlite3.IntegrityError as error:

                print('\n')
                print(error)
                print('ID already exists.')
                time.sleep(.5)
                continue
            
            except ValueError:

                print("\nYou have entered an invalid input. Please try again.")
                time.sleep(.5)
                continue

            else:

                break

        time.sleep(.5)  

        title = input("\nPlease enter the title:\n").lower()
        cursor.execute('UPDATE book SET title = ? WHERE ID = ?', (title, id))
        db.commit()
        time.sleep(.5)
        
        author = input("\nPlease enter the author:\n").lower()
        cursor.execute('UPDATE book SET author = ? WHERE ID = ?', (author, id))
        db.commit()
        time.sleep(.5)
        
        while True: #prompt until valid input

            try:

                quantity = int(input("\nPlease enter the quantity:\n"))
                cursor.execute('UPDATE book SET quantity = ? WHERE ID = ?', (quantity, id))
                db.commit()

            except ValueError:

                print("\nYou have entered an invalid input. Please try again.")
                time.sleep(.5)
                continue

            else:

                break

        time.sleep(.5)
        
    elif menu == '2': #update books
        
        while True: #only proceed when existing/valid id input
            
            try:

                id = int(input('\nWhat record id would you like to update:\n'))
                cursor.execute('SELECT id FROM book WHERE id = ?', (id,))
                
                for row in cursor: #checks if record with input id exists

                    if len(row) != 0:
                        
                        break
            
                else:

                    print("That ID is invalid please try again.")
                    continue

            except ValueError:

                print("\nYou have entered an invalid input. Please try again.")
                break

            sub_menu = input('''\nWhat would you like to update (one option):\n
a. title
b. author
c. quantity
z. exit sub-menu
: ''').lower()
            
            if sub_menu == 'a': 
                
                title = input('\nWhat would you like to update the title to:\n').lower()
                cursor.execute('UPDATE book SET title = ? WHERE id = ?', (title, id))
                db.commit()
                cursor.execute('SELECT * FROM book WHERE id = ?', (id,))

                time.sleep(.5)
                print(f'\nUpdate Record:')
                records_formatted = '{:<5} {:<50} {:<30} {:<6}' #format table for printing
                print(records_formatted.format("\nID", "Title", "Author", "Quantity"))
                
                for row in cursor:

                    print(records_formatted.format(*row))
                
                break

            elif sub_menu == 'b':

                author = input('\nWhat would you like to update the author to:\n').lower()
                cursor.execute('UPDATE book SET author = ? WHERE id = ?', (author, id))
                db.commit()
                cursor.execute('SELECT * FROM book WHERE id = ?', (id,))
                
                time.sleep(.5)
                print(f'\nUpdate Record:')
                records_formatted = '{:<5} {:<50} {:<30} {:<6}' #format table for printing
                print(records_formatted.format("\nID", "Title", "Author", "Quantity"))
                
                for row in cursor:

                    print(records_formatted.format(*row))
                
                break

            elif sub_menu == 'c':

                while True: #prompt until valid input

                    try:

                        quantity = int(input('\nWhat would you like to update the quantity to:\n'))
                        time.sleep(.5)

                    except ValueError:

                        print("\nYou have entered an invalid input. Please try again.")
                        time.sleep(.5)
                        continue

                    else:

                        break

                cursor.execute('UPDATE book SET quantity = ? WHERE id = ?', (quantity, id))
                db.commit()
                cursor.execute('SELECT * FROM book WHERE id = ?', (id,))
                
                time.sleep(.5)
                print(f'\nUpdate Record:')
                records_formatted = '{:<5} {:<50} {:<30} {:<6}' #format table for printing
                print(records_formatted.format("\nID", "Title", "Author", "Quantity"))
                
                for row in cursor:

                    print(records_formatted.format(*row))
                
                break

            elif sub_menu == 'z':
                
                break

            else:

                print("\nYou have entered an invalid choice. Please try again.\n")

    elif menu == '3': #delete books
        
        while True: #prompt until valid input

            try:

                id = int(input('\nWhat record would you like to delete? Please enter id:\n'))
                time.sleep(.5)
                
            except ValueError:

                print("\nYou have entered an invalid input. Please try again.")
                time.sleep(.5)
                continue
            
            else:

                break
        
        cursor.execute('DELETE FROM book WHERE id = ?', (id,))
        db.commit()
        time.sleep(.5)
        print(f"\nAll entries with ID {id} have been deleted, where applicable.")     
        
    elif menu == '4': #search books
        
        while True:
            
            time.sleep(.5)

            sub_menu = input('''\nHow would you like to search:\n
a. id
b. title
c. author
z. exit sub-menu
: ''').lower()
            
            time.sleep(.5)

            if sub_menu == 'a':
                
                while True: #prompt until valid input

                    try:

                        id = int(input('\nWhat record id would you like to search:\n'))
                        time.sleep(.5)

                    except ValueError:

                        print("\nYou have entered an invalid input. Please try again.")
                        time.sleep(.5)
                        continue
                
                    else:

                        break
                
                time.sleep(.5)

                cursor.execute('SELECT * FROM book WHERE id = ?', (id,))
                
                time.sleep(.5)
                print(f'Records found, if any:')
                records_formatted = '{:<5} {:<50} {:<30} {:<6}' #format table for printing
                print(records_formatted.format("\nID", "Title", "Author", "Quantity"))
                
                for row in cursor:
                        print(records_formatted.format(*row))
              
            elif sub_menu == 'b':

                title = input('\nWhat record title would you like to search:\n').lower()
                time.sleep(.5)
                cursor.execute('SELECT * FROM book WHERE title = ?', (title,))
                
                time.sleep(.5)
                print(f'Records found, if any:')
                records_formatted = '{:<5} {:<50} {:<30} {:<6}' #format table for printing
                print(records_formatted.format("\nID", "Title", "Author", "Quantity"))
                
                for row in cursor:

                    print(records_formatted.format(*row))
                
            elif sub_menu == 'c':

                author = input('\nWhat author name would you like to search:\n').lower()
                time.sleep(.5)
                cursor.execute('SELECT * FROM book WHERE author = ?', (author,))
                
                time.sleep(.5)
                print(f'Records found, if any:')
                records_formatted = '{:<5} {:<50} {:<30} {:<6}' #format table for printing
                print(records_formatted.format("\nID", "Title", "Author", "Quantity"))
                
                for row in cursor:

                    print(records_formatted.format(*row))
                
            elif sub_menu == 'z':

                break
            
            else:

                time.sleep(.5)
                print("\nYou have entered an invalid input. Please try again.\n")
            
            break

    elif menu == '5': #display all books

        cursor.execute('SELECT * FROM book')
        
        records_formatted = '{:<5} {:<50} {:<30} {:<6}'
        print(records_formatted.format("\nID", "Title", "Author", "Quantity"))
        
        for row in cursor:

            print(records_formatted.format(*row))

    elif menu == '0': #exit

        time.sleep(.5)
        print('\nGoodbye')
        db.close()
        exit()
    
    else:

        print("\nYou have entered an invalid input. Please try again.\n")


'''I used my level 1 capstone as a guide for the python aspects of this capstone. I wanted the output to be formatted so I
used this as a guide - https://stackoverflow.com/questions/48138015/printing-table-in-format-without-using-a-library-sqlite-3-python/

I also added a menu option to display all entries.'''



