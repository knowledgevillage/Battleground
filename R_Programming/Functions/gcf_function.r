#Lets find out greatest Common factor

gcf_check <- function(num1, num2)
{
  if(num1 > num2)
  {
    smaller<- num2
    if(num1%%num2==0)
    {
      return (num2)
    }
  }else
  {
    smaller <- num1
    if (num2%%num1==0)
    {
      return(num2)
    }
  }
  
    for (i in 1:smaller)
    {
      if(num1%%i==0 && num2%%i==0)
      {
        gcf<-i
      }
    }
    return(gcf)
  }


# take input from the user
num1 = as.integer(readline(prompt = "Enter first number: "))
num2 = as.integer(readline(prompt = "Enter second number: "))

print(paste("The H.C.F. of", num1,"and", num2,"is", gcf_check(num1, num2)))

