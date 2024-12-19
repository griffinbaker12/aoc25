import time
import re

reg = {r: 0 for r in ("A", "B", "C")}
combo_operands = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: lambda x: x["A"],
    5: lambda x: x["B"],
    6: lambda x: x["C"],
    7: 1,
}


def init_registers(chunk):
    for r, v in zip(("A", "B", "C"), chunk.splitlines()):
        reg[r] = int(re.findall(r"\d+", v)[0])


def get_combo_operand(reg, operand):
    if 0 <= operand <= 3:
        return combo_operands[operand]
    else:
        return combo_operands[operand](reg)


def process_instructions(reg, instructions):
    outputs = []
    ip = 0
    while ip < len(instructions) - 1:
        opcode = instructions[ip]
        operand = instructions[ip + 1]
        if opcode == 0:
            num = reg["A"]
            den = 2 ** get_combo_operand(reg, operand)
            reg["A"] = int(num / den)
            ip += 2
        elif opcode == 1:
            reg["B"] ^= operand
            ip += 2
        elif opcode == 2:
            reg["B"] = get_combo_operand(reg, operand) % 8
            ip += 2
        elif opcode == 3:
            if reg["A"] != 0:
                ip = operand
            else:
                ip += 2
        elif opcode == 4:
            reg["B"] = reg["B"] ^ reg["C"]
            ip += 2
        elif opcode == 5:
            out = get_combo_operand(reg, operand) % 8
            outputs.append(str(out))
            ip += 2
        elif opcode == 6:
            num = reg["A"]
            den = 2 ** get_combo_operand(reg, operand)
            reg["B"] = int(num / den)
            ip += 2
        elif opcode == 7:
            num = reg["A"]
            den = 2 ** get_combo_operand(reg, operand)
            reg["C"] = int(num / den)
            ip += 2
    return ",".join(outputs)


with open("input.txt") as f:
    top, bottom = f.read().split("\n\n")
    init_registers(top)
    A = 1
    OG_B, OG_C = reg["B"], reg["C"]
    to_match = ",".join(map(str, map(int, bottom.split(": ")[1].strip().split(","))))
    instructions = list(map(int, to_match.split(",")))

    print(f"Target string: {to_match}")
    print(f"Instructions: {instructions}")

    start = time.time()
    while True:
        reg["A"] = A
        reg["B"] = OG_B
        reg["C"] = OG_C

        output = process_instructions(reg, instructions)

        # if A == 117440:
        #     print(output, len(output), to_match, len(to_match))

        if output == to_match:
            reg["A"] = A
            break

        A += 1

    print(f"Took {time.time() - start}:.3f to complete...")
    print(f"Final A: {reg['A']}")
