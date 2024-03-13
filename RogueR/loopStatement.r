#Loops in R

for(y in 1:10)
{
  print(paste("Number: ", y))
}

#vector with loop
f<-c("orange", "apple", "banana", "graps", "mango")
for (i in f )
{
  print(i)
}


# Repeat loop in R
# Repeat does not uses any condition. If we have to come out of this loop then we will use break keyword

v <- c('hello',"how","are", "you")
x<-2

repeat{
  print(v)
  x<-x+1
  if(x>5)
  {
    break
  }
}



# while loop in R

v<-c("Hello", "R", "Prograaming", "Language")
x<-2
while(x<=6)
{
  print(v)
  x<-x+1
}