import libraries

# save model to `Destination`
with open("<Destination>", "wb") as f:
    pickle.dump(model, f)
    
# 
# Load model from `Destination``
with open("<Destination>", "rb") as f:
    loaded_model = pickle.load(f)
print(loaded_model)
