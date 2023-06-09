import gzip
import shutil
import csv
from collections import deque
column_names = ['ts', 'td', 'srcip', 'srcport', 'dstip', 'dstport', 'proto', 'pkt', 'byt']

def unzip_gz_file(gz_file_path, output_path):
    with gzip.open(gz_file_path, 'rb') as gz_file:
        with open(output_path, 'wb') as output_file:
            shutil.copyfileobj(gz_file, output_file)

#gz_file_path = '../datasets/flows.txt.gz'
#output_path = '../datasets/flow.txt'
#unzip_gz_file(gz_file_path, output_path)

def txt_to_csv(txt_file_path, csv_file_path):
    with open(txt_file_path, 'r') as txt_file:
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(column_names)
            for line in txt_file:
                fields = line.strip().split(',')
                writer.writerow(fields)

txt_file_path = '../datasets/flow.txt'
csv_file_path = '../datasets/flow.csv'
txt_to_csv(txt_file_path, csv_file_path)

with open('../datasets/flow.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    row_count = 0
    for row in reader:
        print(row)
        row_count += 1
        if row_count >= 20:
            break