import csv

def clean_file(input_path, output_path, fields):
    seen = set()
    with open(input_path) as f, open(output_path, "w", newline="") as out:
        reader = csv.DictReader(f)
        writer = csv.DictWriter(out, fieldnames=fields)
        writer.writeheader()

        for row in reader:
            key = tuple(v.strip().title() for v in row.values())
            if key not in seen:
                seen.add(key)
                writer.writerow(dict(zip(fields, key)))