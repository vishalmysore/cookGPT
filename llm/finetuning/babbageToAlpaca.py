import csv
import json

def convert_to_csv(input_file, output_file):
    # Open the input file for reading
    with open(input_file, 'r') as file:
        # Read each line from the file
        lines = file.readlines()

    # Define the CSV headers
    headers = ['instruction', 'input', 'output', 'text']

    # Open the output CSV file for writing
    with open(output_file, 'w', newline='') as csv_file:
        # Create a CSV writer
        csv_writer = csv.DictWriter(csv_file, fieldnames=headers)

        # Write the headers to the CSV file
        csv_writer.writeheader()

        # Iterate through each line in the file
        for line in lines:
            # Load JSON data from the line
            data = json.loads(line)

            # Write a row to the CSV file with the desired values
            csv_writer.writerow({
                'instruction': data.get('prompt', ''),
                'input': '',
                'output': '',
                'text': f"Below is an instruction that describes a task.\n### Instruction:\n{data.get('prompt', '')}\n\n### Response:\n{data.get('completion', '')}",
            })

if __name__ == "__main__":
    # Replace 'input.json' with the actual input file name
    input_filename = 'babbage/cookbook.jsonl'
    # Replace 'output.csv' with the desired output CSV file name
    output_filename = 'huggingface/alpaca/train.csv'

    convert_to_csv(input_filename, output_filename)
