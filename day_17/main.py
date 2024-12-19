import re

reg = {r: 0 for r in ("A", "B", "C")}
combo_operands = {0: 0, 1: 1, 2: 2, 3: 3, 4: lambda x: x["A"], 5: lambda x: x["B"], 6: lambda x: x["C"], 7: 1}


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
            reg["A"] = int(reg["A"] >> get_combo_operand(reg, operand))
        elif opcode == 1:
            reg["B"] ^= operand
        elif opcode == 2:
            reg["B"] = get_combo_operand(reg, operand) % 8
        elif opcode == 3:
            if reg["A"] != 0:
                ip = operand
                continue
        elif opcode == 4:
            reg["B"] = reg["B"] ^ reg["C"]
        elif opcode == 5:
            out = get_combo_operand(reg, operand) % 8
            outputs.append(str(out))
        elif opcode == 6:
            reg["B"] = int(reg["A"] >> get_combo_operand(reg, operand))
        elif opcode == 7:
            continue
            # reg["C"] = int(reg["A"] >> get_combo_operand(reg, operand))
        ip += 2

    return ",".join(outputs)


with open("input.txt") as f:
    top, bottom = f.read().split("\n\n")
    init_registers(top)
    to_match = ",".join(map(str, map(int, bottom.split(": ")[1].strip().split(","))))
    instructions = list(map(int, to_match.split(",")))

    print(f"Target string: {to_match}")
    print(f"Instructions: {instructions}")

    print(process_instructions(reg, list(map(int, bottom.split(": ")[1].split(",")))))
