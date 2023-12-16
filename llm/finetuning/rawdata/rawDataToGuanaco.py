import pandas as pd

def convert_to_human_assistant_format(csv_path, output_csv_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)

    # Create a new 'text' column by combining the required fields in the specified format
    df['text'] = (
            "### Human: give me recipe for " + df['TranslatedRecipeName'] +
            " ### Assistant: " + df['TranslatedInstructions'] +
            "\nIngredients " +df["TranslatedIngredients"]+
            "\nCook Time: " + df['CookTimeInMins'].astype(str) +
            "\nCuisine: " + df['Cuisine'] +
            "\nDiet: " + df['Diet']
    )

    # Save the result to a new CSV file
    df[['text']].to_csv(output_csv_path, index=False)

if __name__ == "__main__":
    input_csv_path = 'IndianFoodDatasetCSV.csv'  # Replace with the actual path to your input CSV file
    output_csv_path = 'train.csv'  # Replace with the desired path for the output CSV file

    convert_to_human_assistant_format(input_csv_path, output_csv_path)
