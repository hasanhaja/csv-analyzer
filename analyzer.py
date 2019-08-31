import csv
import statistics as stats

def extract_value(array):
    array_tokens = array[0].split(";")
    value = float(array_tokens[1])
    return value

def process(list):
    """
    This function does all the mathematical heavy lifting and returns the data as a dictionary (aka map).
    """
    mean = stats.mean(list)
    #Error checking for mode
    try:
        mode = stats.mode(list)
    except:
        mode = "N/A"
    
    median = stats.median(list)
    stdev = stats.stdev(list)
    variance = stats.variance(list)
    
    results = {
        "mean": str(mean),
        "mode": str(mode),
        "median": str(median),
        "stdev": str(stdev),
        "variance": str(variance),
    }

    if results["mode"] == "N/A":
        results.pop("mode")
        return results

    return results

def stringify_results(results):    
    text = ""
    for result_key in results:
        text += result_key.title() + ": " + results[result_key] + "\n"
    return text

def analyze(list):
    """
    This formats the data from the process function and outputs only the relavant data.
    """
    return stringify_results(process(list))

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

        result = analyze(values)
        print(result)

if __name__ == '__main__':
    main()