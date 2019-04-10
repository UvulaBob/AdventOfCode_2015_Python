with open("input.txt") as f:
    instructions = f.readlines()

wires = {}

for instruction in instructions:
    instruction = instruction.rstrip()
    split_instruction = instruction.split(" -> ")
    wires[split_instruction[1]] = split_instruction[0]

wires['b'] = '16076'


def find_value_of_wire(wire):
    try:
        return int(wire)
    except ValueError:
        result = do_instruction(wires[wire])
        wires[wire] = str(result)
        return result


def do_instruction(instruction_to_do):
    split_instruction_to_do = instruction_to_do.split(" ")
    split_instruction_length = len(split_instruction_to_do)

    if split_instruction_length == 1:
        return find_value_of_wire(split_instruction_to_do[0])

    if split_instruction_length == 2:
        try:
            return ~int(split_instruction_to_do[1]) & 65535
        except ValueError:
            return ~int(find_value_of_wire(split_instruction_to_do[1])) & 65535

    operation = split_instruction_to_do[1]
    first_value = find_value_of_wire(split_instruction_to_do[0])
    second_value = find_value_of_wire(split_instruction_to_do[2])

    if operation == "AND":
        return first_value & second_value
    if operation == "OR":
        return first_value | second_value
    if operation == "LSHIFT":
        return first_value << second_value

    return first_value >> second_value


print(find_value_of_wire("a"))
print("Done!")
