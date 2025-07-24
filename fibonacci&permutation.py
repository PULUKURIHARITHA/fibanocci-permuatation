def binary(n,b=' '):
    if n==0:
        print(b)
        return
    binary(n-1,b+'0')
    binary(n-1,b+'1')
    length=int(input("Enter length of string:"))
    print("Binary combination........")
    binary(length)

O/P:-
enter length of string:4
binary combination...........
0000
0001
0010
0011
0100
0101
0110
0111
1000
1001
1010
1011
1100
1101
1110
1111
