highest = max(seats := {int(line.translate(str.maketrans('FBLR', '0101')), 2) for line in open("input.txt")})
print(f"part 1: {highest}")
print(f"part 2: {max({*range(highest)} - seats)}")