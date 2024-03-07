print("\033c")

set_1 = {"Toyota", "Daihatsu", "Honda"}
set_2 = set(("Toyota", "Daihatsu", "Honda"))

print("Tipe data set_1 adalah ", type(set_1))
print("Tipe data set_2 adalah ", type(set_2))
print("Data set_1: ", set_1)
print("Data set_2: ", set_2)

for x in set_1:
  print(x)
print("-----------------------------------------------------")

print(len(set_1))

if "Daihatsu" in set_1:
 print("Yes, 'Daihatsu is an item in set_1.")

 set_1.add("Mitsubishi")
print(set_1)

set_1.update(["Suzuki", "Mazda", "Nissan"])
print(set_1)

set_1.remove("Honda")
print(set_1)

set_1.discard("Mazda")
print(set_1)

set_1.pop()
print(set_1)

del set_1
print("------------------------------------------")

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
print("-----------------------------------------")

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)






