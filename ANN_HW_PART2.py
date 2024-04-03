import csv
import random
import math
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, connections):
        self.collector = 0.0
        self.weights = []
        self.connections = connections
        self.delta = 0.0
        for i in range( len( connections ) ) :
            fan_in = len(connections)
            fan_out = len(self.connections)
            self.weights.append(random.uniform
                                (-math.sqrt(6.0 / (fan_in + fan_out)), 
                                 math.sqrt(6.0 / (fan_in + fan_out)))
                              )

def read_network(in_file):
  with open(in_file, 'r') as file:
    contents = file.read().strip().split(',')
    return list(map(int, contents))

def read_csv(in_file):
  inputs = []
  with open(in_file, 'r') as file:
    contents = csv.reader(file)
    for line in contents:
      inputs.append([float(x) for x in line]) ###[:-1] to get 4 inputs
      #expected.append([float(x) for x in line[-1]])
    #print(inputs)
  return inputs

def init_network(structure):
  network = []
  last_layer = []
  for layer_size in structure:
      layer = [Node(last_layer) for _ in range(layer_size)]
      network.append(layer)
      last_layer = layer
  return network

def forward_prop(inputs, network):
  #plt.ion()
  #print("inputs:",inputs)
  for i in range(len(inputs) - 1):
    network[0][i].collector = inputs[i]

  #####RUN_INPUT######
  for layer in (range(1,len(network))):
    #print(f"layer inputs {inputs}")
    for node in (network[layer]):
      for con_indx in range( len(node.connections)) :
        node.collector = node.collector + (node.connections[con_indx].collector * node.weights[con_indx] )

      node.collector = transfer(node.collector)

    #if layer == 1:
      #visualize_image(inputs)
      
  output = []
  for node in network[-1]:
    output.append(node.collector)
    #print(output)
  #plt.ioff()
  return output

def transfer(activation):
  return 1.0 / (1.0 + math.exp(-activation))

def transfer_deriv(output):
  return output * (1.0 - output)

def backward_propagate_error(network, expected):
  for i in reversed(range(len(network))):
    layer = network[i]
    errors = []
    if i != len(network) - 1:
      for j in range(len(layer)):
        error = 0.0
        for neuron in network[i + 1]:
          error += (neuron.weights[j] * neuron.delta)
        errors.append(error)
    else:
      for j in range(len(layer)):
        neuron = layer[j]
        errors.append(neuron.collector - expected[j])
    for j in range(len(layer)):
      neuron = layer[j]
      neuron.delta = errors[j] * transfer_deriv(neuron.collector)

def update_weights(network, l_rate):
  for i in range(1, len(network)):
    inputs = [neuron.collector for neuron in network[i - 1]]
    for neuron in network[i]:
      for j in range(len(inputs)):
        neuron.weights[j] -= l_rate * neuron.delta * inputs[j]

def train_network(network, train, l_rate, n_epoch, target_error):
  plt.ion()
  num_inputs = len(network[0])
  num_classes = 26
  #print(num_inputs)
  for epoch in range((n_epoch)):
    sum_error = 0.0
    for row in train:
      forward_prop(row[1:], network)
      expected = one_hot_encoding(row[0], num_classes)
      for i in range(len(network[-1])):
        error = expected[i] - network[-1][i].collector
        sum_error += pow(error, 2)
      backward_propagate_error(network, expected)
      update_weights(network, l_rate)
      #visualize_network(network)
      #visualize_image(row[1:])
                
    if sum_error <= (target_error):
      print(f"Target error reached. Error: {sum_error}")
      return
    print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
  plt.ioff()

def one_hot_encoding(letter_index, num_classes):
  encoded_vector = [0] * num_classes
  encoded_vector[letter_index] = 1
  return encoded_vector

def calc_accuracy(network, test_set, num_classes):
  correct_prediction = 0

  for row in test_set:
    inputs = row[1:]
    #print("inputs:", inputs)
    expected = one_hot_encoding(row[0], num_classes)
    print("expected:", expected)

    output = forward_prop(inputs, network)
    print("output:", output)

    predicted_class = np.argmax(output)
    print("predicted_class:", predicted_class)
    actual_class = np.argmax(expected)
    print("actual_class:", actual_class)

    if predicted_class == actual_class:
      correct_prediction += 1
    print("Correct Predictions:", correct_prediction)


  accuracy = correct_prediction / len(test_set)
  return accuracy

def visualize_image(data):
  image_data = np.array(data).reshape(28, 28)

  plt.imshow(image_data, cmap='gray', vmin=0, vmax=1)
  plt.draw()
  plt.pause(0.001)

def visualize_network(network):
    G = nx.DiGraph()

    for layer_idx, layer in enumerate(network):
        for node_idx, node in enumerate(layer):
            node_label = f'Layer {layer_idx}\nNode {node_idx}\n{node.collector:.2f}'
            G.add_node(node_label)

            if layer_idx > 0:
                for prev_node_idx, weight in enumerate(node.weights):
                    prev_node_label = f'Layer {layer_idx - 1}\nNode {prev_node_idx}\n'
                    G.add_edge(prev_node_label, node_label, weight=weight)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_size=100, node_color='skyblue', font_size=4)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()
  

def train_and_test_for_letter(letter, train_limit=10, test_limit=100):
  con = sqlite3.connect("hw_data.db")
  cur = con.cursor()

  sql_train = f"select * from hw_data where letter = {letter} order by random() limit {train_limit}"
  cur.execute(sql_train)
  train_data = cur.fetchall()

  sql_test = f"Select * from hw_data where letter = {letter} order by random() limit {test_limit}"

  cur.execute(sql_test)
  test_data = cur.fetchall()



  structure = read_network('network.csv')
  network = init_network(structure)
  #visualize_network(network)

  letter_ascii = chr(letter + 65)
  print("training network on letter: ", letter_ascii)
  train_network(network, train_data, l_rate=0.01, n_epoch=1000, target_error=0.5)

  num_classes = 26
  #test_accuracy = calc_accuracy(network, test_data, num_classes)
  #print(f'Test Set Accuracy for letter {letter}: {test_accuracy * 100:.2f}%')







if __name__ == '__main__':

  train_and_test_for_letter(letter=0, train_limit=100)

