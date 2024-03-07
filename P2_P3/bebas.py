import matplotlib.pyplot as plt
import numpy as np

col, row = 1200, 1200
print("col, row =", col, ", ", row)

def buat_garis(Gambar, y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    hd = int(pd / 2)
    hw = int(lw / 2)
    dy = y2 - y1
    dx = x2 - x1

    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if (i - x1) * 2 + (j - y1) * 2 < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if (i - x2) * 2 + (j - y2) * 2 < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    if dx == 0:  # Check for vertical line
        for yi in range(min(y1, y2), max(y1, y2)):
            x = x1
            y = yi
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if (i - x) * 2 + (j - y) * 2 < hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb
    else:
        my = dy / dx
        for xi in range(min(x1, x2), max(x1, x2)):
            y = int(my * (xi - x1) + y1)
            x = xi
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if (i - x) * 2 + (j - y) * 2 < hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb

# Inisialisasi gambar
Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)

# Menggambar huruf "G" dengan fungsi yang telah dibuat
buat_garis(Gambar, 200, 100, 1000, 100, 8, 8, 255, 255, 0, 255, 255, 0)
buat_garis(Gambar, 1000, 100, 1000, 400, 8, 8, 255, 255, 0, 255, 255, 0)
buat_garis(Gambar, 1000, 400, 600, 400, 8, 8, 255, 255, 0, 255, 255, 0)
buat_garis(Gambar, 600, 400, 600, 200, 8, 8, 255, 255, 0, 255, 255, 0)

# Menambah garis horizontal di bagian atas huruf "G" (pendekin jadi 400)
buat_garis(Gambar, 200, 100, 200, 500, 8, 8, 255, 255, 0, 255, 255, 0)

# Menampilkan gambar huruf "G"
plt.figure()
plt.imshow(Gambar)
plt.show()
