# Tuple:ordered,immutable,allows duplicate elements

# t1="ram",58,"shyam"
# print(t1)
# print(type(t1))
# for i in t1:
#     print(i)
# item=t1[0]
# print(item)

# if "ram" in  t1:
#     print("yes")
# else:
#     print("no")

# to check the number of bites occupy 

# import sys
# list1=[0,1,2,"hellow",True]
# tuple1=(0,1,2,"hellow",True)
# print(sys.getsizeof(list1),"bytes")
# print(sys.getsizeof(tuple1),"bytes")

# to check the timing of iteration

# import timeit
# print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=100000000))
# print(timeit.timeit(stmt="(0,1,2,3,4,5)",number=100000000))