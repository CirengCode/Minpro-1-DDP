# Minpro-1-DDP
Regina Jelita Ningsih 
<br> (2509116061)
# Program Book Reading Tracker
<br> Program ini dibuat untuk membantu pengguna mencatat dan memantau aktivitas membaca buku, agar pengguna bisa mengetahui sudah sejauh mana pengguna membaca buku. Program ini dibuat dengan menggunakan bahasa pemrograman python dengan menerapkan sistem CRUD. Selanjutnya, akan saya jelaskan fitur-fitur yang ada di program ini.

# 1. Home Page
> Berikut ini merupakan tampilan awal dari program saat dijalankan. Pada home page terdapat list data-data buku yang telah tersimpan, mulai dari judul buku, penulis, genre, status buku (sudah selesai dibaca atau belum), dan yang terakhir ada halaman terakhir yang dibaca. Pada home page juga terdapat beberapa menu pilihan yang dapat digunakan pengguna sesuai dengan kebutuhan pengguna. Terdapat 3 menu utama, yaitu New Book, Update tracker, dan Delete book.
<img width="1477" height="521" alt="image" src="https://github.com/user-attachments/assets/ea918ead-b6e4-4085-a01e-451884ed343a" />

# 2. Menu New Book
> Menu ini berfungsi untuk menambahkan data buku baru dengan mengisi beberapa beberapa data seperti judul buku, penulis, genre, status buku (sudah selesai dibaca atau belum), dan yang terakhir ada halaman terakhir yang dibaca.
<img width="1488" height="650" alt="image" src="https://github.com/user-attachments/assets/a603029d-c8ad-40db-9f49-fd52c150b1b4" />

# 3. Menu Update Tracker
> Menu ini berfungsi untuk melakukan perubahan pada data status buku dan halaman terakhir buku yang dibaca, sehingga pengguna bisa mengetahui sudah sejauh mana pengguna membaca buku. Pengguna hanya perlu memasukan judul buku yang ingin diubah status dan halaman halaman terakhir buku yang dibaca, lalu memasukan status terbaru buku tersebut dan halaman halaman terakhir buku yang telah dibaca.
<img width="1486" height="615" alt="image" src="https://github.com/user-attachments/assets/7fb80079-8bc3-4d27-8d75-bdb42078085f" />

# 4. Menu Delete Book
> Seperti namanya, menu ini berfungsi untuk menghapus data buku yang terdapat dalam list buku. Pengguna hanya perlu memasukan nomor urut kolom dari data buku yang ingin di hapus dan data-data buku tersebut akan langsung terhapus.
<img width="1479" height="420" alt="image" src="https://github.com/user-attachments/assets/84260592-72b8-48a1-a273-6a16006b7944" />

# 5. Kondisi lainnya
> Tampilan jika pengguna pada menu utam menginput selain 1-3
<img width="1468" height="565" alt="image" src="https://github.com/user-attachments/assets/c600a6f6-74a6-4d8e-bbd0-deff7ff4c527" />

> Tampilan jika pengguna pada exit menginput selain "x"
<img width="1484" height="853" alt="image" src="https://github.com/user-attachments/assets/90d535f0-443e-42bb-af94-0d421ba10546" />

> Tampilan jika pengguna pada menu update tracker menginput judul yang tidak ada pada list data
<img width="1486" height="586" alt="image" src="https://github.com/user-attachments/assets/9cd39e43-52b1-4253-806e-4317f923a678" />

> Tampilan jika pengguna pada menu delete book menginput nomor urut kolom yang tidak valid
<img width="1487" height="599" alt="image" src="https://github.com/user-attachments/assets/5647b9ff-69fe-45c3-9ad1-2b04f6ca6858" />



# Penjelesan Program
> List data buku:
<br> Variabel dengan nama book_data berisi tuple-tuple yang fungsinya sebagai sumber data awal agar pada programnya sudah tersedia beberapa data bukunya. Setiap tuple menyimpan data-data buku berupa judul, penulis, genre, status, dan halaman terakhir yang dibaca.
```
book_data = [
            ("All the Lovers in the Night", "Mieko Kawakami", "Slice of Life", "Unfinished", "Page 01"),
            ("Days at the Morisaki Bookshop", "Satoshi Yagisawa", "Slice of Life", "Unfinished", "Page 10"),
            ("Heaven", "Mieko Kawakami", "Slice of Life", "Unfinished", "Page 06")
            ]
```
> Header:
<br> Kode dibawah ini menampilkan header yang fungsi nya hanya sebagai penghias saja agar tampilan awal menjadi lebih menarik.
```
print("-" * 159)
print(" " * 159)
print(f"{"✮ ⋆ ˚｡𖦹 ⋆｡°✩ 𝐵𝑜𝑜𝑘 𝑅𝑒𝑎𝑑𝑖𝑛𝑔 𝑇𝑟𝑎𝑐𝑘𝑒𝑟 ✮ ⋆ ˚｡𖦹 ⋆｡°✩":>103}")
print(f"{"✮ by Regina Jelita Ningsih ✮":>88}")
print(" " * 159)
print("-" * 159)
```
> Tabel data buku:
<br> Kode dibawah ini akan menampilkan tabel yang berisi data-data buku yang ada pada variabel book_data pada tampilan awal.
```
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
```
> Menu Utama:
<br> Kode dibawah ini akan menampilkan menu utama seperti new book, update tracker, dan delete book yang nanti dapat user pilih dengan menginput nomor 1-3 sesuai dengan menu yang pengguna pilih.
```
print("Main menu")
print("[1] New Book")
print("[2] Update Tracker")
print("[3] Delete Book")
menu = input("Select the menu: ")
print("-" * 159)
```
> Menu New Book:
<br>Kondisi dibawah ini akan mengeksekusi pilihan "1" untuk menambahkan buku baru (New Book). Program akan meminta pengguna untuk menginput data-data buku (judul, penulis, genre, status, dan halaman tarakhir buku yang di baca). Program akan menampilkan pesan "The (judul buku) has been successfully added" saat data berhasil ditambahakan. Lalu pengguna diminta untuk menginput "x" dan program akan menampilkan tabel data buku yang terbaru, namun jika pengguna menginput selain "x" akan muncul pesan error.
```
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
```
> Menu Update Tracker:
<br> Kondisi dibawah ini akan mengeksekusi pilihan "2" untuk melakukan update status buku dan halaman buku yang terakhir di baca. Program ini juga hanya akan memeriksa tiga data awal buku pada list book_data secara manual dan tidak menggunakan loop. Sehingga, data-data buku yang diperbarui hanya ditampilkan di output, tetapi tidak benar-benar mengubah isi dari list book_data. Program akan meminta pengguna untuk memasukan judul dari buku yang status dan halaman, yang ingin diubah. Jika pengguna menginput judul yang salah maka akan muncul pesan "Sorry, title was not found :(", namun jika pengguna menginput judul yang benar, pengguna diminta untuk memasukan status buku dan halaman buku yang terakhir di baca. Program akan menampilkan pesan "The tracker has been successfully updated ^^" saat data berhasil ditambahakanLalu pengguna diminta untuk menginput "x" dan program akan menampilkan tabel data buku yang terbaru, namun jika pengguna menginput selain "x" akan muncul pesan error.
```
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
```
> Menu Delete Book:
<br> Kondisi dibawah ini akan mengeksekusi pilihan "3" untuk menghapus data buku berdasarkan nomor urut kolom buku yang dinput. Data buku akan berhasil dihapus jika nomor kolom yang diinput valid, sehingga program akan menampilkan output berupa tabel yang berisi data buku yang tersisa. Namun, jika nomor kolom yang diinput tidak valid, maka program akan menampikan pesan error "Column not found T___T".
```
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
```
> Akhir Cabang:
<br> kode dibawah ini akan menampilkan pesan error jika pada menu utama menginput selain 1-3.
```
else:https://docs.github.com/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
        print("Error :(")
        print("-" * 159)
```

# FLOWCHART
![MINPRO-1-REGINA drawio (6)](https://github.com/user-attachments/assets/2752caae-2029-46e4-b8c9-5ffc3192a96c)

