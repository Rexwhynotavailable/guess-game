import random
r = random.randint(1, 100)
count = 0
times = 10 

while True:
	count = count + 1    #count += 1  快寫法
	times = times - 1
	guess = input("請猜一個數字:")
	guess = int(guess)
	if times == 0:
		print("沒機會了!請加油")
		break
	if r == guess:
		print("恭喜你! 你在第", count, "次答對了!")
		break
	elif guess > 100 or guess < 1:
		print("請輸入1及100之間的數字")
	elif guess > r:
		print("數字太大了")
	elif guess < r:
		print("數字太小了!")	
	print("你還剩", times, "次機會，請小心")
	print("---------------------------------")