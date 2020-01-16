
def b_cal_(coef_arr, k , n,r_coef,s_coef):
	






n = int(input ("Enter N :"))
coef_arr = []
i = 0

coefs = input ("Enter all of them :")
coef_arr = coefs.split()
print(len(coef_arr))
if (len(coef_arr) != n):
	print("ERROR wrong tedad")
else:
	while( i < n):
		coef_arr[i] = int(coef_arr[i])
		i += 1
	
	#  CALL THE FUNCTION HERE
print (coef_arr)


# n = int(n)
print(type(n))