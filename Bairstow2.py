
''' FUNCTIONS '''

def b_cal_(coef_arr, k , n,r_coef,s_coef):

	if (k == n+1 or k == n+2):
		return 0

	return coef_arr[k] + r_coef * b_cal_(coef_arr,k+1,n,r_coef,s_coef) + s_coef * b_cal_(coef_arr,k+2,n,r_coef,s_coef)
	
def c_cal_(coef_arr, k , n,r_coef,s_coef):

	if (k == n+1 or k == n+2):
		return 0

	return coef_arr[k] + r_coef * c_cal_(coef_arr,k+1,n,r_coef,s_coef) + s_coef * c_cal_(coef_arr,k+2,n,r_coef,s_coef)


''' Main '''

coef_b = []
coef_c = []
coef_a = [6.0000,4.0000,3.0000,1.0000,1.0000]
i=0
r = -2.1
s = -1.9
while (i<len(coef_a)):
	temp = b_cal_(coef_a,i,len(coef_a)-1,r,s)
	coef_b.append(temp)
	i +=1
print(coef_b)
i=0
while (i<len(coef_b)):
	temp = c_cal_(coef_b,i,len(coef_b)-1,r,s)
	coef_c.append(temp)
	i +=1
print(coef_c)
# def D_cal_(c1,c2,c3):

# def D1_cal(b0,b1,c2,c3):

# def D2_cal(c1,c2,b0,b1):

# def r_cal_(r_prev,D1,D):
	
# 	''' if ((r_new - r_prev)<0.0000001 ):
	 
# 	'''

# def s_cal_(s_prev,D2,D):
# 	# body




