# Use enumerate() and zip() for paired iteration

animals = ["whale", "crow", "cow", "hare", "white_stag"]
count = [12, 512, 56, 1293, 1]

# enumerate()
for index, animal in enumerate(animals):
	print(index, animal)
print('\n')

for index, animal in enumerate(animals, start=1):
	print(index, animal)
print('\n')

# zip()
for animal, num in zip(animals, count):
	print(f"There are {num} of {animal} down here!")
