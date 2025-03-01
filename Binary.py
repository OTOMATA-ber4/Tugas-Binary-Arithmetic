def is_valid_bit_sequence(bits, valid_set, memo={}):
    if bits == "":
        return True  # Jika sudah kosong, berarti valid
    
    if bits in memo:
        return memo[bits]
    
    for s in valid_set:
        if bits.startswith(s):  # Jika prefix cocok dengan elemen di S
            if is_valid_bit_sequence(bits[len(s):], valid_set, memo):
                memo[bits] = True
                return True
    
    memo[bits] = False
    return False

# Himpunan S yang diberikan
S = {"00", "10", "010", "01001"}

# Contoh penggunaan
binary_input = "0100100100100101000"
if is_valid_bit_sequence(binary_input, S):
    print("Bit valid")
else:
    print("Bit tidak valid")