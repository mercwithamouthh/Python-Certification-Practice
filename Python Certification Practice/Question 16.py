#You are developing a Python application for your company.
#You write the following code
numList = [1,2,3,4,5]
aplhaList = ["a", "b", "c", "d", "e"]
print(numList is aplhaList)
print(numList == aplhaList)
numList = aplhaList
print(numList is aplhaList)
print(numList == aplhaList)

#false
#false
#true
#true