class Library:
    """this is constructor methd which help us to automatically initialize instance after being instantiated.
    this constructor is receiving listofbooks as parameter and it has List datatype."""
    def __init__(self,listofbooks):
        self.availableboks=listofbooks
   #this is a method which will display all list of books available in our library. it is instance method. 
    def displayAvailablebooks(self):
        print("the books available in our library are:")
        for  book in self.availableboks:
            print(book)
        
   #this is an instance method that will help us to lend or request book from library.
    def Lendbook(self,requestBook):
        if requestBook in self.availableboks:
            print("you have now borrowed it")
        else:
            print("Sorry, it is not available right now be patient")

#this is second class called Student. also, it contains different methods that will help us to access different services of library.
class Student:
    #this is a method that allow us to request a bookfrom library and it allow user to input values using keyboard
    def requestBook(self):
        print("Please, enter the name of the book you would like to check out")
        self.book=input()
        
        return self.book
     #method below is also function of this class and it containd other several methods that are used to perform different tasks accordingly. and it will be accessed using ojbect of student class.
    def Main():
        library=Library(["mathematics","biology","chemistry","digital electronics"]) #instatiation of Library object; it should receive parameter to construct Libary attribute List.
        student=Student()      #instantiation of Student class object. this will allow user to access all members of this class.
       
        done=False
         #this hile loop we always allow user to get popup message that tell him or her what to do as long as stated condition is correct(true).
         #it will run only if main() method is called using student object of this class.
        while done==False:
            print("""========LIBRARY MENU=======
               1.Display all available books in our Library
               2.Request a book from Library
               3.Add a book into Library
               4.search book available in library by typing word python
            """)
            #this method allow library user to add book into library.
            def status():
                bookadded=input("please add book into our Library:")
                library.availableboks.append(bookadded)
             #this method below will allow user to remove a book from library by typing its name here.
            def removedbook():
                bookremoved=input("please, enter again removed(lent) book name:")
                library.availableboks.remove(bookremoved)
                print("REMOVED BOOK IS DISPLAYED HERE:"+ bookremoved)
             #this method below allows user to search tdifferent books available in library by using word "python" ass a key to search.
            def SearchBook():
                searched=input("PLEASE SEARCH A BOOK IN LIBRARY BY WRITING [python]:")
                if searched=="python":
                    library.displayAvailablebooks()
              #after reading popup messages tell user what action to perform based on choice she or he have made.
              # this line of code below is the one which allow user to insert or input respective choice.
              #each choice has corresponding task that shoulbe performed after choosing appropriate choice.
            choice=int(input("Enter choice:"))
             # the following command below ill run if its condtion is true(satisfied)
            if choice==1:
                library.displayAvailablebooks()
                size = len(library.availableboks)
                print("THOSE ARE NUMBER OF AVAILABLE BOOKS IN OUR lIBARARY:"+str(size))
              # the following command below ill run if its condtion is true(satisfied)
            elif choice==2:
                library.Lendbook(student.requestBook())
                removedbook()
              # the following command below ill run if its condtion is true(satisfied)
            elif choice==3:
                status()
              # the following command below ill run if its condtion is true(satisfied)
            elif choice==4:
                SearchBook()
 #this calling of main method. sinc, it is instance method of Student class, it will be accessed only if using object of this class(Student).
Student.Main()      



        

