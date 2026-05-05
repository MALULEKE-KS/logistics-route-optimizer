# Quick verification without animation
import heapq

graph = {
    "Disaneng": ["Mahikeng", "Madibogo"],
    "Mahikeng": ["Disaneng", "Mmabatho", "Slurry", "Bakerville", "Madibogo"],
    "Mmabatho": ["Mahikeng", "Slurry"],
    "Slurry": ["Mahikeng", "Mmabatho", "Zeerust", "Groot Marico", "Bakerville"],
    "Zeerust": ["Slurry", "Groot Marico"],
    "Groot Marico": ["Slurry", "Zeerust"],
    "Bakerville": ["Mahikeng", "Slurry", "Lichtenburg"],
    "Lichtenburg": ["Bakerville", "Coligny"],
    "Coligny": ["Lichtenburg", "Ottosdal"],
    "Ottosdal": ["Coligny", "Sannieshof"],
    "Sannieshof": ["Ottosdal", "Delareyville", "Madibogo"],
    "Delareyville": ["Sannieshof"],
    "Madibogo": ["Disaneng", "Mahikeng", "Sannieshof"]
}

weights = {
    ("Disaneng", "Mahikeng"): 25,
    ("Disaneng", "Madibogo"): 35,
    ("Mahikeng", "Mmabatho"): 10,
    ("Mahikeng", "Slurry"): 20,
    ("Mahikeng", "Bakerville"): 35,
    ("Mahikeng", "Madibogo"): 30,
    ("Mmabatho", "Slurry"): 15,
    ("Slurry", "Zeerust"): 35,
    ("Slurry", "Groot Marico"): 40,
    ("Slurry", "Bakerville"): 25,
    ("Zeerust", "Groot Marico"): 20,
    ("Bakerville", "Lichtenburg"): 20,
    ("Lichtenburg", "Coligny"): 30,
    ("Coligny", "Ottosdal"): 35,
    ("Ottosdal", "Sannieshof"): 25,
    ("Sannieshof", "Delareyville"): 30,
    ("Madibogo", "Sannieshof"): 35
}

heuristic = {
    "Disaneng": 70,
    "Mahikeng": 50,
    "Mmabatho": 55,
    "Slurry": 45,
    "Zeerust": 65,
    "Groot Marico": 75,
    "Bakerville": 30,
    "Lichtenburg": 20,
    "Coligny": 0,
    "Ottosdal": 25,
    "Sannieshof": 40,
    "Delareyville": 55,
    "Madibogo": 60
}

# Manual path calculation
path = ["Disaneng", "Mahikeng", "Bakerville", "Lichtenburg", "Coligny"]
total = 0
for i in range(len(path)-1):
    a, b = path[i], path[i+1]
    if (a,b) in weights:
        dist = weights[(a,b)]
    else:
        dist = weights[(b,a)]
    print(f"{a} → {b}: {dist} km")
    total += dist

print(f"\nTotal Distance: {total} km")
print(f"Expected:      110 km")
print(f"Match: {'✅ YES' if total == 110 else '❌ NO'}")