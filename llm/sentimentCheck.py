

# Replace 'textattack/bert-base-uncased-SST-2' with the model name you want to use
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# Load pre-trained sentiment analysis model and tokenizer
model_name = "textattack/bert-base-uncased-SST-2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Example sentences for sentiment analysis
sentences = [
    "I love this recipe, it's amazing!",
    "The food was great and very tasty.",
    "This food was disappointing, I didn't enjoy it.",
]

# Tokenize and get model predictions
for sentence in sentences:
    # Tokenize input sentence
    tokens = tokenizer(sentence, return_tensors="pt")

    # Forward pass through the model
    outputs = model(**tokens)

    # Get predicted sentiment (positive or negative)
    prediction = "positive" if outputs.logits.argmax().item() == 1 else "negative"

    # Print the result
    print(f"Sentence: '{sentence}'\nPredicted Sentiment: {prediction}\n")
