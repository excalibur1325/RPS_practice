coursesAvailable = ['History', 'Math', 'Biology', 'Botany', 'Physics']
coursesAvailable2 = ['Art', 'Communication', 'Business']
nums = [1,5,9,3,4,7,2]
# -1 in the square brackets shows the last item in the list
# 0 is the first item
# (nothing):2 the colon is "go-to but not to include" the number (2) is the stopping point
# difference between "append", "insert", "extend"
coursesAvailable.append('Music')
coursesAvailable.insert(3,'Engineering')
coursesAvailable.extend(coursesAvailable2)

# variable.sort = sorts the list alphabetically (numbers in ascending)
# variable.reverse = sorts the list in reverse order
# passing the argument sort(reverse=Ture) in the sort() will invert(descending) the order 
coursesAvailable.reverse()
coursesAvailable2.sort()
nums.sort(reverse=True)

# another way to organize your list without altering the original is to use the sorted function
# sorted_courses = sorted(coursesAvailable)

# variable.remove will remove any item in the list
# pop will by default remove the last item in the list
coursesAvailable.remove('Math')
popped = coursesAvailable.pop()
# you can set the popped value as a variable to pull the returned value


print(popped)
# print(sorted_courses)
print(coursesAvailable)
print(nums)
