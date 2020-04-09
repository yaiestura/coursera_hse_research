def main():
	with open("emotions.txt", "r") as f:
		count = set(f.readlines())
		print(count)
		print(len(count))


if __name__ == '__main__':
	main()
