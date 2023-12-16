import json
import csv

def jsonl_to_csv(jsonl_file, csv_file):
    # Open JSON Lines file for reading
    with open(jsonl_file, 'r', encoding='utf-8') as jsonl_file:
        # Open CSV file for writing
        with open(csv_file, 'w', encoding='utf-8', newline='') as csv_file:
            # Create a CSV writer
            csv_writer = csv.writer(csv_file)

            # Write CSV header
            csv_writer.writerow(['text'])

            # Process each line in the JSON Lines file
            for line in jsonl_file:
                # Load JSON object from the line
                json_obj = json.loads(line)
                print(line)
                # Construct the 'text' content in the desired format
                text_content = f"### Human: {json_obj.get('prompt', '')} ### Assistant: {json_obj.get('completion', '')}"

                # Write to CSV
                csv_writer.writerow([text_content])

# Example usage
jsonl_to_csv('babbage/cookbook.jsonl', 'huggingface/guanaco/train.csv')
