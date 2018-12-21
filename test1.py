import sys
import os
import time
import difflib
import platform
print("###########################################")
print()
print("/** this is a test file for COMP9024 assn1")
print("  * Author: Ricky Qi")
print("  * Email: bitxspace@gmail.com")
print("  */")
print("Please read the ReadMe.txt first")
print()
if 'ind' in platform.system():
	print("windows is not a legal env!")
	sys.exit()
def readfile(filename):
    try:
        with open(filename, 'r') as fileHandle:
            text = fileHandle.read().splitlines()
        return text
    except IOError as e:
        print("Read file Error:", e)
        sys.exit()

if ((not os.path.isfile('listIteratorInt.c')) | (not os.path.isfile('listIteratorInt.h'))):
	print("Please put your assn1 file to current directory!!");
	sys.exit(1);
if (os.path.isfile('final_report.html')):
	os.system("rm -rf final_report.html")
command1 = "git clone https://github.com/RickyYhQi/COMP9024.git"
os.system(command1)
os.system("cp listIteratorInt.c COMP9024/new_project/src/ricky/")
os.system("cp listIteratorInt.h COMP9024/new_project/src/ricky/")
os.chdir("COMP9024/new_project/")
os.system("make")

print("If the error keyword is not displayed on the command line... \nThen congratulations on completing the first phase.")
print("\n")

os.chdir("tests/")

text1 = readfile('tests.log')
text2 = readfile('standard_result.log')
d = difflib.HtmlDiff()
result = d.make_file(text1, text2, 'your_output', 'standard_result', context=True)

with open("final_report.html", 'w') as resultfile:
    resultfile.write(result)
os.system("cp final_report.html ../../../")
os.system("cp tests.log ../../../")
os.system("cp standard_result.log ../../../")
os.chdir("../../../")
print("Done !!!  \nPlease check final_report.html in current dir!! \ncompleting the second phase.")
os.system("rm -rf COMP9024")


