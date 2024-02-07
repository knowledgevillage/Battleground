# Function and User input

#user input
#Take a input from user
name <- readline(prompt="Enter you name")
age <- readline(prompt="Enter you age")
print(paste("Hellos my name is ", name, " and my age is ", age))
#Paste is used to print and combine multiple values. If you use print function with multiple valus then it will print only first one.
print(name, age)

paste("Hello", "233", "Ram")
paste("Hello", "233", "Ram", sep='-')

#paste0 is another funvtion where by defaul it does not have any seprator
paste0("Hello", "233", "Ram")




#R functions
#function is set of code defined to perform the set of steps. it is of two type built in and user defined function.


#user defined function
# syntex -- > fun_name<- function( arg1, arg2, ..){}

new.function<-function()
{
  for(i in 1:5)
  {
    print(i^2)
  }
}
new.function()


#function with argument

new.function1 <- function(x,y,z)
{
  res<-x+y+z
  paste(res)

}

new.function1(10,23,56L)




# function with defaul argument

new.function2 <- function(x=3,y=6,z=10)
{
  res<-x+y+z
  paste(res)
  
}

new.function2()

new.function2(10,45,68)



#built-in functions

#abs()
#sqrt() - square root function
#floor()
#ceiling()
#trunc()
x<- c(5.6, 8,60)
print(abs(x))
print(sqrt(x))
print(floor(x))
print(ceiling(x))
print(trunc(x))

print(sin(x))
print(log(x))
print(exp(x))



a<-"Todayis07022024LetscheckwhatArebigNews Today"
print(substr(a,4,9))
print(toupper(a))

#patern serchgin
s1<-c('abcd', 'abcade', 'abdbcae')
pat<-'^abc'
print(grep(pat,s1))



a1<-c(1:10, 40)
print(a1)
print(sum(a1))

print(min(a1))
print(max(a1))