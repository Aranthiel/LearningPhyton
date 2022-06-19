def is_prime(num):
    no_primo=0
    if num >= 1:
        for i in range (1, num):
            if num%i == 0:
                no_primo +=1
        if no_primo>2:
            return False
        else:
            return True
    else:
        return False
    

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
