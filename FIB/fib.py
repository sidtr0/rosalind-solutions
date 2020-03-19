n = int(input("Enter positive integer (<= 40): "))
k = int(input("Enter positive integer (<= 5): "))
mature_rabbits = 1
immature_rabbits = 0

def liveRabbits(months, k):
	F1 = 1
	F2 = 1
	for i in range(months - 2):
		F3 = F1 * k + F2
		F1 = F2
		F2 = F3
	return F3

print(liveRabbits(n, k))