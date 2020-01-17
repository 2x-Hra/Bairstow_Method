

def b_cal_(coef_arr, k , n,r_coef,s_coef):

	if (k == n+1 or k == n+2):
		return 0

	return coef_arr[k] + r_coef * b_cal_(coef_arr,k+1,n,r_coef,s_coef) + s_coef * b_cal_(coef_arr,k+2,n,r_coef,s_coef)
	
def c_cal_(coef_arr, k , n,r_coef,s_coef):

	if (k == n+1 or k == n+2):
		return 0

	return coef_arr[k] + r_coef * b_cal_(coef_arr,k+1,n,r_coef,s_coef) + s_coef * b_cal_(coef_arr,k+2,n,r_coef,s_coef)
	
def D_cal_(c1,c2,c3):

def D1_cal(b0,b1,c2,c3):

def D2_cal(c1,c2,b0,b1):

def r_cal_(r_prev,D1,D):
	
	''' if ((r_new - r_prev)<0.0000001 ):
	 
	'''

def s_cal_(s_prev,D2,D):
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