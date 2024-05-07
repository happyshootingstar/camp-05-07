# n 個の整数が並んでいます。 i 番目の整数は a(i) で表します。
# これらの数がすべて互いに異なるかどうか判定してください。
n = int(input())
n_list=list(map(int, input().split(" ")))
my_set=set(n_list)
if n == len(my_set):
    print("YES")
else:
    print("NO")
