data = {}

with open("LaLiga.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

lines = lines[1:]

for line in lines:
    parts = line.split("\t")

    if len(parts) < 10:
        continue # skip free lines

    team = parts[1].strip()
    data[team] = {
        "Pl": int(parts[2]),
        "W": int(parts[3]),
        "D": int(parts[4]),
        "L": int(parts[5]),
        "F": int(parts[6]),
        "A": int(parts[7]),
        "GD": int(parts[8]),
        "Pts": int(parts[9]),
    }
def my_item(item):
    return item[1]['F']
print(data)
# bishtarin goal zade
top_team = max(data.items(), key=my_item)
print(f"bishtarin goal zade: {top_team[0]} ba {top_team[1]['F']} goal")
# kamtarin goal khorde 
top_team = min(data.items(), key=lambda item: item[1]["A"])
print(f"kamtarin goal khorde: {top_team[0]} ba {top_team[1]['A']} goal")
# behtarin ekhtelaf
top_team = max(data.items(), key=lambda item: item[1]["GD"])
print(f"behtarin ekhtelaf: {top_team[0]} ba {top_team[1]['GD']} goal")
# badtarin ekhtelaf
top_team = min(data.items(), key=lambda item: item[1]["GD"])
print(f"badtarin ekhtelaf: {top_team[0]} ba {top_team[1]['GD']} goal")
# bishtarin goal khorde
top_team = max(data.items(), key=lambda item: item[1]["A"])
print(f"bishtarin goal khorde: {top_team[0]} ba {top_team[1]['A']} goal")
# kamtarin goal zade
top_team = min(data.items(), key=lambda item: item[1]["F"])
print(f"kamtarin goal zade: {top_team[0]} ba {top_team[1]['F']} goal")
# bishtarin mosavi
top_team = max(data.items(), key=lambda item: item[1]["D"])
print(f"bishtarin mosavi: {top_team[0]} ba {top_team[1]['D']} goal")
# kamtarin mosavi
top_team = min(data.items(), key=lambda item: item[1]["D"])
print(f"kamtarin mosavi: {top_team[0]} ba {top_team[1]['D']} goal")
