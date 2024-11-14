from abc import ABC, abstractmethod

# Impelementasi Encapsulation dan Abstraksi
class Person(ABC): 
    def __init__(self, name, phoneNumber, emailAddress):
        self.name = name
        self.__phoneNumber = phoneNumber # Private Attribute
        self.emailAddress = emailAddress
    
    def purchaseParkingPass(self):
        print(f"{self.name} has purchased a parking pass.")

    # Getter untuk phoneNumber
    def getPhoneNumber(self):
        return self.__phoneNumber
    # Setter untuk phoneNumber
    def setPhoneNumber(self, newPhoneNumber):
        self.__phoneNumber = newPhoneNumber

    # Implementasi Polymorphism dan Abstraksi
    @abstractmethod
    def displayInfo(self):
        pass
        
class Address:
    def __init__(self, street, city, state, postalCode, country):
        self.street = street
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.country = country

    def validate(self):
        return True
    
    def outputAsLabel(self):
        print (f"{self.street}, {self.city}, {self.state}, {self.postalCode}, {self.country}")


# Impelementasi Inheritance
class Student(Person):
    def __init__(self, name, phoneNumber, emailAddress, studentNumber, averageMark):
        super().__init__(name, phoneNumber, emailAddress)
        self.studentNumber = studentNumber
        self.averageMark = averageMark

    def isEligibleToEnroll(self):
        return self.averageMark >= 80
    
    def getSeminarsTaken():
        print("Seminars taken by student")
    
    # Implementasi Polymorphism
    def displayInfo(self):
        print(f"Student Name: {self.name}, Student Number: {self.studentNumber}")

    


# Impelementasi Inheritance   
class Professor(Person):
    def __init__(self, name, phoneNumber, emailAddress, salary, staffNumber, yearsOfService, numberOfClasses ):
        super().__init__(name, phoneNumber, emailAddress)        
        self.salary = salary
        self.staffNumber = staffNumber
        self.yearsOfService = yearsOfService
        self.numberOfClassess = numberOfClasses
    
    # Implementasi Polymorphism
    def displayInfo(self):
        print(f"Professor Name: {self.name}, Professor Number: {self.staffNumber}")


print(f"Soal 1")

# Membuat objek dari kelas turunan yang mengimplementasikan displayInfo()
student1 = Student("Rama", "08123456789", "rama@example.com", "S12345", 85)
professor1 = Professor("Dr. Joko", "08198765432", "joko@university.com", 1000000, "P987", 10, 5)

# 1. Encapsulation (Akses melalui Getter dan Setter)
print(f"Initial Phone Number: {student1.getPhoneNumber()}")
student1.setPhoneNumber("08123456790")
print(f"Updated Phone Number: {student1.getPhoneNumber()}")

# 2. Inheritance (Mewarisi dari Person)
# 3. Polymorphism (Metode displayInfo() yang diimplementasikan berbeda)
student1.displayInfo()  # Output yang spesifik untuk Student
professor1.displayInfo()  # Output yang spesifik untuk Professor

# 4. Abstraction (Metode displayInfo() yang abstrak di Person diimplementasikan di kelas turunan)

# 5. Membuat dan menggunakan objek Address
address1 = Address("Jl. Merdeka No. 1", "Jakarta", "DKI Jakarta", "12345", "Indonesia")
address1.outputAsLabel()  # Menampilkan alamat
print(f"Is the address valid? {address1.validate()}")



print(f"    ")
print(f"    ")
print(f"    ")
print(f"Soal 2")


# Implementasi Abstraksi
class Book(ABC):
    # Konstruksi untuk menginisialisasi nama perpustakaan
    def __init__(self, name):
        self.name = name
    
    # Funtion abstraksi yang harus digunakan di kelas turunan
    @abstractmethod
    def get_books(self):
        pass


class Library(Book):
    # Konstruksi untuk menginisialisasi daftar buku
    def __init__(self,name):
        # Inisialisasi dari Book
        super().__init__(name)
        self.name = name
        # Implementasi Encapsulation
        self.__books = {}

    # Metode untuk menambahkan buku ke perpustakaan
    def add_book(self,title, quantity=1):
        if title in self.__books:
            self.__books[title] += quantity
        else:
            self.__books[title] = quantity
            print(f"Added '{title}' to the library. Total copies: {self.__books[title]}")

    # Penerapan function abstraksi dengan menampilkan daftar buku yang di private
    def get_books(self):
        return self.__books
    
    

# Penggunaan
library = Library("Perpustakaan Rama")

library.add_book("Python Programming", 5)
library.add_book("Python Programming", 3)
library.add_book("Data Science Essentials", 2)

print(library.get_books())



print(f"    ")
print(f"    ")
print(f"    ")
print(f"Soal 3")


# Implementasi Abstraksi
class Dish(ABC):
    # Konstruksi untuk menginisialisasi atribut Dish
    def __init__(self, name, category, price, ingredients, availability):
        self.name = name
        self.category = category
        self.price = price
        self.ingredients = ingredients 
        self.availability = availability
    
    # Function Abstraksi yang harus diterapkan di kelas turunan
    @abstractmethod
    def get_info(self):
        pass


# Penerapan Encapsulation
class Customer:
    # Konstruksi untuk menginisialisasi atribut pada kelas Customer
    def __init__(self, name, customer_id, order_history, current_order):
        self.name = name
        self.customer_id = customer_id
        self.__order_history = order_history # Private Attribute
        self.__current_order = current_order # Private Attribute

    # Function untuk mengakses Private Attribute (order history)
    def get_order_history(self):
        return self.__order_history
    
    # Function untuk mengakses Private Attribute (current order)
    def get_current_order(self):
        return self.__current_order

class Waiter:
    def __init__(self, name,employee_id, assigned_table, shift_hours):
        self.name = name
        self.employee_id = employee_id
        self.assigned_table = assigned_table
        self.shift_hours = shift_hours
        
# Implementasi Inheritance dan Polymorphism
class NasiGoreng(Dish):
    # Konstruksi untuk menginisialisasi atribut pada kelas NasiGoreng
    def __init__(self, name, category, price, ingredients, availability):
        super().__init__(name, category, price, ingredients, availability)

    # Function Abstraksi dan Polymorphism untuk menampilkan informasi pada kelas NasiGoreng
    def get_info(self):
        print("\n".join([f"Name: {self.name}", f"Category: {self.category}", f"Price: {self.price}", f"Ingredients: {self.ingredients}", f"Availability: {self.availability}"]))


# Implementasi Inheritance
class AyamGoreng(Dish):
    # Konstruksi untuk menginisialisasi atribut pada kelas AyamGoreng
    def __init__(self, name, category, price, ingredients, availability):
        super().__init__(name, category, price, ingredients, availability)

    # Function Abstraksi dan Polymorphism untuk menampilkan informasi pada kelas AyamGoreng
    def get_info(self):
        print("\n".join([f"Name: {self.name}", f"Category: {self.category}", f"Price: {self.price}", f"Ingredients: {self.ingredients}", f"Availability: {self.availability}"]))


# Membuat objek makanan
nasi_goreng = NasiGoreng("Nasi Goreng", "Main Course", 25000, ["Rice", "Egg", "Chicken", "Spices"], True)
ayam_goreng = AyamGoreng("Ayam Goreng", "Main Course", 30000, ["Chicken", "Spices", "Oil"], True)

# Menampilkan informasi makanan
nasi_goreng.get_info()  # Memanggil metode get_info() untuk NasiGoreng
ayam_goreng.get_info()  # Memanggil metode get_info() untuk AyamGoreng


