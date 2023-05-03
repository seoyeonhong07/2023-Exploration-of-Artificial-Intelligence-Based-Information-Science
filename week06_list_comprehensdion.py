#week06_list_comprehension

#n = []
#n.append(1*1)
#n.append(2*1)
#n.append(3*1)
#n.append(4*1)
#n.append(5*1)
#n.append(6*1)


#n =[]
#for i in range(1,6):
#    n.append(i*i)
#print(n)


#def squares(number) :
#    return number * number
#
#n = list(map(squares, list(range(1,6))))
#print(n)


# n = list(map(lambda x : x*x, list(range(1,6))))
# print(n)


# list comprehension (more pythonic)
n = [x*x for x in range(1, 6)]
print(n)

