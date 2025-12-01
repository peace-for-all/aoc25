with open("input_d1t1", "r") as f:
    pos = 50
    pass_zero_cnt = 0

    for line in f:
        line = line.strip()
        direction = line[0]
        shift = int(line[1:])
        # pos = (pos + shift) % 100
        if direction == "R":
            pos = (pos + shift) % 100
        if direction == "L":
            pos = (pos - shift) % 100

        if pos == 0:
            pass_zero_cnt += 1

        print("Processed:", line, "new pos:", pos)

print(pass_zero_cnt)