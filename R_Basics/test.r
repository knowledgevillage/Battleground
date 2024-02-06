# This is a test file for R sctiping

4+5

print("have you got result above as 9")

print('Lets assign few varables to see there behaviour')

a=3
b=5
print(a)
sum=a+b
print(sum)
sub= a-b
print(sub)
div =a/b
print(div)
mul=a*b
print(mul)


dummy <- "Hellos r Programming"

#this is a single line cooment

demo1 <-2+5 ; demo2 <- 3/5
demo1
print(demo1)
demo2
print(demo2)
sessionInfo()
x<-1:10
plot(x)
?plot(x) # this is to get the help from R about a command or syntex
# is a case senstive language
a=10
A=10

##Varialbes in R programming

var.1 <- c(0,1,2,6)
print(var.1)




#Data Types in R

# Logical, numeric, complex, character, raw

#Defult data type of below would be numeric 
10->num

## Numeric data type -->  it will consist of all values +ve, -ve, natural, whole, and real numbers. eg. 12, 123.45, -123, -123.54
## Integer --> declare varialbe with capital 'L' at the end to define the variable as integer else it would be numeric as that is the default data type
##Complex -- > 5+2i
## Logical --> TRUE, FLASE #here 0,1 are not considered as FALSE and True respectively. You have to define them as FALSE and TRUE.
## Character --> "A", 'A', 'Hello R', '23.46', "Hellos 23.65 R" this can hold both the values od string and character.
char <- "A"
char2 <- 'A'
char3 <- 'Hello R'
print(char)
print(char2); print(char3)
class(char)
class(char2)
class(char3)
typeof(char)
typeof(char2)
typeof(char3)

## raw --> is used to hold raw bytes (unused infromation)

# lets do some pratical
num <- 10.56
class(num)
typeof(num)

intl<-14
class(intl)
#coverting data type
intl<-as.integer(intl)
class(intl)
intl1<-16L
class(intl1)
typeof(intl1)




#Conversion of data types in R

#converting data type into numeric data type
cnum1<-as.numeric(26L)
print(cnum1)
cnum2 <- as.numeric(25+6i)
print(cnum2)
cnum3 <- as.numeric("123535")
print(cnum3)
cnum4 <- as.numeric("LetsSeeWhatItReturns")
print(cnum4)



#converting data type into integer data type

cint1<-as.integer(26L)
print(cint1)
cint2 <- as.integer(25+6i)
print(cint2)
cint3 <- as.integer("123535")
print(cint3)
cint4 <- as.integer("LetsSeeWhatItReturns")
print(cint4)




#Oprator in R

##Arithmeatic Oprator --> =, +, -, *, / , %%, %/%, ^

a <- 7.5
b <- 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%%b) #reminder opration
print(a%/%b) #quotient
print(a^b)


#Vector in R
## Vecotr is a collection of similar data type.To declre a vectoer we have to use letter 'c'
c1 <- c(8,9,6)
c2 <- c(2,4,5)

print(c1+c2)
print(c1-c2)
print(c1*c2)
print(c1/c2)
print(c1%%c2) #reminder oprc1tion
print(c1%/%c2) #quotient
print(c1^c2)



#Relational Oprator --> <,>,==, <=, >=, !=
## it will always give output eiter as true or false. and will be appliable in both numbers and vectors.
print(c1<c2)
print(c1>c2)
print(c1==c2)
print(c1<=c2)
print(c1>=c2) 
print(c1!=c2) 


# Logical oprator -> &, |. !. &&, ||

d<-c(3.5,TURE,2+5i)
d




#Assignment Oprater =, <- , ->, <<- , ->>