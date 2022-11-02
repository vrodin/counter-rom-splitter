from os import listdir
from os.path import isfile, join, getsize
import sys

def main(argv):
	Mbit = int(argv[0])
	memByteSize =  Mbit << 17
	path = argv[1]
	files = [[join(path, f), getsize(join(path, f))] for f in listdir(path) if join(path, f)]
	biggestRomSize = max([cfile[1] for cfile in files])
	
	romsCount = int(Mbit/(biggestRomSize >> 17))
	if romsCount < len(files):
		print('Not possible')
		return
	elif romsCount > len(files): 
		
		print('You can add ' + str(romsCount - len(files)) + ' with max size ' + str(biggestRomSize >> 20) + ' MByte')
		
	with open('output.bin', "wb") as output:
		for fl in files:
			with open(fl[0], "rb") as f:
				output.write(f.read() + bytes(0xFF for i in range(biggestRomSize - fl[1])))
				f.close()
	
		output.close()
	print('Done')

if __name__ == "__main__":
	main(sys.argv[1:])
	
