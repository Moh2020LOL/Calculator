from cmath import *
from sympy import *
import turtle as tr



choose = input("choose your al math + , // , trangle: ")



def main():
    if plus == "+":
        print(x+y)
    if plus == "x" or plus == "*":
        print(x*y)
    if plus == "-":
        print(x-y)
    if plus == "/" and x != 0 and y !=0:
        print(x/y)
    if x == 0 and y ==0 and plus == "/":
        print("error")
    return 0

def sinc():
    sec = tr.Screen()
    pen = tr.Turtle()

    if x == 60:
        tr.right(180)
        
        tr.forward(300-145)
        
        tr.right(90)
        
        tr.forward(200)
        
        tr.right(143.1)
        
        tr.forward(500-250)
        tr.end_fill()
        sec.exitonclick()

def re():
    M,t,r,theta,phi = symbols("M t r theta phi")

    coor = [t,r,theta,phi]

    def m(i,j):
        g00 = -(1-2*M/r)
        g01 = 0
        g02 = 0
        g03 = 0
        g10 = 0
        g11 = 1/(1-2*M/r)
        g12 = 0
        g13 = 0
        g20 = 0
        g21 = 0
        g22 = r**2
        g23 = 0
        g30 = 0
        g31 = 0
        g32 = 0
        g33 = r**2*sin(theta)**2
        return ([[g00,g01,g02,g03],
                [g10,g11,g12,g13],
                [g20,g21,g22,g23],
                [g30,g31,g32,g33]])[i][j]

    def dm(i,j,k):
        return diff(m(i,j),coor[k])
    def im(i,j):
        K = Matrix([[m(0,0),m(0,1),m(0,2),m(0,3)],
                    [m(1,0),m(1,1),m(1,2),m(1,3)],
                    [m(2,0),m(2,1),m(2,2),m(2,3)],
                    [m(3,0),m(3,1),m(3,2),m(3,3)]])
        return K.inv(method="LU")[i,j]


    def gamma(i,j,k):
        s = 0
        for l in range(4):
            s +=0.5*im(i,l)*(dm(k,l,j)+dm(l,j,k)-dm(j,k,l))
            return simplify(s)
    for a in range(4):
        for b in range(4):
            for c in range(4):
                if gamma(a,b,c) == 0:
                    pass
                else:
                    print("[",a,b,c,"]",gamma(a,b,c))

def po():
    t = int(input())
    print("-")
    g = int(input())
    print("")
    f = int(input())
    print("-")
    l = int(input())
    print("----------")
    m = input("?:")
    print("------------")
    
    if m == "+":
        print(t/g + f/l)
        print("------------")
        if g == l:
            print(t+f)
            print("---")
            print(l or g)
        else:
            print((t*l)+(f*g))
            print("---")
            print(l*g)
    if m == "x":
        print(t/g * f/l)
    if m == "-":
        print(t/g - f/l)
        print("------------")
        if g == l:
            print(t-f)
            print("---")
            print(l or g)
        else:
            print((t*l)-(f*g))
            print("---")
            print(l*g)
    if m == "/":
        print(t/g * l/f)

def aso():
    p = int(input())
    b =int(input())
    def res(b,p):
        r = 1
        for index in range(p):
            r = r * b
        return r
    print(res(b,p))


def lo():
    x = int(input())
    y = int(input())
    z = int(input())
    m = input()
    if m == "+" :
        f = x + y + z
        print("x^2",x,"+",y,"+",z)
        print("----------")
        nm = x % 2
        nu = z % y
        if nm != 0:
            np = x % z
        else:
            np = z % x
        if nu != 0:
            nt = z % y
        else:
            nt = y % z 

        if np + nt == y:
            print("(","x","+",nm,")","(","x","+",nu,")")

        
        else:
            print("Sorry Error")


    if m == "-":
        f = x + y - z
        print("x^2",x,"+",y,"+",z)
        print("----------")


    


if choose == "+":
    x = int(input())

    plus = input()

    y = int(input())

    main()


if choose == "trangle":
    x = int(input())
    sinc()

if choose == "re":
    re()

if choose == "//":
    po()

if  choose == "^":
    aso()
if choose == "lo":
    lo()