def binary_diagnostic(data):
    num_data = len(data)
    one_freq = [0] * len(data[0])

    for binary in data:
        for i, bit in enumerate(binary):
            one_freq[i] += int(bit)
    
    gamma_rate = []
    epsilon_rate = []

    for freq in one_freq: 
        if freq/num_data > 0.5:
            gamma_rate.append("1")
            epsilon_rate.append("0")
        elif freq/num_data < 0.5:
            gamma_rate.append("0")
            epsilon_rate.append("1")
        else:
            gamma_rate.append("1")
            epsilon_rate.append("0")

    gamma_rate = int(''.join(gamma_rate), 2)
    epsilon_rate = int(''.join(epsilon_rate), 2)

    return (gamma_rate, epsilon_rate)

# 3046463 is too low
def binary_diagnostic2(data, length):

    ogr = data.copy()

    bit_index = 0
    while len(ogr) > 1:
        ogr_bit_criteria, _ = binary_diagnostic(ogr)
        ogr_bit_criteria = str(bin(ogr_bit_criteria))[2:].zfill(length)

        bit = ogr_bit_criteria[bit_index]

        index = 0
        while len(ogr) > 1 and index < len(ogr):
            if ogr[index][bit_index] != bit:
                ogr.pop(index)
            else:
                index += 1
        
        bit_index += 1
    
    bit_index = 0
    csr = data.copy()
    while len(csr) > 1:
        _, csr_bit_criteria = binary_diagnostic(csr)
        csr_bit_criteria = str(bin(csr_bit_criteria))[2:].zfill(length)

        bit = csr_bit_criteria[bit_index]

        index = 0
        while len(csr) > 1 and index < len(csr):
            if csr[index][bit_index] != bit:
                csr.pop(index)
            else:
                index += 1
        
        bit_index += 1
    
    return int(ogr[0], 2) * int(csr[0], 2)




if __name__ == "__main__":
    print("Day 3 and I am Contemplating life")

    input_file = "day_3.txt"

    f = open(input_file,'r',encoding = 'utf-8')

    data = []

    for row in f:
        data.append(row[:-1])

    gamma_rate, epsilon_rate = binary_diagnostic(data)
    power_consumption = gamma_rate * epsilon_rate
    print(power_consumption)

    ogr_bit_criteria = gamma_rate
    csr_bit_criteria = epsilon_rate

    result = binary_diagnostic2(data, 12)
    print(result)
    