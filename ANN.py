#FIRST: get row from csv file, last column is expected output
#SECOND: feed foward(run_input -> activate -> transfer)
#THIRD: 

import csv
import random
import math

class Node:
    def __init__(self, connections):
        self.collector = 0.0
        self.connections = connections


def read_network(in_file):
  with open(in_file, 'r') as file:
    contents = file.read().strip().split(',')
    return list(map(int, contents))

def read_csv(in_file):
  inputs = []
  expected = []
  with open(in_file, 'r') as file:
    contents = csv.reader(file)
    for line in contents:
       inputs.append([float(x) for x in line]) ###[:-1] to get 4 inputs
  return inputs

def init_network(structure):
  network = []
  last_layer = None
  for layer_size in structure:
      layer = [Node(last_layer) for _ in range(layer_size)]
      network.append(layer)
      last_layer = layer
  return network

def forward_prop(inputs, network):
  print("inputs:",inputs)
  for i in range(len(inputs) - 1):
    network[0][i].collector = inputs[i]
  #####RUN_INPUT######
  for layer_index, layer in enumerate(range(1,len(network))):
    for node_index, node in enumerate(network[layer]):
      node.collector = 0.0
      for conn_index, conn in enumerate(node.connections):
        weight = random.uniform(0,1)

        node.collector += conn.collector * weight
        node.collector = transfer(node.collector)
        
        print(f"weight of: {layer_index + 1}, {node_index + 1}, {conn_index + 1}:", weight)
        print(f"value at collector:{layer_index + 1}, {node_index + 1}, {conn_index + 1}:", node.collector)
      print("\n")
      
  output = []
  for node in network[-1]:
    output.append(node.collector)
    print("output",output)
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
          error += (neuron.connections[j].collector * neuron.delta)
        errors.append(error)
    else:
      for j in range(len(layer)):
        neuron = layer[j]
        errors.append(neuron.collector - expected[j])
    for j in range(len(layer)):
      neuron = layer[j]
      neuron.delta = errors[j] * transfer_deriv(neuron.collector)





if __name__ == '__main__':
  '''
  ######TESTING FORWARD_PROP########
  structure = read_network('network.txt')
  inputs = read_csv('data.csv')

  network = init_network(structure)

  output = forward_prop(inputs[0], network)
  ########################
  '''


#####TESTING BACK_PROP_ERROR#########
  structure = read_network('network.txt')
  inputs = read_csv('data.csv')
  network = init_network(structure)

  for input_data in inputs:
    expected = [input_data[-1]]

  backward_propagate_error(network, expected)
  for layer in network:
    for neuron in layer:
      print(neuron.delta)
    print('\n')
###########################


'''
  print("The structure of the ANN is:",structure)
  print(f"The first layer contains {len(inputs[15])} input(s)")
  print(f"The hidden layer contains {structure[1]} nodes")
  print(f"The output layer contains {structure[2]} node")
  print("The inputs are:", inputs[15])
  for i in range(0, len(network)):
    for j in range(0, len(network[i])):
      print(network[i][j].collector)
    print('\n')
  print("The output is:", output)
  print("--------------------")
  #output = feed_foward(network, inputs)
'''


  



'''
  network_structure = read_file('data.csv')
  inputs = read_file('data.csv')
  network = init_network(network_structure)
  output = feed_foward(network, inputs)
  print("The structure of the ANN is:", network_structure)
  print(f"The first layer contains {len(inputs)} input(s)")
  print(f"The hidden layer contains {network_structure[1]} nodes")
  print(f"The output layer contains {network_structure[2]} node")
  print("The inputs are:", inputs)
  for i in range(0, len(network)):
     for j in range(0, len(network[i])):
      print(network[i][j].collector)
  print("The output is:", output)
'''