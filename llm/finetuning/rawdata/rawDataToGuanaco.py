import pandas as pd

def convert_to_human_assistant_format(csv_path, output_csv_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)

    # Create a new 'text' column by combining the required fields in the specified format
    df['text'] = (
            "### Human: give me recipe for " + df['TranslatedRecipeName'] +
            " ### Assistant: " + df['TranslatedInstructions'] +
            "\nIngredients " +df["Cleaned-Ingredients"]+
            "\nCook Time: " + df['TotalTimeInMins'].astype(str) +
            "\nCuisine: " + df['Cuisine']
    )

    # Save the result to a new CSV file
    df[['text']].to_csv(output_csv_path, index=False)

if __name__ == "__main__":
    input_csv_path = 'Cleaned_Indian_Food_Dataset.csv'  # Replace with the actual path to your input CSV file
    output_csv_path = 'train.csv'  # Replace with the desired path for the output CSV file

    convert_to_human_assistant_format(input_csv_path, output_csv_path)
