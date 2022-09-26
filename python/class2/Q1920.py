from sys import stdin, stdout
N=stdin.readline()
A=set(stdin.readline().split())
M=stdin.readline()
search=stdin.readline().split()
for s in search:
    if s in A:
        stdout.write('1\n')
    else:
        stdout.write('0\n')
