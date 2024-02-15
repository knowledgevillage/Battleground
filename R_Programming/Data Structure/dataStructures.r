#Data structures in R

# vector
# matrix
# list
# arrays
# data frames

# A vector is simply a list of items that are of the same type. To combine the list of items to a vector, use the c() function and separate the items by a comma.
## elements of vactor are known as components
# Type of vector can be check with typeof function


# function in vector
# length --> used to fined the number of elements in a vector
# # type of Vector
# 1 --> Atomic vector
# 2 --> list


#how to create a vector

# Method 1 --> using c function

a <- c(1,23,45,144,67)
a

#Method 2 --> using : oprator
b<- -3:5
b


#Method 3 --> using seq function

c <- seq(1,5)
c

  #lets add steps or gaps in the sequence
d <- seq(1,5, by =.4)
d



  #we can use length.out insted of by 
e <- seq(1,4, length.out = 12)
e


#atomic vector is of 4 types 
# 1 - Numeric Vector

numv <- c(1,2.3,5,6,7,8.9)
numv
class(numv)


# 2 - integer vector
#there are two ways to create integer vector. 
#i - keep L with each elements of vector. If you give any values with decimal then vector will converte into numeric vector.
intv1 <- c(1L,2L,3L, 5L)
intv1
class(intv1)


#ii -  convert a numric vector into Integer vector
intv2 <- seq(1,28, by=2 )
intv2 
class(intv2)
intv2<- as.integer(intv2)
class(intv2)



# 3 - character vector
charv <- c(1,5,8,7)
charv
class(charv)
charv <- as.character(charv)
class(charv)
charv

charvv <- c("ram", "shyam", "tulsi")
charvv
class(charvv)


# 4 Logical vector
#vector with true and false will be  known as logical vector. numbers can be converted into logical vector





# Accessing Vector Elements
