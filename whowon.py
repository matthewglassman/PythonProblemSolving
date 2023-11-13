apple_threes = int(input());
apple_twos = int(input());
apple_ones = int(input());

banana_threes = int(input());
banana_twos = int(input());
banana_ones = int(input());

apples_total = apple_threes * 3 + apple_twos * 2 + apple_ones
bananas_total = banana_threes * 3 + banana_twos * 2 + banana_ones

if apples_total > bananas_total:
	print("A");
elif apples_total < bananas_total:
	print("B");
else:
	print("T")