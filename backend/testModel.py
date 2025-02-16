from refugee_support_model import predict_priority_areas

example_input = [3, 2, 1, 0, 1, 2, 3, 0, 1, 2]

# Get priority areas from model
print("Predicted Priority Areas:", predict_priority_areas(example_input))
