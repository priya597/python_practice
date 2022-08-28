#program to count the number of comparison
#operations executed by FIRST and SECOND */

# FIRST
c1 = 1
# c2 = 1
i = 0
while (i < c1 and i < 10):
	j = -1
	c1 += 1 #2
	while (j < c1 and j < 20):
		c1 += 1 #3
		j += 1 #0
	i += 1

# SECOND
# i = 0
# while (i < c2 and i < 100):
# 	j = -1
# 	c2 += 1
# 	while (j < c2 and j < 10):
# 		c2 += 1
# 		j += 1
# 	i += 1
	
print(" Count fot FIRST " , c1)
# print(" Count fot SECOND " , c2)

# This code is contributed by shivanisinghss2110

