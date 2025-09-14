print("-" * 159)
print(" " * 159)
print(f"{"✮ ⋆ ˚｡𖦹 ⋆｡°✩ 𝐵𝑜𝑜𝑘 𝑅𝑒𝑎𝑑𝑖𝑛𝑔 𝑇𝑟𝑎𝑐𝑘𝑒𝑟 ✮ ⋆ ˚｡𖦹 ⋆｡°✩":>103}")
print(f"{"✮ by Regina Jelita Ningsih ✮":>88}")
print(" " * 159)
print("-" * 159)

book_data = [
            ("All the Lovers in the Night", "Mieko Kawakami", "Slice of Life", "Unfinished", "Page 01"),
            ("Days at the Morisaki Bookshop", "Satoshi Yagisawa", "Slice of Life", "Unfinished", "Page 10"),
            ("Heaven", "Mieko Kawakami", "Slice of Life", "Unfinished", "Page 06")
            ]

print(" " * 159)
print(f"{"Books List":>84}")
print(" " * 159)
print("-" * 159)
print(f"{"Book Title":<35}|{"Author":<31} |{"Genre":<31} |{"Status":<31}|{"Last page":<31}")
print("-" * 159)
print(f"{book_data[0][0]:<35}| {book_data[0][1]:<31}|{book_data[0][2]:<31} |{book_data[0][3]:<31}|{book_data[0][4]:<31}")
print(f"{book_data[1][0]:<35}| {book_data[1][1]:<31}|{book_data[1][2]:<31} |{book_data[1][3]:<31}|{book_data[1][4]:<31}")
print(f"{book_data[2][0]:<35}| {book_data[2][1]:<31}|{book_data[2][2]:<31} |{book_data[2][3]:<31}|{book_data[2][4]:<31}")
print("-" * 159)

print("Main menu")
print("[1] New Book")
print("[2] Update Tracker")
print("[3] Delete Book")
menu = input("Select the menu: ")
print("-" * 159)

if menu == "1":
        title = input("Book Title: ")
        author = input("Author: ")
        genre = input("Genre: ")
        status = input("Status (Unfinished/Finished): ")
        progress = input("Last page: ")
        print("-" * 159)
        book_data.append((title, author, genre, status, progress))
        
        print(" " * 159)
        print(f"The {title} has been successfully added ^^")
        print(" " * 159)
        print("-" * 159)

        print("[x] Exit")
        exit = input("= ") 
        if exit == "x":  
            print("-" * 159)
            print(" " * 159)
            print(f"{"Books List":>84}")
            print(" " * 159)
            print("-" * 159)
            print(f"{"Book Title":<35}|{"Author":<31} |{"Genre":<31} |{"Status":<31}|{"Last page":<31}")
            print(f"{book_data[0][0]:<35}| {book_data[0][1]:<31}|{book_data[0][2]:<31} |{book_data[0][3]:<31}|{book_data[0][4]:<31}")
            print(f"{book_data[1][0]:<35}| {book_data[1][1]:<31}|{book_data[1][2]:<31} |{book_data[1][3]:<31}|{book_data[1][4]:<31}")
            print(f"{book_data[2][0]:<35}| {book_data[2][1]:<31}|{book_data[2][2]:<31} |{book_data[2][3]:<31}|{book_data[2][4]:<31}")
            print(f"{book_data[3][0]:<35}| {book_data[3][1]:<31}|{book_data[3][2]:<31} |{book_data[3][3]:<31}|{book_data[3][4]:<31}")
            print("-" * 159)

        else:
            print("-" * 159)
            print("Error :(")
            print("-" * 159)

    
elif menu == "2":
    search_title= input("Book Title: ")
    print("-" * 159)

    if search_title == book_data[0][0]:
            print("Book Title:", search_title)
            update_status = input("Update 'Status': ")
            update_page = input("Update 'Last page': ")
            print("-" * 159)
            print(" " * 159)
            print(f"The tracker has been successfully updated ^^")
            print(" " * 159)
            print("-" * 159)

            print("[x] Exit")
            exit = input("= ") 
            if exit == "x": 
                print("-" * 159)
                print(" " * 159)
                print(f"{"Books List":>84}")
                print(" " * 159)
                print("-" * 159)
                print(f"{"Book Title":<35}|{"Author":<31} |{"Genre":<31} |{"Status":<31}|{"Last page":<31}")
                print(f"{book_data[0][0]:<35}| {book_data[0][1]:<31}|{book_data[0][2]:<31} |{update_status:<31}|{update_page:<31}")
                print(f"{book_data[1][0]:<35}| {book_data[1][1]:<31}|{book_data[1][2]:<31} |{book_data[1][3]:<31}|{book_data[1][4]:<31}")
                print(f"{book_data[2][0]:<35}| {book_data[2][1]:<31}|{book_data[2][2]:<31} |{book_data[2][3]:<31}|{book_data[2][4]:<31}")
                print("-" * 159)

            else:
                print("Error :(")

    elif search_title == book_data[1][0]:
            print("Book Title:", search_title)
            update_status = input("Update 'Status': ")
            update_page = input("Update 'Last page': ")
            print("-" * 159)
            print(" " * 159)
            print(f"The tracker has been successfully updated ^^")
            print(" " * 159)
            print("-" * 159)

            print("[x] Exit")
            exit = input("= ") 
            if exit == "x":  
                print(" " * 159)
                print(f"{"Books List":>84}")
                print(" " * 159)
                print("-" * 159)
                print(f"{"Book Title":<35}|{"Author":<31} |{"Genre":<31} |{"Status":<31}|{"Last page":<31}")
                print(f"{book_data[0][0]:<35}| {book_data[0][1]:<31}|{book_data[0][2]:<31} |{book_data[0][3]:<31}|{book_data[0][4]:<31}")
                print(f"{book_data[1][0]:<35}| {book_data[1][1]:<31}|{book_data[1][2]:<31} |{update_status:<31}|{update_page:<31}")
                print(f"{book_data[2][0]:<35}| {book_data[2][1]:<31}|{book_data[2][2]:<31} |{book_data[2][3]:<31}|{book_data[2][4]:<31}")
                print("-" * 159)

            else:
                print("Error :(")

            
    elif search_title == book_data[2][0]:
            print("Book Title:", search_title)
            update_status = input("Update 'Status': ")
            update_page = input("Update 'Last page': ")
            print("-" * 159)
            print(" " * 159)
            print(f"The tracker has been successfully updated ^^")
            print(" " * 159)
            print("-" * 159)

            print("[x] Exit")
            exit = input("= ") 
            if exit == "x":  
                print(" " * 159)
                print(f"{"Books List":>84}")
                print(" " * 159)
                print("-" * 159)
                print(f"{"Book Title":<35}|{"Author":<31} |{"Genre":<31} |{"Status":<31}|{"Last page":<31}")
                print(f"{book_data[0][0]:<35}| {book_data[0][1]:<31}|{book_data[0][2]:<31} |{book_data[0][3]:<31}|{book_data[0][4]:<31}")
                print(f"{book_data[1][0]:<35}| {book_data[1][1]:<31}|{book_data[1][2]:<31} |{book_data[1][3]:<31}|{book_data[1][4]:<31}")
                print(f"{book_data[2][0]:<35}| {book_data[2][1]:<31}|{book_data[2][2]:<31} |{update_status:<31}|{update_page:<31}")
                print("-" * 159)

            else:
                print("Error :(")
    else:
        print("Sorry, title was not found :(")


    
elif menu == "3":
        column = int(input("Book Column: "))
        print("-" * 159)
        del_book = column - 1
        
        if 0 <= del_book < len(book_data):
            book_data.pop(del_book)
            print("The book has been deleted")
            print("-" * 159)
        else:
            print("-" * 159)
            print("Column not found T___T")
            print("-" * 159)

        print(" " * 159)
        print(f"{"Books List":>84}")
        print(" " * 159)
        print("-" * 159)
        print(f"{"Book Title":<35}|{"Author":<31} |{"Genre":<31} |{"Status":<31}|{"Last page":<31}")
        print("-" * 159)

        if len(book_data) == 0:
            print("Error: no books found")
        elif len(book_data) == 1:
            print(f"{book_data[0][0]:<35}| {book_data[0][1]:<31}|{book_data[0][2]:<31} |{book_data[0][3]:<31}|{book_data[0][4]:<31}")
        elif len(book_data) == 2:
            print(f"{book_data[0][0]:<35}| {book_data[0][1]:<31}|{book_data[0][2]:<31} |{book_data[0][3]:<31}|{book_data[0][4]:<31}")
            print(f"{book_data[1][0]:<35}| {book_data[1][1]:<31}|{book_data[1][2]:<31} |{book_data[1][3]:<31}|{book_data[1][4]:<31}")
        else:  
            print(f"{book_data[0][0]:<35}| {book_data[0][1]:<31}|{book_data[0][2]:<31} |{book_data[0][3]:<31}|{book_data[0][4]:<31}")
            print(f"{book_data[1][0]:<35}| {book_data[1][1]:<31}|{book_data[1][2]:<31} |{book_data[1][3]:<31}|{book_data[1][4]:<31}")
            print(f"{book_data[2][0]:<35}| {book_data[2][1]:<31}|{book_data[2][2]:<31} |{book_data[2][3]:<31}|{book_data[2][4]:<31}")

        

else:
        print("Error :(")
        print("-" * 159)