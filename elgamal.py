import random
from tabulate import tabulate  # Import tabulate untuk tabel ASCII

# Parameter kunci publik
p = 2579
alpha = 2
beta = 949

# Fungsi untuk menghitung perpangkatan modular dengan format tampilan yang sesuai
def mod_exp_verbose(base, exp, mod):
    steps = []
    intermediate_values = {1: base % mod}

    # Langkah awal (pangkat 1)
    steps.append(f"{base}^1 mod {mod} = {intermediate_values[1]}")

    # Hitung kelipatan pangkat 2 (2, 4, 8, 16, ...)
    power = 2
    while power <= exp:
        prev = intermediate_values[power // 2]
        intermediate_values[power] = (prev * prev) % mod
        steps.append(f"{base}^{power} mod {mod} = [{base}^{power//2} mod {mod}] . [{base}^{power//2} mod {mod}] mod {mod}")
        steps.append(f"= [{prev}] . [{prev}] mod {mod}")
        steps.append(f"= {prev * prev} mod {mod}")
        steps.append(f"= {intermediate_values[power]}")
        power *= 2

    # Jika exp tidak ditemukan langsung di dictionary, cari kombinasi pangkat
    if exp not in intermediate_values:
        bin_exp = bin(exp)[2:]  # Konversi ke biner
        exp_parts = sorted([2**i for i in range(len(bin_exp)) if bin_exp[-(i+1)] == '1'], reverse=True)

        result = 1
        steps.append(f"\nMenghitung {base}^{exp} mod {mod} dari kombinasi:")

        for i, part in enumerate(exp_parts):
            if i == 0:
                result = intermediate_values[part]
            else:
                steps.append(f"{base}^{exp} mod {mod} = [{base}^{exp_parts[i-1]} mod {mod}] . [{base}^{part} mod {mod}] mod {mod}")
                steps.append(f"= [{result}] . [{intermediate_values[part]}] mod {mod}")
                result = (result * intermediate_values[part]) % mod
                steps.append(f"= {result} mod {mod}")
        
        intermediate_values[exp] = result

    steps.append(f"\nDitemukan nilai = {intermediate_values[exp]}")
    return intermediate_values[exp], steps

# Fungsi enkripsi dengan algoritma El Gamal
def elgamal_encrypt(message, p, alpha, beta):
    encrypted_pairs = []
    output_text = ""

    # Membuat tabel ASCII
    table_data = [["i", "Karakter", "Plainteks mi", "ASCII"]]

    for i, char in enumerate(message):
        m = ord(char)  # Konversi karakter ke ASCII
        k = random.choice([x for x in range(10, 100, 2)])  # Pilih nilai k (2 digit & kelipatan 2)

        table_data.append([i + 1, char, f"m_{i+1}", m])

        output_text += f"\nm{i+1} = {m}\n"
        output_text += f"k{i+1} = {k}\n"

        # Hitung gamma = α^k mod p
        gamma, gamma_steps = mod_exp_verbose(alpha, k, p)
        output_text += f"γ{i+1} = {alpha}^{k} mod {p}\n"
        output_text += "\n".join(gamma_steps) + "\n"
        output_text += f"Ditemukan nilai ɣ{i+1} = {gamma}\n\n"

        # Hitung delta = β^k mod p
        delta_base, delta_steps = mod_exp_verbose(beta, k, p)
        output_text += f"δ = {beta}^{k} mod {p}\n"
        output_text += "\n".join(delta_steps) + "\n"
        output_text += f"Ditemukan nilai δ = {delta_base}\n\n"

        # Hitung δi = (β^k * m) mod p
        delta = (delta_base * m) % p
        output_text += f"Menghitung rumus δ{i+1} = {beta}^{k} . m{i+1} mod {p}\n"
        output_text += f"δ{i+1} = [{delta_base}] . [{m}] mod {p}\n"
        output_text += f"= {delta_base * m} mod {p}\n"
        output_text += f"= {delta}\n"
        output_text += f"Ditemukan nilai δ{i+1} = {delta}\n\n"

        encrypted_pairs.append((gamma, delta))

        # Format output
        output_text += f"Hasil enkripsi m{i+1} = {m} dengan k{i+1} = {k} adalah = ({gamma}, {delta})\n"

    # Menambahkan tabel ASCII ke dalam output
    output_text = "Tabel ASCII:\n" + tabulate(table_data, headers="firstrow", tablefmt="grid") + "\n\n" + output_text

    return encrypted_pairs, output_text

# Fungsi untuk menyimpan hasil enkripsi ke dalam file
def save_to_file(filename, output_text):
    with open(filename, 'w') as f:
        f.write(output_text)

# Main program
if __name__ == "__main__":
    message = input("Masukkan pesan yang ingin dienkripsi: ")
    encrypted_data, output_text = elgamal_encrypt(message, p, alpha, beta)

    # Simpan hasil ke file
    output_filename = "encrypted_message.txt"
    save_to_file(output_filename, output_text)
    print(f"\nHasil enkripsi berhasil disimpan ke dalam file {output_filename}")