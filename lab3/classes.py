# 1 task
print("1")
class two_classes():
    def getString(self):
        self.name = input()

    def printString(self):
        print(self.name.upper())

b = two_classes()
b.getString()
b.printString()

print("2")

# 2 task
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length=length

    def area(self):
        return self.length*self.length
    
if __name__=="__main__":
    square=Square(int(input()))
    print(square.area())
print("3")

# 3 task
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length*self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

sL = float(input())
s = Square(sL)
print(s.area())

rL = float(input())
rW = float(input())
r = Rectangle(rL, rW)
print(r.area())

print("4")

# 4 task
import math
class Point():
    def __init__(self, x1, y1, x2, y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.point_coordinates={self.x1:self.y1,}
        self.show()
        self.move()
        self.dist()
    def show(self):
        print(self.point_coordinates)
    def move(self):
        self.point_coordinates={self.x2:self.y2,}
    def dist(self):
        self.distance=math.sqrt(pow((self.x2-self.x1), 2)+pow((self.y2-self.y1), 2))
        print(self.distance)
ex = Point(int(input()), int(input()), int(input()), int(input()))


# 5 task
print("5")
class Account:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
        print(f"deposit of {amount} accepted. New balance:{self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance-=amount
            print(f"withdraw of {amount} accepted. new balance:{self.balance}")
        else:
            print("insufficient funds")

account = Account(input("owner is: "), abs(float(input("the balance is:"))))

account.deposit(float(input("write the amount u wanna deposit: ")))
account.withdraw(float(input("write the amount u wanna withdraw:")))

print("6")

# 6 task
class Prime:
    def __init__(self, a):
        self.a = a
    def isPrime(self, a):
        if (a>1):
            for i in range(2,a):
                if (a%i==0):
                    return False
            return True
        return False

    def filterPrimes(self):
        return list(filter(lambda x: self.isPrime(x),self.a))
    
b = input()
a = list(map(int, b.split()))
prF= Prime(a)
print(prF.filterPrimes())