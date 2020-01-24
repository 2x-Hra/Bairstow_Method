
import numpy as my_numpy
import random
import cmath
''' FUNCTIONS '''





# WHY DO U WANNA COPY my CODE?


''' ~~~~~~~~~~~~ MAIN ~~~~~~~~~~~~ '''

if __name__ == "__main__":





	
	coef_b = []
	coef_c = []

	
	coef_a =[]

	
	counter3 = 0
	degree = int(input())
	coefficients = input()
	coefficients_arr = coefficients.split()
	

	while(counter3 <len(coefficients_arr)):
		coef_a.append(int(coefficients_arr[counter3]))
		counter3 +=1	

	# print(coef_a)
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
	# print(final_roots)
	counter = 0
	while(counter < len(final_roots)):
		if(final_roots[counter].imag >= 0):
			result[0] = (round(result[0] + final_roots[counter].real,6))
			result[1] = result[1] + final_roots[counter].imag
		counter +=1
	print(str(result[0])+ " " + str(result[1]))

		
	
		




















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
	