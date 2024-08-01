poets_dict = {}

with open('F:\\IranianPoets.txt', 'r') as f:
    f_lines= f.readlines()
    if len(f_lines) < 10 or len(f_lines) > 1000:
            print("The number of lines should be between 10 and 1000 lines!")
            exit()
    f.seek(0)
    for line in f:
        line = line.strip()
        parts = line.split()
        if parts[0].isdigit():
            birth_year = parts[0]
            name = " ".join(parts[1:])
        else:
            name = " ".join(parts[:-1])
            birth_year = parts[-1]
            
        poets_dict[name] = birth_year

        

sorted_poets = sorted(poets_dict.items(), key=lambda item: item[0])

sorted_poets.reverse()

with open('F:\\HW4-Output.txt', 'w') as f:
    for name, birth_year in sorted_poets:
        f.write(f"{name} {birth_year}\n")


