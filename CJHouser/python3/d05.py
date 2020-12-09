import boiler

# Bucket or radix sort sounds good for day 5. Didn't realize this
# until after finishing part 1. Oops.

def part1(bpasses):
    bpasses = narrow(bpasses, 0, 7)
    bpasses = narrow(bpasses, 7, 10)
    maximum = 0
    for bpass in bpasses:
        row = calculate(bpass, 0, 7)
        col = calculate(bpass, 7, 10)
        maximum = max(maximum, row * 8 + col)
    return maximum

def part2(bpasses, last_seat_id, start, end):
    seat_count = (2**start) * (2**(end-start))
    remainder = seat_count - last_seat_id
    first_seat_id = seat_count - len(bpasses) - remainder
    # pretty sure there is a mathematical way to solve this
    # possibly using pigeon hole principal or something like that.
    # My idea is to count the number of boarding passes that have
    # a similar column ("RRR", "RRL", etc) and check to see which
    # column has a missing passenger. The problem says that some rows
    # in the front and back are missing. The three lines at the
    # start of this function define the boundaries of existing
    # seat IDs. With that, we can figure out how many seats are supposed
    # to be missing from each column due to missing rows in the front
    # and back. Once the column with missing boarding pass is found,
    # it should be trivial to find the missing seat.

def part2brute(bpasses):
    seat_ids = []
    for bpass in bpasses:
        row = calculate(bpass, 0, 7)
        col = calculate(bpass, 7, 10)
        seat_ids.append(row * 8 + col)
    i = min(seat_ids)
    while i in seat_ids:
        i += 1
    return i

def calculate(bpass, start, end):
    lo, hi = 0, (2 ** (end - start)) - 1
    for pos in range(start, end):
        if bpass[pos] in ("B", "R"):
            lo += (hi - lo) // 2 + 1
        else:
            hi -= (hi - lo) // 2 + 1
    return lo

def narrow(bpasses, start, end):
    for pos in range(start, end):
        finalists = []
        for bpass in bpasses:
            if bpass[pos] in ("B", "R"):
                finalists.append(bpass)
        if finalists:
            bpasses = finalists
    return bpasses

if __name__ == "__main__":
    bpasses = boiler.getLines("d05")
    p1 = part1(bpasses)
    print("Part 1:", p1)
    #p2 = part2(bpasses, p1, 7, 10)
    p2 = part2brute(bpasses)
    print("Part 2:", p2)
