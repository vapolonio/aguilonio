"""
Esse arquivo gera a topologia, a partir dos nos que estao descritos em nodes_gen
"""

# Imports
import pandas as pd
import math
import nodes_gen


def Network_gen(inputs, topo, outputs, name, input_size, output_size):
    """
    Nessa funcao inputs eh o numero de inputs que eu quero
    topo tem o formato [n,m,k, ... , z] com a topologia da rede
    outputs eh a quantidade de saidas que temos
    
    Aqui eu pego essas informacoes e monto a topologia, para depois
    serem definidos os pesos.
    """

    # Creates a new file
    topo_done = open("%s.vhd" %name, "w+")

    topo_string = '--Headers\nlibrary ieee;\nuse ieee.std_logic_1164.all; \nuse ieee.numeric_std.all;\nentity Node is\n     generic (\n            '
    
    in_size = input_size
    out_size = output_size

    input_list = []
    for i in range(1, inputs):
        # Gero tambem uma lista com os nomes das entradas
        # Gero a primeira camada da minha rede, a camada de inputs
        inputs_list.append('input_%s' %i)
        topo_string = topo_string + '\n'

    topo_string = topo_string + ');'
        

        
    for layer in range(len(topo)):
        # Gero cada camada da topologia
        layer_nodes = topo[layer]

        for node in range(layer_nodes):
            topo_string = topo_string + ''
