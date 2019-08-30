import csv

def extract_value(array):
    array_tokens = array[0].split(";")
    value = float(array_tokens[1])
    return value


def average_values(list):
    return sum(list) / len(list)

def main():
    with open('price_history_LU1664415285.csv') as csv_file:
        # Book keeping mainly
        csv_reader = csv.reader(csv_file, delimiter='\n')
        line_count = 0
        values = []
        for row in csv_reader:
            # Line count only to check if it is not the first line
            if line_count == 0:
                line_count += 1
                continue
            else:
                values.append(extract_value(row))

        average = average_values(values)

        print(average)

if __name__ == '__main__':
    main()