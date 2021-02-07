mylist = [1, 2, 3]
mylist = ['stringstuff', 1, 2, 3, 23.2, True, 'asdf', [1, 2, 3]]
print(mylist)
print(len(mylist))
mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(mylist)
print(mylist[:3])

mylist[0] = 'New Item'
print(mylist)

mylist.append("Last Item")
print(mylist)
mylist.append(['x', 'y', 'z'])
print(mylist)
mylist.extend(['x', 'y', 'z'])
print(mylist)
mylist.pop()
mylist.pop()
mylist.pop()
print(mylist)
mylist.pop(0)
print(mylist)
mylist.reverse()
print(mylist)
mylist = [4, 39,6, 7, 8, 9]
print(mylist)
mylist.sort()
print(mylist)

mylist = [1, 2, ['x', 'y', 'z']]
print(mylist[2][0])
print(mylist[2][1])
print(mylist[2][2])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)

first_col = [row[0] for row in matrix]
print(first_col)