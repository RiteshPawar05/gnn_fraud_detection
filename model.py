class GraphNeuralNetwork:
    def __init__(self, in_channels, out_channels):
        self.in_channels = in_channels
        self.out_channels = out_channels

    def forward(self, x, edge_index):
        return [sum(node) for node in x]

if __name__ == '__main__':
    model = GraphNeuralNetwork(16, 2)
    print("GNN initialized.")
