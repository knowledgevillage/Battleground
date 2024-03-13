# Write a code to calcualte factorial in number using recursive function calling method.

factorial_func <- function(num)
{
  
  if (num==1)
  {
    return (1)
  }else
  {
    num*factorial_func(num-1)
  }
}

#output<-factorial_func(5)
#output




#Write a code to calcualte factorial in number using recursive function calling method with user input.

factorial_num <- as.integer(readline(prompt = "Enter the number"))


factorial_output <- factorial_func(factorial_num)
factorial_output