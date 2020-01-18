
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
	Q, R = my_numpy.polydiv(arr1, arr2)
	return Q






def calculate_newCoef (coef_a,coef_b,coef_c,roots,r,s,rs_container):
	
	i=0

	''' ~~~~ ~~~~'''

	while (i<len(coef_a)): 
		temp = b_cal_(coef_a,i,len(coef_a)-1,r,s)
		coef_b.append(temp)
		i +=1
		
	
	i=0
	while (i<len(coef_b)): 
		temp = c_cal_(coef_b,i,len(coef_b)-1,r,s)
		coef_c.append(temp)
		i +=1
	

	s_prev = s
	s_next = s_cal_(s_prev,D2_cal_(coef_b,coef_c),D_cal_(coef_c))
	r_prev = r
	r_next=r_cal_(r_prev,D1_cal_(coef_b,coef_c),D_cal_(coef_c))
	counter = 0
	while(( abs(r_next - r_prev) >0.000001 )  ):

		i=0
		coef_b = []
		coef_c = []
		while (i<len(coef_a)): 
			temp = b_cal_(coef_a,i,len(coef_a)-1,r_next,s_next)
			coef_b.append(temp)
			i +=1
		# print(str(i)+"Omin B :" + str(coef_b))

		i=0

		while (i<len(coef_b)): 
			temp = c_cal_(coef_b,i,len(coef_b)-1,r_next,s_next)
			coef_c.append(temp)
			i +=1
		# print(str(i)+"Omin C :" + str(coef_c))


		r_prev = r_next
		r_next = r_cal_(r_prev,D1_cal_(coef_b,coef_c),D_cal_(coef_c))
		s_prev = s_next
		s_next = s_cal_(s_prev,D2_cal_(coef_b,coef_c),D_cal_(coef_c))
		print ( " r Jadid = " + str(r_next) + " S jadid = " + str(s_next) + " Dowre " +str(counter) )
		counter +=1 


	
	rs_container.append(r_prev)
	rs_container.append(s_prev)
	roots.append(my_numpy.roots([1,-r_next,-s_next]))
	
	
	print(coef_a)
	print("in Fucntion roots" + str(roots))
	
	coef_a = poly_div_(coef_a,[1,-r_next,-s_next]) #inja darim poly jadidemun ro be dast miarim 
	
	# print("in bairstow function" +str(coef_a))
	
	return coef_a










''' ~~~~~~~~~~~~ MAIN ~~~~~~~~~~~~ '''

if __name__ == "__main__":
	
	''' ~~~~ Variables ~~~~'''
	
	coef_b = []
	coef_c = []
	coef_a = [-3.0000,2.0000,1.0000,0.0000,-1.0000,-1.0000]
	roots =[]
	rs_container =[]
	i=0
	r = -2.1
	s = -1.9

	''' ~~~~ ~~~~'''

	while(True):

		if(len(coef_a) > 3 ):
			coef_a = calculate_newCoef(coef_a,coef_b,coef_c,roots,r,s,rs_container)
			print ("THIS IS r " + str(r))
			print ("THIS IS S " + str(s))
			print("THIS IS COEF " + str(coef_a))
		else:
			
			roots.append(my_numpy.roots(coef_a))
			break
	print ("after while roots :" + str(roots))
	print ("THIS IS RS CONTAINER :" + str(rs_container))