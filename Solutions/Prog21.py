def main():
	# movements = "UP 5\nDOWN 3\nLEFT 3\nRIGHT 2".split('\n')
	movements = input().split('\n')
	traces = []
	coordinates = [0, 0]
	for movement in movements:
		traces.append((movement.split(' ')[0], int(movement.split(' ')[1])))
	for trace in traces:
		if trace[0] == 'UP':
			coordinates[1] += trace[1]
		elif trace[0] == 'DOWN':
			coordinates[1] -= trace[1]
		elif trace[0] == 'LEFT':
			coordinates[0] -= trace[1]
		elif trace[0] == 'RIGHT':
			coordinates[0] += trace[1]
	print (int((coordinates[0]**2 + coordinates[1]**2)**0.5))


if __name__ == '__main__':
	main()

