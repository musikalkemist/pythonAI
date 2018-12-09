"""
Author: Valerio Velardo
Email: valeriovelardo@gmail.com
Website: http://valeriovelardo.com
Python AI mailing list (free AI and ML tutorials): https://bit.ly/2K4gqE5

This file contains an implementation of a simpple feedforward neural network.
"""

# Remember to pip install the numpy library, if you haven't downloaded it
# already!
import numpy as np


class FeedForwardNet(object):
    """A class that represents a simple feedforward neural network, with an
    input layer, a hidden layer and an output layer. The layers are fully
    connected:each neuron of a layer, is connected with all the neurons of the
    following layer.
    """

    def __init__(self, x, y, numNeuronsHiddenLayer=5):
        """Class constructor

        Args:
            x (numpy array): Training input data in the form of a 2d array
            y (numpy array): Training output represented as a 2d array
            numNeuronsHiddenLayer (int): Number of neurons of the hidden
                layer of the network. Defaulted to 5.
        """

        super(FeedForwardNet, self).__init__()

        # training input data
        self.input = x

        # get number of input neurons from training data
        numInputNeurons = self.input.shape[1]

        # randomise weights between input and hidden layer
        self.weights1 = np.random.rand(numInputNeurons, numNeuronsHiddenLayer)

        # randomise weights between hidden and output layer
        self.weights2 = np.random.rand(numNeuronsHiddenLayer,1)

        self.y = y

        # initialise output of the network with all zeros
        self.output = np.zeros(self.y.shape)


    def feedforward(self):
        """Apply feedforward propagation."""

        # calculate dot product between input layer and 1st layer of weights
        dotProductLayer1 = np.dot(self.input, self.weights1)

        # apply sigmoid activation function
        self.layer1 = self._sigmoid(dotProductLayer1)

        # calculate dot product between hidden layer and 2nd layer of weights
        dotProductLayer2 = np.dot(self.layer1, self.weights2)

        # apply sigmoid activation function
        self.output = self._sigmoid(dotProductLayer2)


    def backpropagation(self):
        """Propagate the error back, and update weights and biases. Sum of
        square errors is used as the loss function."""

        # calculate the derivative of the loss function with respect to
        # weights2
        d_loss_function2 = (2*(self.y - self.output) *
                            self._sigmoid_derivative(self.output))
        d_weights2 = np.dot(self.layer1.T, d_loss_function2)

        # calculate the derivative of the loss function with respect to
        # weights1
        d_loss_function1 = (np.dot(2*(self.y - self.output) *
                            self._sigmoid_derivative(self.output),
                            self.weights2.T) *
                            self._sigmoid_derivative(self.layer1))
        d_weights1 = np.dot(self.input.T,  d_loss_function1)

        # update the weights with the derivative of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2


    def train(self, epochs):
        """Train network using feedforward and back propagations.

        Args:
            epochs (int): Number of times we process the training data
        """
        for _ in range(epochs):
            self.feedforward()
            self.backpropagation()


    def _sigmoid(self, x):
        return 1.0 / (1 + np.exp(-x))


    def _sigmoid_derivative(self, x):
        return x * (1.0 - x)


if __name__ == "__main__":

    # training set for logic 'and'
    x = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])

    # training output
    y = np.array([[0],[0],[0],[1]])

    # instantiate neural net
    ffn = FeedForwardNet(x,y)

    # train for 1500 epochs
    ffn.train(1500)

    print(ffn.output)
