#source: https://codeforces.com/blog/entry/83441#
import sys
import io,os
"""
Reading from judge's file directly
"""
input_data = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
input_data = input_data.decode()
# or input = sys.stdin.readline but for not too large input

"""
Writing to judge's file directly
"""
#single integer output: print(n)
sys.stdout.write(str(n) + "\n")
# list output: print(*list)
sys.stdout.write(" ".join(map(str,list)) + "\n")