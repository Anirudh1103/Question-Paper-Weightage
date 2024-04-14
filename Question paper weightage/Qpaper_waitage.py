from pypdf import PdfReader
from termcolor import colored
print(colored("Enter the name of the question paper which is in pdf from:  ",'red'))
pdf = input()
reader = PdfReader(pdf)
for i in range(len(reader.pages)):
    page = reader.pages[i]
    with open('whole_qp.txt','w') as f:
        f.write(str(page.extract_text()))
#Extracting the questions from the question paper
with open('whole_qp.txt','r') as infile, open('questions.txt','w') as outfile:
    for line in infile:
        # line = line.strip()
        if line.startswith('1'):
            outfile.write(line)
        if line.startswith('2'):
            outfile.write(line)
        if line.startswith('3'):
            outfile.write(line)
        if line.startswith('4'):
            outfile.write(line)
        if line.startswith('5'):
            outfile.write(line)
#Filtering only integer numbers and writing into a new text file 'bloom.txt'
f = open('questions.txt','r')
bloom = f.read()
with open('bloom.txt','w') as b:
    for i in bloom:
        if i:
            try:
                number = int(i)
                b.write(str(i + '\n'))
            except ValueError:
                pass
bl = open('bloom.txt','r')
y = bl.read()
y = y.split()
i = 3
bloom_level = 0
n = 0
print(colored("BLOOMS LEVEL ARE:......",'red'))
print(colored("1 - Remembering",'red'))
print(colored("2 - Understanding",'red'))
print(colored("3 - Applying",'red'))
print(colored("4 - Analyzing",'red'))
print(colored("5 - Evaluating",'red'))
print(colored("6 - Creating",'red'))
print(colored("_" * 100,'white'))

print(colored('Blooms level in question paper are: ','cyan'))
while i<=len(y):
    print(colored(y[i],'cyan'))
    bloom_level += int(y[i])
    i = i + 4 
    n += 1
print(colored("_" * 100,'white'))
print(colored("There are ",'green'),colored(n,'green'),colored(' questions in the question paper','green'))
percentage = bloom_level/(n*6) * 100
print(colored(str(round(percentage))+'%','magenta'))
if percentage>=1 and percentage<=40:
    print(colored("The given question paper is easy",'green'))

elif percentage>= 41 and percentage<=72:
    print(colored("The given question paper is Medium",'yellow'))

elif percentage>=73 and percentage<=100:
    print(colored("The given question paper is Hard",'red'))