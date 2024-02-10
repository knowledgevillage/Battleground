# # Datastructures in R
# #vector
# matrix
# array
# list
# data Frame


#Vector
#Definition -- What is a vector in R example?
# A vector is the basic data structure in R that stores data of similar types. For example, Suppose we need to record the age of 5 employees. Instead of creating 5 separate variables, we can simply create a vector.
#elements of vactor is known as components
# #vetore are of two type 
# 1 - Atomic vector
# 2 - List

#how to create a vectore - vector is creating using c function.
a<-c(1,2,3,4,5,6,7)
#this one type of defining a vectore. it will return one - dimensional array

#vectore using ":" oprator

b<- c(1:6)

a
b

#vector using sequence function
c<- seq(1,6)
c

d<-seq(1,8,by=.4) #by decide interval windows in the rane
d



e<-seq(1,8,length.out = 5) #length.out is used to define the number of output element. interval will be be calcualed by r directly. 
e




#numeric vector
numv <- c(12.3, 526,45.78, 4567.9)
numv
class(numv)


#integer vector

intv <- c(12,346,24,765)
intv
class(intv)

#converting numeric vector data type to integer
intv1 <- as.integer(intv)
class(intv1)


