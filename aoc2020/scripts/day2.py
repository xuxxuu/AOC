from pathlib import Path

tests_dir = Path(__file__).absolute().parent.parent / Path("tests/")
input_dir = Path(__file__).absolute().parent.parent / Path("inputs/")

with open(input_dir / "2.txt") as f:
    data = f.read().strip().split("\n")

part1_total = 0
part2_total = 0

def is_valid(minimum, maximum, target, password):
    if any(minimum <= password.count(target) <= maximum for letter in password):
        return True
    return False


for line in data:
    policy_str, password = line.split(": ")
    minimum, maximum = map(int, policy_str.split(" ")[0].split("-"))
    target = policy_str.split(" ")[1]
    if is_valid(minimum, maximum, target, password):
        part1_total += 1
    if password[minimum-1] == target and not password[maximum-1] == target:
        part2_total += 1
    elif password[maximum-1] == target and not password[minimum-1] == target:
        part2_total += 1

print(f"{part1_total} valid passwords for part 1")
print(f"{part2_total} valid passwords for part 2")


# idiotic solution for p1 for the memes
# p1 = sum([
#     is_valid(
#         int(line.split(": ")[0].split(" ")[0].split("-")[0]),
#         int(line.split(": ")[0].split(" ")[0].split("-")[1]),
#         line.split(": ")[0].split(" ")[1],
#         line.split(": ")[1]
#              )
#     for line in data
#     ])
# print(p1)