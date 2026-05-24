
tuple1=(4,3,2,2,-1,18)
tuple2=(2,4,8,8,3,2,9)
result = tuple(x * y for x, y in zip(tuple1, tuple2))
print(result) 