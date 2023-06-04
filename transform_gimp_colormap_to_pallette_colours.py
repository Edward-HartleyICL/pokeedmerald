import argparse
import os

def hex_to_rgb(hex_value):
    hex_value = hex_value[1:]
    return tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))

def convert_file(input_file):
    output_file = os.path.splitext(input_file)[0] + '_pal.txt'
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            rgb = hex_to_rgb(line.strip())
            outfile.write(' '.join(map(str, rgb)) + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert hex colors to RGB.')
    parser.add_argument('input_file', type=str, help='Input file path')

    args = parser.parse_args()
    convert_file(args.input_file)