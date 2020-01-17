

def b_cal_(coef_arr, k , n,r_coef,s_coef):

	if (k == n+1 or k == n+2):
		return 0

	return coef_arr[k] + r_coef * b_cal_(coef_arr,k+1,n,r_coef,s_coef) + s_coef * b_cal_(coef_arr,k+2,n,r_coef,s_coef)
	
def c_cal_(coef_arr, k , n,r_coef,s_coef):

	if (k == n+1 or k == n+2):
		return 0

	return coef_arr[k] + r_coef * b_cal_(coef_arr,k+1,n,r_coef,s_coef) + s_coef * b_cal_(coef_arr,k+2,n,r_coef,s_coef)
	

def r_cal_():
	# Body

def s_cal_():
	# body





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
# print (coef_arr)

print(b_cal_(coef_arr,0,n-1,1,2))