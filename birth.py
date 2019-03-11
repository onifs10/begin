def birthdayCakeCandles(ar):
   return(ar.count(max(ar)))

ar = list(map(int, input().rstrip().split()))

print(birthdayCakeCandles(ar))