import re

filename = "passports.txt"

required_items = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    
valid_passports = []
all_passports = []

def check_byr(byr):
    byr = int(byr)
    return (byr >= 1920 and byr <= 2002)

def check_iyr(iyr):
    iyr = int(iyr)
    return (iyr >= 2010 and iyr <= 2020)

def check_eyr(eyr):
    eyr = int(eyr)
    return (eyr >= 2020 and eyr <= 2030)

def check_hgt(hgt):
    if "cm" in hgt:
        h = int(hgt.split("cm")[0])
        return (h>=150 and h<=193)
    elif "in" in hgt:
        h = int(hgt.split("in")[0])
        return (h>=59 and h<=76)
    else:
        return False

def check_hcl(hcl):
    return (not not re.match(r"^#\w{6}$", hcl))

def check_ecl(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def check_pid(pid):
    return (len(pid) == 9 and isinstance(int(pid), int))

def check_if_valid(passport_dict):
    has_required_keys = set(required_items).issubset(set(list(passport_dict.keys()))) #check if passport has all required keys
    if (has_required_keys):
        pd = passport_dict
        return (
            check_byr(pd["byr"])
            and check_iyr(pd["iyr"])
            and check_eyr(pd["eyr"])
            and check_hgt(pd["hgt"])
            and check_hcl(pd["hcl"])
            and check_ecl(pd["ecl"])
            and check_pid(pd["pid"])
        )
    else:
        return False

with open(filename) as f:
    lines = f.read().split("\n\n")

for l in lines:
    data = " ".join(l.split("\n")).split()
    pass_dict = {}
    for d in data:
        pair = d.split(":")
        pass_dict[pair[0]] = pair[1]
    keys = list(pass_dict.keys())
    if (check_if_valid(pass_dict)):
        valid_passports.append(pass_dict)

print("Number of valid passports: %d" %len(valid_passports))