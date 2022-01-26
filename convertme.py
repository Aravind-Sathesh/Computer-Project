# take input as (123+3*2+4^8-5/9)
# inputs include log()_(), ln(), sin(), cos(), tan()
import math

sin = "sin"
ln = "ln"
tan = "tan"
cos = "cos"

inp = input("equation= :")

direct = False 

def check1(eq):
	for i in eq:
		if i.isalpha() == False:
			direct = True
		else:
			pass

	if ln in eq:
		starti = eq.find(ln)
		endi = eq.find((")"),starti)
		return(eq,"2",starti,endi)
		#we are trying to find the length of the log(xyz) function, so we find the immediate ")" after our ln function
	elif sin in eq:
		starti = eq.find(sin)
		endi = eq.find((")"),starti)
		return(eq,"3",starti,endi)
	elif cos in eq:
		starti = eq.find(cos)
		endi = eq.find((")"),starti)
		return(eq, "4",starti,endi)
	elif tan in eq:
		starti = eq.find(tan)
		endi = eq.find((")"),starti)
		return(eq, "5",starti,endi)
	elif direct== True:
		return(eq,"1",0,0)
	else:
		print("enter a valid input")
		

def solve1(eqf,mode,starti,endi):
	#replacing to math python formatting
	eqfn = eqf.replace("^", "**")
	if mode == "1":
		print(eval(eqfn))
	elif mode == "2":
		toreplace = eqf[starti:(endi+1)]
		sliced = eqf[starti+2:(endi+1)]
		value = math.log(eval(sliced),2)
		edited = eqf.replace(toreplace,str(value))
		print(eval(edited))
	elif mode == "3":
		toreplace = eqf[starti:(endi+1)]
		sliced = eqf[starti+3:(endi+1)]
		value = math.sin(math.radians(eval(sliced)))
		edited = eqf.replace(toreplace,str(value))
		print(eval(edited))
	elif mode == "4":
		toreplace = eqf[starti:(endi+1)]
		sliced = eqf[starti+3:(endi+1)]
		value = math.cos(math.radians(eval(sliced)))
		edited = eqf.replace(toreplace,str(value))
		print(eval(edited))
	else:
		toreplace = eqf[starti:(endi+1)]
		sliced = eqf[starti+3:(endi+1)]
		value = math.tan(math.radians(eval(sliced)))
		edited = eqf.replace(toreplace,str(value))
		print(eval(edited))


		
	


#calling the function, it gives the items back in a list
print(solve1(check1(inp)[0],check1(inp)[1],check1(inp)[2],check1(inp)[3]))








