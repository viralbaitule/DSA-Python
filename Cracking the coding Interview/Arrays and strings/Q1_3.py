
def permute_and_check(s1,s2,l,r,check):
	
	if (l==r):
		print (s1)
		if s1==s2:
			check="True"	
	else:
		for i in range(l,r+1):
			s1[l],s1[i]=s1[i],s1[l]
			check=permute_and_check(s1,s2,l+1,r,check)
			s1[l],s1[i]=s1[i],s1[l]
	return check

def check_permutation(s1,s2):
	if len(s1)!=len(s2):
		return False
	s1=list(s1)
	s2=list(s2)
	return(permute_and_check(s1,s2,0,len(s1)-1,"False"))
	

s1="dog"
s2="god"


print(check_permutation(s1,s2))