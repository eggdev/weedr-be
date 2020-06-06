from sys import argv
from os.path import exists
# script is the file being called
# each one after is the available arguement passed
# script, butts, second, third = argv
# You can redefine first to butts and have that variable defined
# Open uses a string to find the filename. Can hard code extension
# txt = open(f"{filename}.txt")
# print(txt.read())

# target = open(filename, "w")
# "w" = write "r" = read "a" = append
# target.truncate()
# target.write("text")
# target.close()
# last line finishes it

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright all done")

out_file.close()
