# Use a pipeline as a high-level helper
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline

from huggingface_hub import login

if __name__ == '__main__':

    # login(token="")

    model_hf = "meta-llama/Llama-2-7b-hf"

    pipe = pipeline("text-generation", model=model_hf)

    # Load model directly

    tokenizer = AutoTokenizer.from_pretrained(model_hf)
    model = AutoModelForCausalLM.from_pretrained(model_hf)

    input_text = "Helo, how are you?"
    inputs = tokenizer.encode(input_text, return_tensors='pt')
    outputs = model.generate(inputs, max_length=50, num_return_sequences=5, temperature=0.7)
    print("Generated text:")

    for i, output in enumerate(outputs):
        print(f"{i}: {tokenizer.decode(output)}")
