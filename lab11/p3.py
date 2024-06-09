# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("Daoguang/PyCodeGPT")
model = AutoModelForCausalLM.from_pretrained("Daoguang/PyCodeGPT")

def generate_method_from_description(description):
    inputs = tokenizer.encode(description, return_tensors="pt")
    outputs = model.generate(inputs, max_length=512, num_beams=5, early_stopping=True)
    method = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return method

# Example usage
description = "Write a Python method with the name 'add' that adds two numbers"
generated_method = generate_method_from_description(description)
print("Generated Method:", generated_method)


