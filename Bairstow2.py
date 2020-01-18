
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




''' ~~~~~~~~~~~~ MAIN ~~~~~~~~~~~~ '''

if __name__ == "__main__":
	
	''' ~~~~ Variables ~~~~'''
	
	coef_b = []
	coef_c = []
	coef_a = [6.0000,4.0000,3.0000,1.0000,1.0000]
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

	while(( r_next - r_prev >0.000001 ) or ( s_next - s_prev > 0.000001 )):

		i=0
		coef_b = []
		coef_c = []
		while (i<len(coef_a)): 
			temp = b_cal_(coef_a,i,len(coef_a)-1,r_next,s_next)
			coef_b.append(temp)
			i +=1

		i=0
		while (i<len(coef_b)): 
			temp = c_cal_(coef_b,i,len(coef_b)-1,r_next,s_next)
			coef_b.append(temp)
			i +=1

			
		r_prev = r_next
		r_next = r_cal_(r_prev,D1_cal_(coef_b,coef_c),D_cal_(coef_c))
		s_prev = s_next
		s_next = s_cal_(s_prev,D2_cal_(coef_b,coef_c),D_cal_(coef_c))
		print ( "prev :" + str( r_prev))
		print ( r_next)

	# print(D_cal_(coef_c))
	# print(D1_cal_(coef_b,coef_c))
	# print(D2_cal_(coef_b,coef_c))
	# print(r_cal_(r,D1_cal_(coef_b,coef_c),D_cal_(coef_c)))
	# print(s_cal_(s,D2_cal_(coef_b,coef_c),D_cal_(coef_c)))

	# p2 = m_numpy.array([1, 1, 3, 4, 6])
	# p1 = m_numpy.array([1, 2, 2])
	# quotient, remainder = m_numpy.polydiv(p2, p1)