a = []

with open('2024/2/input.txt', 'r') as f:
    for line in f.readlines():
        report = []
        for char in line.split():
            report.append(int(char))
        a.append(report)

safeReports = 0
for report in a:
    safe = False
    increasing = 0 # 1 is increasing, -1 is decreasing
    last = None
    for level in report:
        if last == None:
            last = level
            continue
    if safe:
        safeReports += 1

print(safeReports)
