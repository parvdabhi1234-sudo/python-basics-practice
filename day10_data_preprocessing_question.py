# ===== Practice Questions =====

# Q1 Remove negative numbers

nums = [5, -3, 8, -1, 10]
positive = []

for n in nums:
    if n >= 0:
        positive.append(n)

print("Q1 Output:", positive)

# Q2 Convert string list to int list

s = ["1","2","3","4"]
int_list = []

for i in s:
    int_list.append(int(i))

print("Q2 Output:", int_list)

# Q3 Find average

vals = [10,20,30,40]
avg = sum(vals)/len(vals)

print("Q3 Average:", avg)

print("\n--- Practice End ---")
