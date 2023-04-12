import csv

class Node:
    def __init__(self, connections):
        self.collector = 0.0
        self.connections = connections

def read_file(in_file):
  inputs = list()
  with open(in_file, 'r') as file:
    contents = csv.reader(file)
    for line in contents:
       inputs.append(line)
  return inputs
      
    
def init_network(structure):
  network = []
  last_layer = None
  for layer_size in structure:
      layer = [Node(last_layer) for _ in range(layer_size)]
      network.append(layer)
      last_layer = layer
  return network
    
def feed_foward(network, inputs):
  for i, node in enumerate(network[0]):
    node.collector = inputs[i]
  for layer in network[1:]:
    for node in layer:
      node.collector = sum(connection.collector for connection in node.connections)
  return [node.collector for node in network[-1]]





if __name__ == '__main__':
  inputs = read_file('data.csv')
  print("inputs:", inputs)




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