#prime number check function

prime_check<- function(num)
{
  if(num==2)
  {
    return (TRUE)
    
  } else if(num<=1)
  {
    return(FALSE)
  }
  else
  {
    for (i in 2:(num-1))
    {
      if (num %% i ==0)
      {
        return(FALSE)
      }
      else
      {
        return(TRUE)
      }
    }
    # return(1)
  }
  
}
prm_num_chk <- as.integer(readline(prompt = "Enter the number"))

if(prime_check(prm_num_chk))
{
  print(paste(prm_num_chk, " is a prime number"))
}else
{
  print(paste(prm_num_chk, "is not a prime number"))
}