def CheckWhoWinElection(A):
	A.sort()
	counter=maxCounter=1
	winningCandidate=candidate=A[0]
	for i in  range(0,len(A)-1):
		if A[i]==A[i+1]:
			candidate=A[i]
			counter+=1
		else:
			counter=1
		if maxCounter<counter:
			winningCandidate=candidate
			candidate=A[i]
			maxCounter=counter
	return ("Candidate ",winningCandidate," has appeared ",maxCounter," times")





A=[3,2,4,1,3,2,4,2,4,4,4]
print(CheckWhoWinElection(A))