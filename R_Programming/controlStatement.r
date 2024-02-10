#R if else statment

x <-25L

if (is.integer(x))
{
  print("X is an integer number")
}else
{
  print("X is not a integer number")
}


# if else statment with  vector 

y <- c("Hardwork", 'is', "the", "key", "of", "success")
y

if('key' %in% y)
{
  print("key is found in our vector")
}else
{
  print("key is not found in our vector")
}


#nesting of if else

marks <- 75

if(marks>75)
{
  print("Passed with First class")
}else if(marks >65)
{
  print("Passed with Second Class")
}else if (marks>45)
{
  print("Passed with third class grades")
}else
{
  print("Fail")
}





# #Switch case
# # Swtich syntex == > switch(expression, case1, case2 ......)
# # Switch case can be implemented or work in two ways
# 1) By index value 
# 2) by matching values



# switch by index value

x <- switch(7,
            "RAM",
            "shyam",
            "Mohan",
            "Sumit"
            )

print(x)


# switch by matching values
y<-4
x<-switch(y,
          "4"="Ram",
          "14"="Shyam",
          "20"="Mohan",
          "25"="Sumit"
          )
print(x)




# next and break statement 
# next wrok same as continue key word in other prograaming language

x<-1:10
for(val in x)
{
  if(val==5)
    {
    next
  }
  print(val)
}



#repeat with break

a<-1;
repeat{
  if(a>5)
  {
    break
  }
  print(a)
  a<-a+1
}