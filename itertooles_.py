# itertools:product,permutations,combinations,accumulate,gropby ,and infinite iterators

# from itertools import product
# a=[1,2]
# b=[3,4]
# prod=product(a,b)
# # cartitian product 
# print(list(prod)) 
# prod2=product(a,b,repeat=2)
# print(list(prod2))

# from itertools import permutations
# a=[1,2,3]
# count=0
# perm=permutations(a)
# print(list(perm))
# perm=permutations(a)
# for i in perm:
#     if i!=0:
#         count+=1
# print(count)

# b=[1,2,3]
# per=permutations(b,2)
# print(list(per))

# from itertools import combinations
# a=[1,2,3,4]
# comb=combinations(a,1)
# comb1=combinations(a,2)
# comb2=combinations(a,3)
# comb3=combinations(a,4)
# comb4=combinations(a,5)
# print(list(comb))
# print(list(comb1))
# print(list(comb2))
# print(list(comb3))
# print(list(comb4))

# from itertools import combinations,combinations_with_replacement
# a=[1,2,3,4]
# comb=combinations(a,2)
# print(list(comb))
# comb_wi=combinations_with_replacement(a,2)
# print(list(comb_wi))


# from itertools import accumu late
# a=[1,2,3,4]
# acc=accumulate(a)
# print(a)
# print(list(acc))

# from itertools import accumulate
# import operator
# a=[1,2,5,3,4]
# acc=accumulate(a,func=operator.mul)
# acc1=accumulate(a,func=max)
# print(a)
# print(list(acc))
# print(list(acc1)) 


#  from itertools import groupby