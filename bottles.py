def bottle_song():
	x = 99
	while x > 0:
		if x > 1:
			print(f"{(x)} bottles of beer on the wall {(x)} bottles of beer \n Take one down and pass it around, {(x -1)} bottles of beer.")
		if x == 1:
			print(f"{(x)} bottle of beer on the wall {(x)} bottle of beer\n Take one down and pass it around, no more bottles of beer.\n Go to the store and buy some more, 99 bottles of beer on the wall.")
		x = x - 1


bottle_song()


#Make the code take any amount of bottles

def bottle_song(num):
	x = num
	while x > 0:
		if x > 1:
			print(f"{x} bottles of beer on the wall {x} bottles of beer \n Take one down and pass it around, {x - 1} bottles of beer.")
		if x == 1:
			print(f"{x} bottle of beer on the wall {x} bottle of beer\n Take one down and pass it around, no more bottles of beer.\n Go to the store and buy some more, {num} bottles of beer on the wall.")
		x -= 1


bottle_song(500)