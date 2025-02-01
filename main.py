import sys

def remove_duplicates(input_file):
    seen = set()
    output_file = f"modified-{input_file}"
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if line not in seen:
                outfile.write(line)
                seen.add(line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <filename>")
    else:
        input_file = sys.argv[1]
        remove_duplicates(input_file)
        print(f"Finished! Saved as modified-{input_file}")