def print_state(lM, lC, rM, rC, direction):
    #Fungsi untuk mencetak kondisi saat ini
    print("\n")
    for _ in range(lM):
        print("M ", end="")
    for _ in range(lC):
        print("C ", end="")
    print(f"| {direction} | ", end="")
    for _ in range(rM):
        print("M ", end="")
    for _ in range(rC):
        print("C ", end="")
    print("\n")

def validate_input(uM, uC, lM, lC, rM, rC, direction):
    #Validasi input untuk memastikan pergerakan valid.
    if uM < 0 or uC < 0:
        return False
    if uM + uC == 0 or uM + uC > 2:
        return False
    if direction == "->" and (uM > lM or uC > lC):
        return False
    if direction == "<-" and (uM > rM or uC > rC):
        return False
    return True

def is_game_over(lM, lC, rM, rC):
    #Periksa apakah permainan berakhir karena misionaris dimakan.
    if (lC > lM > 0) or (rC > rM > 0):
        print("Kanibal memakan misionaris:\nAnda kalah")
        return True
    return False

def main():
    print("\n\tPermainan Dimulai\n")
    print("Tugas: Memindahkan semuanya ke sisi kanan sungai.")
    print("Aturan:")
    print("1. Perahu dapat mengangkut paling banyak dua orang.")
    print("2. Jika kanibal lebih banyak daripada misionaris di satu sisi, kanibal akan memakan misionaris.")
    print("3. Perahu tidak dapat menyeberang tanpa orang di dalamnya.\n")
    
    # Inisialisasi variabel
    lM, lC, rM, rC = 3, 3, 0, 0
    attempts = 0
    print_state(lM, lC, rM, rC, "---")
    
    while True:
        # Sisi kiri -> kanan
        while True:
            try:
                uM = int(input("Masukkan jumlah Misionaris untuk sisi kanan => "))
                uC = int(input("Masukkan jumlah Kanibal untuk sisi kanan => "))
                if validate_input(uM, uC, lM, lC, rM, rC, "->"):
                    break
                else:
                    print("Input salah, masukkan kembali.")
            except ValueError:
                print("Harap masukkan angka yang valid.")

        # Update kondisi
        lM -= uM
        lC -= uC
        rM += uM
        rC += uC
        attempts += 1
        print_state(lM, lC, rM, rC, "-->")
        
        if is_game_over(lM, lC, rM, rC):
            break
        if rM + rC == 6:
            print("Anda memenangkan permainan!\nSelamat!")
            print(f"Total upaya: {attempts}")
            break

        # Sisi kanan -> kiri
        while True:
            try:
                uM = int(input("Masukkan jumlah Misionaris untuk sisi kiri => "))
                uC = int(input("Masukkan jumlah Kanibal untuk sisi kiri => "))
                if validate_input(uM, uC, lM, lC, rM, rC, "<-"):
                    break
                else:
                    print("Input salah, masukkan kembali.")
            except ValueError:
                print("Harap masukkan angka yang valid.")

        # Update kondisi
        lM += uM
        lC += uC
        rM -= uM
        rC -= uC
        attempts += 1
        print_state(lM, lC, rM, rC, "<--")
        
        if is_game_over(lM, lC, rM, rC):
            break

if _name_ == "_main_":
    main()
