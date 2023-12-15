from transformers import BertTokenizer, BertModel,BertForQuestionAnswering
import torch
# Replace 'textattack/bert-base-uncased-SST-2' with the model name you want to use
model_name = 'prajjwal1/bert-tiny'

tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForQuestionAnswering.from_pretrained(model_name)

# Example context and question
context = "food dishes."
question = "What is egg curry?"

# Tokenize input context and question
inputs = tokenizer(context, question, return_tensors='pt')

# Forward pass through the model
outputs = model(**inputs)

# Get the predicted start and end positions
start_positions = torch.argmax(outputs.start_logits)
end_positions = torch.argmax(outputs.end_logits)

# Decode the tokens to obtain the answer
answer_tokens = inputs['input_ids'][0][start_positions:end_positions+1]
answer = tokenizer.decode(answer_tokens)

# Print the answer
print("Question:", question)
print("Answer:", answer)