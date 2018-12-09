"""
Author: Valerio Velardo
Email: valeriovelardo@gmail.com
Website: http://valeriovelardo.com
Python AI mailing list (free AI and ML tutorials): https://bit.ly/2K4gqE5

This file contains an implementation of a neuron that processes input signals
and outputs a signal, using a sigmoid activation function.
"""

import math


def compute_output(inputs, weights):
    """Computes output of neuron based on input signals and connection
    weights. Output = f(x_1*w_1 + x_2*w_2 + ... + x_k*w_k), where 'f' is the
    sigmoid function.

    Args:
        inputs (list): Input signals
        weights (list): Connection weights

    Returns:
        output (float): Output value
    """

    s = 0

    # compute the sum of the product of the input signals and the weights
    for x, w in zip(inputs, weights):
        s += x*w

    # process sum through sigmoid activation function
    output = sigmoid(s)

    return output


def sigmoid(x):
    """Sigmoid activation function

    Args:
        x (float): Value to be processed

    Returns:
        y (float): Output
    """
    output = 1.0 / (1 + math.exp(-x))
    return output


if __name__ == "__main__":

    # value of input neurons
    inputs = [0.3, 0.4, 0.5]

    # weights of connections between input neurons and output neuron
    weights = [0.4, 0.7, 0.2]

    output = compute_output(inputs, weights)

    print("Computed value: {}".format(output))