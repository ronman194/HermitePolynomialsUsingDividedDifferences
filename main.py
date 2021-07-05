import math

def printFormula():
    print("H₂ₙ₊₁(X) = f[z₀] + sigma from k = 1 to 2n+1 of f[z₀,...,zₖ](x-z₀)(x-z₁)···(x-zₖ₋₁) \n")


def HermitePolynomialsUsingDividedDifferences(table, derivativesTable, xPoint):
    """

    :param table: table of x points and y values
    :param derivativesTable: table of x points and y' values (derivatives table by x ,y)
    :param xPoint: x point that we want to calculate his y value
    :return: the value of y at the given point
    """
    rows=len(table)*2 # size of z table
    arr = [[0]] * rows #create z table
    tempArr=[[0] * 2] * rows#create table for help
    i=0 #for while loop
    j=0 #for while loop
    while i != rows:# initilaize z table and help table
        arr[i]=[table[j][1]]
        arr[i+1]=[table[j][1]]
        tempArr[i]=table[j]
        tempArr[i+1]=table[j]
        i=i+2
        j=j+1
    temp=0  #for der
    for i in range(0,(rows-1)):
        if i % 2 == 0:
            arr[i].append(derivativesTable[temp][1])
            temp+=1
        else:
            arr[i].append((arr[i+1][0]-arr[i][0])/(tempArr[i+1][0]-tempArr[i][0]))
    i=0 #for while loop
    k=2 #for while loop
    j=1 #for while loop
    n=0 #for while loop
    while n <= rows-2:
        for i in range(rows-k):
            arr[i].append((arr[i + 1][j] - arr[i][j]) / (tempArr[i + k][0] - tempArr[i][0]))
        j+=1
        i=0
        k+=1
        n+=1
    i=2 #for for loop
    j=0 #for for loop
    k=2 #for for loop
    p=2 #for for loop
    sol=(table[0][1])+((derivativesTable[0][1]) * (xPoint - table[0][0])) #the solution
    for i in range(len(arr[0])):#calculate hermit polynomial
        mul=1
        if i < len(arr[0])-2:
            for j in range(k):
                mul=mul*(xPoint - tempArr[j][0])
            sol+=arr[0][p]*mul
            j=0
            p+=1
            if i!= (len(arr[0])-1):
                k+=1
    for row in arr:
        print(row)
    print("\n")
    printFormula()

    i = 2  # for for loop
    j = 0  # for for loop
    k = 2  # for for loop
    p = 2  # for for loop
    print("H{0}({1})=".format(rows - 1, xPoint), end=" ")
    print("{0}+{1}*{2}".format(tempArr[0][1], derivativesTable[0][1], (math.ceil((xPoint - table[0][0]) * 1000) / 1000)), end="")
    for i in range(len(arr[0])):  # calculate hermit polynomial
        mul = 1
        if i < len(arr[0]) - 2:
            for j in range(k):
                mul = mul * (xPoint - tempArr[j][0])
            print("+{0}*{1}".format(arr[0][p],math.ceil(mul*100000000)/100000000),end="")
            j = 0
            p += 1
            if i != (len(arr[0]) - 1):
                k += 1

    print(" ")
    print("\nH{0}({1}) = {2}".format(rows - 1, xPoint, sol))
    error=arr[0][len(arr[0])-1]
    for i in range(0,len(tempArr)):
        error=error*(xPoint - tempArr[i][0])
    error=abs(error)
    print("\nError: ",error)

    return sol
a=[[1,1],[2,4],[3,9],[4,16]]
aDer=[[1,2],[2,4],[3,6],[4,8]]
b=[[1.3,0.620086],[1.6,0.4554022],[1.9,0.2818186]]
bDer=[[1.3,-0.5220232],[1.6,-0.5698959],[1.9,-0.5811571]]
c=[[0.1,-0.6204995835],[0.2,-0.2839866844],[0.3,0.0066009467]]
cDer=[[0.1,3.585020824],[0.2,3.140332712],[0.3,2.666680427]]
HermitePolynomialsUsingDividedDifferences(b,bDer,1.5)

