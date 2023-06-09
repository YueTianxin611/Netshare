import random
import csv
import pandas as pd

def generate_random_ipv4_address():
    ip_components = [str(random.randint(0, 255)) for _ in range(4)]
    ipv4_address = ''.join(ip_components)
    return ipv4_address

def generate_random_ipv4_csv():
    deidentified_mapping = {}
    with open('flow.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)

        for row in rows[1:]:
            for i in [2,4]:
                deidentify_ip = row[i]
                if deidentify_ip not in deidentified_mapping:
                    random_ip = generate_random_ipv4_address()
                    deidentified_mapping[deidentify_ip] = random_ip

                row[i] = deidentified_mapping[deidentify_ip]

    with open('processed_flow.csv', 'w', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(rows)
    return None

def generate_random_port():
    return random.randint(1024, 65535)

def generate_random_port_csv():
    deidentified_mapping = {}
    with open('processed_flow.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)

        for row in rows[1:]:
            for i in [3,5]:
                if row[i].startswith('N'):
                    deidentify_port = row[i]
                    if deidentify_port not in deidentified_mapping:
                        random_port = generate_random_port()
                        deidentified_mapping[deidentify_port] = random_port

                    row[i] = deidentified_mapping[deidentify_port]

    with open('processed_flow.csv', 'w', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(rows)
    return None

#generate_random_ipv4_csv()
#generate_random_port_csv()
protocols = {'1': 'ICMP', '6':'TCP', '17':'UDP'}
def assign_protocol_csv():
    with open('processed_flow.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)
        for row in rows[1:]:
            row[6] = protocols[row[6]]
    with open('processed_flow.csv', 'w', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(rows)
    return None

def add_type_csv():
    with open('flows.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        rows = list(csvreader)

    rows[0].append('type')
    
    for row in rows[1:]:
        row.append('backgorund')

    with open('flows.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(rows)
