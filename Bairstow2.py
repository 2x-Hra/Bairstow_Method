
import numpy as my_numpy

''' FUNCTIONS '''

def b_cal_(coef_arr, k , n,r_coef,s_coef):

	if (k == n+1 or k == n+2):
		return 0

	return coef_arr[k] + r_coef * b_cal_(coef_arr,k+1,n,r_coef,s_coef) + s_coef * b_cal_(coef_arr,k+2,n,r_coef,s_coef)
	
def c_cal_(coef_arr, k , n,r_coef,s_coef):

	if (k == n+1 or k == n+2):
		return 0

	return coef_arr[k] + r_coef * c_cal_(coef_arr,k+1,n,r_coef,s_coef) + s_coef * c_cal_(coef_arr,k+2,n,r_coef,s_coef)

def D_cal_(coef_c):
	return (coef_c[1] * coef_c[3]) - (coef_c[2]*coef_c[2])

def D1_cal_(coef_b,coef_c):
	return (-coef_b[0] * coef_c[3])-(coef_c[2] * -coef_b[1])

def D2_cal_(coef_b,coef_c):
	return (coef_c[1] * -coef_b[1] - (-coef_b[0] * coef_c[2]))

def r_cal_(r_prev,D1,D):
	return r_prev + D1/D

def s_cal_(s_prev,D2,D):
	return s_prev + D2/D

def poly_div_(arr1,arr2):
	poly1 = my_numpy.array(arr1)
	poly2 = my_numpy.array(arr2)
	Q, R = my_numpy.polydiv(p2, p1)
	return Q



''' ~~~~~~~~~~~~ MAIN ~~~~~~~~~~~~ '''

if __name__ == "__main__":
	
	''' ~~~~ Variables ~~~~'''
	
	coef_b = []
	coef_c = []
	coef_a = [-3.0000,2.0000,1.0000,0.0000,-1.0000,-1.0000]
	i=0
	r = -2.1
	s = -1.9

	''' ~~~~ ~~~~'''

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

	s_prev = s
	s_next = s_cal_(s_prev,D2_cal_(coef_b,coef_c),D_cal_(coef_c))
	r_prev = r
	r_next=r_cal_(r_prev,D1_cal_(coef_b,coef_c),D_cal_(coef_c))

	while(( abs(r_next - r_prev) >0.000001 ) or ( abs(s_next - s_prev) > 0.000001 )):

		i=0
		coef_b = []
		coef_c = []
		while (i<len(coef_a)): 
			temp = b_cal_(coef_a,i,len(coef_a)-1,r_next,s_next)
			coef_b.append(temp)
			i +=1
		# print ("COEF _ B HERE " + str(coef_b))

		i=0

		while (i<len(coef_b)): 
			temp = c_cal_(coef_b,i,len(coef_b)-1,r_next,s_next)
			coef_c.append(temp)
			i +=1
		# print ("COEF _ C HERE " + str(coef_c))


		r_prev = r_next
		r_next = r_cal_(r_prev,D1_cal_(coef_b,coef_c),D_cal_(coef_c))
		s_prev = s_next
		s_next = s_cal_(s_prev,D2_cal_(coef_b,coef_c),D_cal_(coef_c))
		
	print ( "r - prev :" + str( r_prev))
	# print ( "r_next : " + str(r_next))
	print ("s_prev :" + str(s_prev))
	# print ("s_next : "+ str(s_next))
	print (my_numpy.roots([1,-r_prev,-s_prev]))

	# print(D_cal_(coef_c))
	# print(D1_cal_(coef_b,coef_c))
	# print(D2_cal_(coef_b,coef_c))
	# print(r_cal_(r,D1_cal_(coef_b,coef_c),D_cal_(coef_c)))
	# print(s_cal_(s,D2_cal_(coef_b,coef_c),D_cal_(coef_c)))

