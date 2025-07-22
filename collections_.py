# collections: Counter,namedtuple,ordereddict,defaultdict,deque

# from collections import Counter
# a="sudhanshu"
# count1=Counter(a)
# print(count1)

# # most reperted or common element
# # return as list with tuple in it
# print(count1.most_common(1))
# # return tuple 
# print(count1.most_common(1)[0])
# # first element of tuple 
# print(count1.most_common(1)[0][0])

# from collections import namedtuple
# point=namedtuple('point','x,y')
# pt=point(1,-4)
# pt1=point(2,-8)
# print(pt1)
# print(pt)
# print(pt.x,pt.y)

# from collections import defaultdict
# d=defaultdict(int)
# d['a']=1
# d['b']=2
# print(d)

from collections import deque
d=deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
