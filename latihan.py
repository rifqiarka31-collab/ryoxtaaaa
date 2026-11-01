
import time
import sys

def mengetik(teks, kecepatan=0.05):
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(kecepatan)
    print()

# Warna teks
pink = "\033[95m"
merah = "\033[91m"
reset = "\033[0m"

# Membersihkan tampilan terminal
print("\033[2J\033[H", end="")

# Tampilan hati
hati = [
    "  **     **  ",
    " ****   **** ",
    "****** ******",
    " *********** ",
    "  *********  ",
    "   *******   ",
    "    *****    ",
    "     ***     ",
    "      *      "
]

print(merah)

for baris in hati:
    print(baris)
    time.sleep(0.15)

print(reset)

time.sleep(0.5)

# Ucapan ulang tahun
mengetik(pink + "   HAPPY BIRTHDAY YANTIIIII 🎂" + reset, 0.1)
time.sleep(0.5)

mengetik("   Selamat ulang tahun yang ke 20 ")
time.sleep(0.5)

mengetik("   Semoga panjang umur,")
mengetik("   sehat selalu,")
mengetik("   semua impianmu tercapai,")
mengetik("   tugas tugas di permudah,")
mengetik("   rezekinyaa lancarrr,")
mengetik("   dan jugaa tidak garang lagii,")
mengetik("   wkwkwkwwkwkwkwkwk")
mengetik("   ohh iyaa jangan lupa yaa,")
mengetik("   kalo sekarang udah di kepala 2")
mengetik("   wkwkwkwwkwkwkwkwk")
mengetik("   pokoknyaa aku cuma minta")
mengetik("   kamu untukk selaluu merhatiin")
mengetik("   kesehatan kamu mau kayak manapu.")

time.sleep(0.5)

print(merah)
mengetik("   ❤️ LOVE YOU ❤️", 0.1)
print(reset)

