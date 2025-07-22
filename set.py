# set: unorrdered,mutable,no duplicates

set1={1,2,3}
print(set1)

set2={1,2,3,2,3}
print(set2)

set3=set([1,2,3,2])
print(set3)

set4={"hellow"}
print(set4)

set5=set("hellow")
print(set5)

set6=set()
set6.add(1)
set6.add(2)
print(set6)

set7=set6.union(set5)
print(set7)

