def fact(n :int ) -> int:
	
	if(n == 0 or n==1):
		return 1
	return n*fact(n-1)
	
print("enter the number you want factorial")
n = int(input())
	
print(fact(n))
