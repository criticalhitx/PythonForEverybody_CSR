#Count these lines and extract the floating point values from each of the lines and compute the average of those
#  values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    
    line=line.rstrip()
    dotpos=line.find(':')
    line= line[dotpos+1:]
    line= float(line)
    count = count + 1 
    total = total + line
    
print("Average spam confidence:",total/count )