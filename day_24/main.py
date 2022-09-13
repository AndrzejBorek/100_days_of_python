with open("./input/names.txt") as f:
    names = f.readlines()
    names = [name.rstrip() for name in names]
    for name in names:
        with open("./input/letter_pattern.txt") as pattern:
            letter = pattern.read().replace('[name]', name)
            with open(f"./output/letter_to_{name}.txt", "w") as o:
                o.write(letter)
