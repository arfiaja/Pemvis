# Case 1
set1 = {True, False}
print(set1)
print("====================================")

# Case 2
set2 = {3 > 2, 3 + 2 == 5, 3 > 2}
print(set2)
print("===================================")

# Case 3
Penghasilan = 20000000
PenghasilanTanpaPajak = 4000000
set3 = set()
if Penghasilan <= PenghasilanTanpaPajak:
    set3.add(0)
if Penghasilan > PenghasilanTanpaPajak:
    set3.add(0.1 * Penghasilan)
print("Pajak yang harus Anda bayar:", set3)

# Case 4
set4 = {3, "Ini data string.", ("laptop", "buku", "ballpen"), frozenset(("laptop", "buku", "ballpen")),
        frozenset(("laptop", "buku", "ballpen")), frozenset({1, 2, 3, 4, 5})}
print(set4)
print("==============================================")

# Case 5
set5 = {0, "", frozenset(), frozenset(), frozenset()}
print(set5)
print("==============================================")

# Case 6
class myclass():
    def __len__(self):
        return 0

set6 = {myclass()}
print(set6)
print("==============================================")