def indv(n):
#Calculate tax based on tax bracket
	if n < 9525:
		t_indv = n - ((n * 0.1) + (n * .033) + (n * .0505))
	elif 9526 < n < 38700:
		t_indv = n - ((n * 0.12) + (n * .033) + (n * .0505))
	elif 38701 < n < 82500 :
		t_indv = n - ((n * 0.22) + (n * .033) + (n * .0505))
	elif 82501 < n < 157500:
		t_indv = n - ((n * 0.24) + (n * .033) + (n * .0505))
	elif 157501 < n < 200000:
		t_indv = n - ((n * 0.32) + (n * .033) + (n * .0505)) 	
	elif 200001 < n < 500000:
		t_indv = n - ((n * 0.35) + (n * .033) + (n * .0505))
	else:
		t_indv = n - ((n * 0.37) + (n * .033) + (n * .0505))
        print("Individual Filing income after tax is approximately ", t_indv)

def mfj(n):
	#Calculate tax based on tax bracket
	if n < 19050:
		t_mfj = n - ((n * 0.1) + (n * .033) + (n * .0505))
	elif 19051 < n < 77400:
		t_mfj = n - ((n * 0.12) + (n * .033) + (n * .0505))
	elif 77401 < n < 165000 :
		t_mfj = n - ((n * 0.22) + (n * .033) + (n * .0505))
	elif 165001 < n < 315000:
		t_mfj = n - ((n * 0.24) + (n * .033) + (n * .0505))
	elif 315001 < n < 400000:
		t_mfj = n - ((n * 0.32) + (n * .033) + (n * .0505))
	elif 400001 < n < 600000:
		t_mfj = n - ((n * 0.35) + (n * .033) + (n * .0505))
	else:
		t_mfj = n - ((n * 0.37) + (n * .033) + (n * .0505))
        print("Married Filing Jointly income after tax is approximately ", t_mfj)
