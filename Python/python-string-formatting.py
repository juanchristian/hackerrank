def print_formatted(number):
    pad_size = len(str(bin(number))[2:])
    
    for n in range(1, number + 1):
        n_dec = str(n)
        n_oct = str(oct(n))[2:]
        n_hex = str(str(hex(n))[2:]).upper()
        n_bin = str(bin(n))[2:]

        print(n_dec.rjust(pad_size), n_oct.rjust(pad_size), n_hex.rjust(pad_size), n_bin.rjust(pad_size))
