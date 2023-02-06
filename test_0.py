import json

def count_objects(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    count_ce = 0
    count_wa = 0
    for obj in data:
        if obj.get("source") == "Contract Explorer":
            count_ce += 1
        elif obj.get("source") == "Watson assistant":
            count_wa += 1
    return (count_ce, count_wa)

file_path = 'file.txt'
count_ce, count_wa = count_objects(file_path)
print("Number of objects with source 'Contract Explorer':", count_ce)
print("Number of objects with source 'Watson assistant':", count_wa)