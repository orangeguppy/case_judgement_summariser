"""
1) Loading/Preprocessing data
2) Split dataset into train, validation, and test sets
3) Set hyperparameters (refer to Google Doc)
4) Instantiate model
5) Call the train() method to train the model
6) Call the test() method to evaluate model performance

Add method parameters as needed, this is just a template/pseudocode. 
Don't need to follow the steps in this specific order either, it's just a list of things we need to do

Some helpful documentation:
https://pytorch.org/tutorials/beginner/basics/data_tutorial.html
https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html for training a generic classifier
"""

# This line is to set the model to use the GPU if available, else the CPU
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)

# Generate Dataset
dataset = utils.generate_dataset()

# Specify hyperparameters

# Split dataset and create Dataloaders for each training set
# Need to create the train, validation, and testing dataset
# To load the data from each of the train, validation, and testing datasets, we need to create corresponding Dataloaders.
# train_loader, val_loader, test_loader =  # Do modify as needed, don't necessarily need to do it like this!!

# Instantiate model
# model = 
model.to(device) # Move the model to the GPU if available, else move it to the CPU

# Train the model
utils.train()

# Test the model
utils.test()