with open("input_d1t1", "r") as f:
    pos = 50
    pass_zero_cnt = 0

    for line in f:
        line = line.strip()
        direction = line[0]
        shift = int(line[1:])

        print("Got instruction: ", shift, " moves to the ", direction)
        if direction == "R":
            pos_diff = pos + shift
            new_pos = (pos_diff) % 100
            pass_zero_local = (pos + shift) // 100
            print("Pass zero local: ", pass_zero_local)
        if direction == "L":
            pos_diff = pos - shift
            new_pos = (pos_diff) % 100
            pass_zero_local = abs(pos + shift) // 100
            print("Pass zero local: ", pass_zero_local)

        if direction == "L" and pass_zero_local == 1:
            print("pos: ", pos, "instruction: ", shift, " moves to the ", direction, " result: ", pass_zero_local)
        pass_zero_cnt += pass_zero_local
        # if new_pos == 0:
        #     pass_zero_cnt += 1

        pos = new_pos
        print("Processed:", line, "new pos:", new_pos, " global zero passes:", pass_zero_cnt)

print(pass_zero_cnt)