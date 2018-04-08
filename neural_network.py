import numpy as np
from layer import Layer
from util import squared_loss


class NeuralNetwork:

    def __init__(self, features, layers, classes, alpha, node_operator):
        if type(features) is not list or type(classes) is not list or (layers and type(layers) is not list):
            raise TypeError("One of the inputs is not a list.")
        if type(alpha) is not float:
            raise TypeError("Alpha must be a float between 0.0 and 1.0")
        if alpha < 0.0 or alpha > 1.0:
            raise ValueError("Alpha must be a float between 0.0 and 1.0")
        self.alpha = alpha
        self.features = np.array(features)
        self.layers = []
        inn = len(features)
        for i in range(len(layers)):
            self.layers.append(Layer(inn, layers[i],i, i==len(layers)))
            inn = layers[i]
        self.classes = np.array(classes)
        self.node_operator = node_operator
        # TODO: Initialize the weights and make the connected graph that is the network in some way

    def train(self, cases):
        # TODO: Implement the training process
        for case in cases:
            self.__process_case(case[0], case[1])

    def __inference_step(self, features):
        # TODO: Implement feedforward/inference step, prolly needs some inputs
        return np.array(np.zeros(len(layer)) for layer in self.hidden_layers)

    def __backward_pass(self, losses):
        # TODO: Implement backpropagation/backward pass
        pass

    def __compute_loss(self, actual, correct):
        return squared_loss(actual,correct)

    def __process_case(self, feature_vector, class_label):
        if class_label not in self.classes:
            raise TypeError("Label is not part of this network's classes.")
        if len(feature_vector) is not len(self.features):
            raise TypeError("Length if feature vector is not the same as the network's defined feature length.")
        # TODO: Run features through the current network, return losses for each layer?
        return np.array(np.zeros(len(layer)) for layer in self.hidden_layers)

    def evaluate(self,samples):
        ""
        #TODO: make function to test the network and calculate accuracy

