
import numpy as my_numpy
import random
import cmath
''' FUNCTIONS '''

def b_cal_(coef_arr, k , n,r_coef,s_coef):
	# print(coef_arr)
	if (k == n+1 or k == n+2):
		return 0

	return coef_arr[k] + r_coef * b_cal_(coef_arr,k+1,n,r_coef,s_coef) + s_coef * b_cal_(coef_arr,k+2,n,r_coef,s_coef)
	
def c_cal_(coef_arr, k , n,r_coef,s_coef):

	if (k == n+1 or k == n+2):
		return 0

	return coef_arr[k] + r_coef * c_cal_(coef_arr,k+1,n,r_coef,s_coef) + s_coef * c_cal_(coef_arr,k+2,n,r_coef,s_coef)

def D_cal_(coef_c):
	# tempC = list(reversed(coef_c))
	return (coef_c[1] * coef_c[3]) - (coef_c[2]*coef_c[2])

def D1_cal_(coef_b,coef_c):
	# tempC = list(reversed(coef_c))
	# tempB = list(reversed(coef_b))
	return (-coef_b[0] * coef_c[3])-(coef_c[2] * -coef_b[1])

def D2_cal_(coef_b,coef_c):
	# tempC = list(reversed(coef_c))
	# tempB = list(reversed(coef_b))
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


def b_array_calculator(coef_a,coef_b,r_coef,s_coef):
	i=0
	while (i<len(coef_a)): 
		temp = b_cal_(coef_a,i,len(coef_a)-1,r_coef,s_coef)
		coef_b.append(temp)
		i +=1
	return coef_b

def c_array_calculator(coef_b,coef_c,r_coef,s_coef):	
	i=0
	while (i<len(coef_b)): 
		temp = c_cal_(coef_b,i,len(coef_b)-1,r_coef,s_coef)
		coef_c.append(temp)
		i +=1
	return coef_c

def calculate_newCoef (coef_a,coef_b,coef_c,roots,r_coef,s_coef,rs_container):
	
	b_array_calculator(list(reversed(coef_a)),coef_b,r_coef,s_coef)
		#chun arraye Coef_A be tartibe zaribe bishtarin tavan hast va man baraye mohasebeye 
		#b niaz be artibe az 0 daram array ra Reverse miknam va mifrestam

	c_array_calculator(coef_b,coef_c,r_coef,s_coef)
		# dar inja niaz be reverse nis chun array b ke towliad mishavad moratab ast

	# print(r_coef,s_coef)
	s_prev = s
	s_next = s_cal_(s_prev,D2_cal_(coef_b,coef_c),D_cal_(coef_c))
	r_prev = r
	r_next=r_cal_(r_prev,D1_cal_(coef_b,coef_c),D_cal_(coef_c))
	# counter = 0
	while(( abs(r_next - r_prev) > 0.000001 ) and abs(s_next - s_prev) > 0.000001 ):

		
		coef_b = []
		coef_c = []

		b_array_calculator(list(reversed(coef_a)),coef_b,r_next,s_next)

		c_array_calculator(coef_b,coef_c,r_next,s_next)
		
		r_prev = r_next	
		r_next = r_cal_(r_prev,D1_cal_(coef_b,coef_c),D_cal_(coef_c))
		s_prev = s_next
		s_next = s_cal_(s_prev,D2_cal_(coef_b,coef_c),D_cal_(coef_c))
		# print ( " r Jadid = " + str(r_next) + " S jadid = " + str(s_next) + " Dowre " +str(counter) )
		# counter +=1 
		
	rs_container.append(r_next)
	rs_container.append(s_next)
	roots.append(list(my_numpy.roots([1,-r_next,-s_next])))
	
	 
	
	coef_a = poly_div_(coef_a,[1,-r_next,-s_next]) #inja darim poly jadidemun ro be dast miarim 
	
	return coef_a

def final_roots_array_maker (roots_array):
	temp=[]
	counter =0
	counter2 =0
	while ( counter < len(roots)):
		counter2= 0
		while ( counter2 < len((roots)[counter]) ):
			temp.append(round(roots[counter][counter2],6)) 
			counter2 +=1
		counter+=1
	return temp

''' ~~~~~~~~~~~~ MAIN ~~~~~~~~~~~~ '''

if __name__ == "__main__":





	
	coef_b = []
	coef_c = []

	
	coef_a =[]

	while(True):
		counter3 = 0
		degree = int(input("Degree ? "))
		coefficients = input("Coefficents ? ")
		coefficients_arr = coefficients.split()
		if (len(coefficients_arr)== degree+1):

			while(counter3 <len(coefficients_arr)):
				coef_a.append(int(coefficients_arr[counter3]))
				counter3 +=1	

			print(coef_a)
			roots =[]
			rs_container =[]
			i=0
			r = -2.1
			s = -1.9

			''' ~~~~ ~~~~'''

			while(True):

				if(len(coef_a) > 3 ): # agar bishtr az daraje 2 bood
					coef_a = calculate_newCoef(coef_a,coef_b,coef_c,roots,r,s,rs_container)
				
				else:
					
					roots.append(list(my_numpy.roots(coef_a)))
					break
			#---------------------------#

			''' Outputs'''

			final_roots =[]
			final_roots = final_roots_array_maker(roots)
			result =[0,0]
			print(final_roots)
			counter = 0
			while(counter < len(final_roots)):
				if(final_roots[counter].imag >= 0):
					result[0] = (round(result[0] + final_roots[counter].real,6))
					result[1] = result[1] + final_roots[counter].imag
				counter +=1
			print(str(result[0])+ " " + str(result[1]))

			ques = input("Do you wanna try again? ")
			if (ques == "yes"):
				continue
			else:
				break
		else:
			ques = input("Do you wanna try again? ")
			if (ques == "yes"):
				continue
			else:
				break
		 




















	#---------------------------#
	
	## ina baraye Check kardan function haye khodam hast ke hamegi check shode va dorost ast
	### tebghe mesale ketab
	
	# print(b_array_calculator(list(reversed(coef_a)),coef_b,r,s)) 
	# print(c_array_calculator(coef_b,coef_c,r,s)) 
	# s_prev = s
	# print("S prev :" + str(s_prev))
	# s_next = s_cal_(s_prev,D2_cal_(coef_b,coef_c),D_cal_(coef_c))
	# print("S next :" + str(s_next))
	# r_prev = r
	# print("r prev :" + str(r_prev))
	# r_next=r_cal_(r_prev,D1_cal_(coef_b,coef_c),D_cal_(coef_c))
	# print("r next :" + str(r_next))
	