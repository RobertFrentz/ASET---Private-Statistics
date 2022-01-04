import pathlib


def read_paillier_setup():
    current_path = pathlib.Path(__file__).parent / 'setup'
    file = open(current_path, 'r')
    line = file.readline()
    line_values = line.split(' ')
    n = int(line_values[0])
    g = int(line_values[1])
    random_seed = int(line_values[2])
    s = int(line_values[3])
    shares = [int(x) for x in line_values[4][1:-1].split(',')]
    delta_patrat = int(line_values[5])
    return n, g, random_seed, s, shares, delta_patrat


print(read_paillier_setup())
