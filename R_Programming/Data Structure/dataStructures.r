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