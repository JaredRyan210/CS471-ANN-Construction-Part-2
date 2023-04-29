import csv
import random
import math
import time

class Node:
    def __init__(self, connections):
        self.collector = 0.0
        self.weights = []
        self.connections = connections
        self.delta = 0.0
        for i in range( len( connections ) ) :
            self.weights.append(random.random())



def read_network(in_file):
  with open(in_file, 'r') as file:
    contents = file.read().strip().split(',')
    return list(map(int, contents))

def read_csv(in_file):
  inputs = []
  #expected = []
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
  #print("inputs:",inputs)
  for i in range(len(inputs) - 1):
    network[0][i].collector = inputs[i]

  #####RUN_INPUT######
  for layer in (range(1,len(network))):
    #print(f"layer inputs {inputs}")
    for node in (network[layer]):
      for con_indx in range( len(node.connections)) :
        #weight = random.uniform(0,1)
        #print("Input:",inputs[i + 1])        
        #print("Initial weight:", conn.weight)
        node.collector = node.collector + (node.connections[con_indx].collector * node.weights[con_indx] )

        #print("collector:",node.collector)
      node.collector = transfer(node.collector)
      
  output = []
  for node in network[-1]:
    output.append(node.collector)
    #print("output",output)
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
          #print("delta", neuron.delta)
          #error += (neuron.connections[j].collector * neuron.delta)
          error += (neuron.weights[j] * neuron.delta)
        errors.append(error)
        #print(errors)
    else:
      for j in range(len(layer)):
        neuron = layer[j]
        errors.append(neuron.collector - expected[j])
    for j in range(len(layer)):
      neuron = layer[j]
      neuron.delta = errors[j] * transfer_deriv(neuron.collector)
      #print('delta',neuron.delta)



def update_weights(network, l_rate):
  for i in range(1, len(network)):
    inputs = [neuron.collector for neuron in network[i - 1]]
    for neuron in network[i]:
      for j in range(len(inputs)):
        neuron.weights[j] -= l_rate * neuron.delta * inputs[j]
        #print("updated weight:",neuron.connections[j].weight)


def train_network(network, train, l_rate, n_epoch, target_error):
  num_inputs = len(network[0])
  for epoch in range((n_epoch)):
    sum_error = 0.0
    for row in train:
      #print(row)
      forward_prop(row, network)
      expected = []
      for i in range(len(network[-1])):
        expected.append(row[num_inputs + i])
        #print(expected[i], "-", network[-1][i].collector, "**2", sum_error)
      sum_error += (expected[-1] - network[-1][i].collector) ** 2
        #sum_error += (error) ** 2
        #sum_error += (expected[i] - network[-1][i].collector) ** 2
        #print('expected:', expected)
        #print("sum_error", sum_error)
        #print("row[num_inputs + i]:", row[num_inputs + i])
        #print("network[-1][i].collector:",network[-1][i].collector)
        
        #print("sum error total: ",sum_error)
      backward_propagate_error(network, expected)
      update_weights(network,l_rate)          
        #print("sum error total: ",sum_error)

    if sum_error <= (target_error):
      print("Target error reached...error r=%f" % (sum_error))
      return
    print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))


           

    

if __name__ == '__main__':



####IT WOOOOOOOOOOOORKKKKKKKSSSSS##############
  ########TESTING TRAIN_NETWORK########
  structure = read_network('network.txt')
  inputs = read_csv('data.csv')

  network = init_network(structure)

  train_network(network, inputs, l_rate= 0.5, n_epoch=10000, target_error= 0.5)
  start_time = time.time()
  print("---%s seconds ---" % (time.time() - start_time))

  ###############