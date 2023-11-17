def main():
    
    
    try:
        # Initializing an empty bookslist...
        booksList = []
        infile = open("TheBooksList.txt","r")
        line = infile.readline()
        while line:
            booksList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()

    except FileNotFoundError :
        print("The <bookslist.txt> file is not found ")
        print("Starting a new books list!")
        booksList = []
    

    choice = 0
    while choice != 4:
        print("*** Welcome To The Books Manager ***")
        print("1.) Add a book")
        print("2.) Lookup a book")
        print("3.) Display a book(s)")
        print("4.) Quit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("You've chosen to add a book....")
            bookName = input("Enter the name of the book: ")
            bookAuthor = input("Enter the name of the author: ")
            pages = input("Enter the number of pages of the book: ")
            booksList.append([bookName, bookAuthor, pages])
            

        elif choice == 2:
            print("You've chosen to lookup a book...")
            hint = input("Enter a hint for finding the book of your choice: ")
            for book in booksList:
                if hint in book: 
                    print("Book details:",book)

        elif choice == 3:
            print("Displaying all book(s)...")
            # Displaying details of the book entered as a Dictionary...
            for i in range(len(booksList)):
                booksDictionary = {'BookName':booksList[i][0], 'BookAuthor':booksList[i][1], 'Pages':booksList[i][2]}
                print(booksDictionary)
            

        else:
            print("Thanks for your time!")
            print("You're now exiting the programme...")

    print("Programm Terminated!!")

    # Saving books to an external txt file...

    outfile = open("TheBooksList.txt","w")
    for book in booksList:
        outfile.write(",".join(book) + "\n")
    outfile.close()


if __name__ == "__main__":
    main()

