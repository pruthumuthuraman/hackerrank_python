n = int(input())
list1 = list(map(int, input().split()))
num_ops = int(input())
h = set(list1)

for i in range(num_ops):
    operation_info = input().split()
    op_name = operation_info[0]
    
    list2 = list(map(int, input().split()))
    b = set(list2)
    
    if op_name == "intersection_update":
        h.intersection_update(b)
    elif op_name == "update":
        h.update(b)
    elif op_name == "symmetric_difference_update":
        h.symmetric_difference_update(b)
    elif op_name == "difference_update":
        h.difference_update(b)

print(sum(h))
