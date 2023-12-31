# from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import pickle
# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
# model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")

# save_model = open(r"chatmodel.pickle","wb")
# pickle.dump(model, save_model)
# save_model.close()

# save_tokenizer = open(r"chattokenizer.pickle","wb")
# pickle.dump(tokenizer,save_tokenizer)
# save_tokenizer.close()

open_file = open("chatmodel.pickle", "rb")
model= pickle.load(open_file)
open_file.close()

open_file = open("chattokenizer.pickle", "rb")
tokenizer= pickle.load(open_file)
open_file.close()

def predict(input, history=[]):
    # tokenize the new input sentence
    new_user_input_ids = tokenizer.encode(input + tokenizer.eos_token, return_tensors='pt')

    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([torch.LongTensor(history), new_user_input_ids], dim=-1)

    # generate a response 
    history = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id).tolist()

    # convert the tokens to text, and then split the responses into lines
    response = tokenizer.decode(history[0]).split("<|endoftext|>")
    # response = [(response[i], response[i+1]) for i in range(0, len(response)-1, 2)]  # convert to tuples of list
    return list(response)[1]

