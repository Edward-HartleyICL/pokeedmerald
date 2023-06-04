import argparse
import os

def rgb_to_hex(rgb):
    return '#' + ''.join('{:02x}'.format(int(i)) for i in rgb)

def convert_file(input_file):
    output_file = os.path.splitext(input_file)[0] + '_hex.txt'
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            rgb = tuple(map(int, line.strip().split()))
            hex_color = rgb_to_hex(rgb)
            outfile.write(hex_color + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert RGB colors to hex.')
    parser.add_argument('input_file', type=str, help='Input file path')

    args = parser.parse_args()
    convert_file(args.input_file)