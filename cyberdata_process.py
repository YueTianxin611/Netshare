import random
import csv

def generate_random_ipv4_address():
    ip_components = [str(random.randint(0, 255)) for _ in range(4)]
    ipv4_address = '.'.join(ip_components)
    return ipv4_address

def generate_random_ipv4_csv():
    deidentified_mapping = {}
    with open('../datasets/flow.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)

        ip_columns = ['srcip', 'dstip']
        for row in rows:
            for c in ip_columns:
                deidentify_ip = row[c]
                if deidentify_ip not in deidentified_mapping:
                    random_ip = generate_random_ipv4_address()
                    deidentified_mapping[deidentify_ip] = random_ip

                row[c] = deidentified_mapping[deidentify_ip]

    with open('../datasets/processed_flow.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return None


generate_random_ipv4_csv()
with open('../datasets/processed_flow.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    row_count = 0
    for row in reader:
        print(row)
        row_count += 1
        if row_count >= 20:
            break