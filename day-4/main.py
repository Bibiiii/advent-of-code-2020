filename = "passports.txt"

required_items = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    
valid_passports = []

with open(filename) as f:
    lines = f.read().split("\n\n")
    passports = []
    for p in lines:
        data = p.split("\n")
        data = " ".join(data)
        data = data.split()
        passDict = {}
        for d in data:
            pair = d.split(":")
            passDict[pair[0]] = pair[1]
        keys = list(passDict.keys())
        print(keys, sorted(required_items) == sorted(keys))
        if (set(required_items).issubset(set(keys))):
            valid_passports.append(passDict)

print(len(valid_passports))