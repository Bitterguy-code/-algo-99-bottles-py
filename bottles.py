bottles = int(input("Enter how many bottles you want: "))

def bottle_song(max):
	if max > 1:
		print(str(max) + " bottles of bear on the wall, " + str(max) + " bottles of beer.")
		print("Take one down, pass it around " + str(max-1) + " bottles of beer on the wall")
		bottle_song(max-1)
	elif max == 1:
		print(str(max) + " bottles of bear on the wall, " + str(max) + " bottles of beer.")
		print("Take one down, pass it around no more bottles of beer on the wall")
		bottle_song(max-1)
	elif max == 0:
		pass
	

bottle_song(bottles)

