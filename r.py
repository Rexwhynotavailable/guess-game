import random
r = random.randint(1, 100)


while True:
	guess = input("請猜一個數字:")
	guess = int(guess)
	if r == guess:
		print("你答對了!")
		break
	elif guess > 100 or guess < 1:
		print("請輸入1及100之間的數字")
	elif guess > r:
		print("你答錯了!數字太大了!")
	elif guess < r:
	    print("你答錯了!數字太小了!") 
		
	
