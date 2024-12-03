with open("input.txt", "r") as file:
    lines = file.readlines()

reports = []
for line in lines:
    a = line.strip().split()
    a = [int(item) for item in a]
    reports.append(a)


def is_safe(report):
    is_increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))

    if not (is_increasing or is_decreasing):
        return False

    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 3:
            return False
    return True


def is_safe_with_dampener(report):
    if is_safe(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True

    return False


safe_reports = [report for report in reports if is_safe(report)]
safe_reports_with_dampener = [report for report in reports if is_safe_with_dampener(report)]

print(f"Number of safe reports              : {len(safe_reports)}")
print(f"Number of safe reports with dampener: {len(safe_reports_with_dampener)}")
