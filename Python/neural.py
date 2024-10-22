import numpy as np

# Activation function: Sigmoid and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Neural Network Class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights randomly with mean 0
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Weights between input and hidden layer
        self.W1 = np.random.randn(self.input_size, self.hidden_size)

        # Weights between hidden and output layer
        self.W2 = np.random.randn(self.hidden_size, self.output_size)

    # Forward Propagation
    def forward(self, X):
        # Input to hidden layer
        self.z1 = np.dot(X, self.W1)
        self.a1 = sigmoid(self.z1)

        # Hidden to output layer
        self.z2 = np.dot(self.a1, self.W2)
        output = sigmoid(self.z2)
        return output

    # Backward Propagation
    def backward(self, X, y, output):
        # Calculate error at output
        output_error = y - output
        output_delta = output_error * sigmoid_derivative(output)

        # Calculate error at hidden layer
        hidden_error = output_delta.dot(self.W2.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.a1)

        # Update weights using the gradients
        self.W2 += self.a1.T.dot(output_delta)
        self.W1 += X.T.dot(hidden_delta)

    # Training the neural network
    def train(self, X, y, epochs):
        for epoch in range(epochs):
            # Forward propagation
            output = self.forward(X)

            # Backward propagation and update weights
            self.backward(X, y, output)

            # Every 1000 epochs, print the error to track progress
            if epoch % 1000 == 0:
                loss = np.mean(np.square(y - output))
                print(f"Epoch {epoch}, Loss: {loss}")

# Example usage

# Input dataset (XOR problem)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Output dataset
y = np.array([[0], [1], [1], [0]])

# Create the Neural Network
nn = NeuralNetwork(input_size=2, hidden_size=2, output_size=1)

# Train the neural network
nn.train(X, y, epochs=10000)

# Test the neural network after training
for i in range(len(X)):
    print(f"Input: {X[i]} -> Predicted Output: {nn.forward(X[i])}")
