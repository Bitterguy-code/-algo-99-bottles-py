# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down and pass it around, 98 bottles of beer on the wall.
# 98 bottles of beer on the wall, 98 bottles of beer.

def bottle_song():
	for i in range(99,0,-1):
		if i > 1:
			print(str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer.")
			print("Take on down and pass it around, " + str(i-1) + " bottles of beer on the wall.")
		else:
			print(str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer.")
			print("Take on down and pass it around, no more bottles of beer on the wall.")
	pass

bottle_song()

####kldjsfalkfdajalskdfjdfls