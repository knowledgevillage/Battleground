#Write a function to find the least common multiple (LCM) of two numbers. 

lcm_check <- function(num1, num2)
{
  if(num1>num2)
  {
    smaller <- num2
  }else 
  {
    smaller <- num1
  }
  for (i in 2:smaller)
  {
    if (num1%%i==0 && num2%%i==0)
    {
      lcm <- i
      return(lcm)
    }
  }
  
}

# take input from the user
num1 = as.integer(readline(prompt = "Enter first number: "))
num2 = as.integer(readline(prompt = "Enter second number: "))

print(paste("The L.C.M. of", num1,"and", num2,"is", lcm_check(num1, num2)))

