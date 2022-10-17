from collections import defaultdict
import json
import matplotlib.pyplot as plt
import numpy as np

class Graph:
  def __init__(self, vertices_list,edge_list):
    self.graph=defaultdict(set)
    for v in vertices_list:
      self.graph[v]=set()
    self.addEdges(edge_list)
  
  def addEdges(self, edge_list):
    for a, b in edge_list:
      self.graph[a].add(b)
  
  def removeNodes(self, nodes_list):
    for n in nodes_list:
      try:
        del self.graph[n]
        for _, values in self.graph.items():
          try:
            values.remove(n)
          except KeyError:
            pass
          
      except KeyError:
        pass
  
  def removeEdges(self, edge_list):
    for a, b in edge_list:
      if a in self.graph.keys():
        try:
          self.graph[a].remove(b)
        except KeyError:
          pass
      else:
        pass
  
  def __str__(self):
    
    return f'{dict(self.graph)}'


def graphStat(graph):
  N_vertices=len(graph.keys())
  N_edges=len([i for sublist in graph.values() for i in sublist])
  return f'There are {N_vertices} vertices and {N_edges} edges'


def serializeToJson(graph, filename):
  grSer={}
  for k, v in graph.items():
    grSer[k]=list(v)
  with open( filename , "w" ) as write:
    json.dump(grSer, write )
  return None

def deserializeFromJson(filename):
  fr_js=json.load(open(filename))
  return defaultdict(set,{int(k):set(v) for k, v in fr_js.items()})

def plotInOutDegrees(graph, filename):
  out_in={}
  for k, v in graph.items():
    out_degrees=len(v)
    in_degrees=0
    for k1, v1 in graph.items():
      if k1==k:
        continue
      if k in v1:
        in_degrees+=1
    out_in[k]=(out_degrees, in_degrees)
  fig, ax = plt.subplots(figsize=(10, 5))
  x = np.arange(len(out_in.keys()))
  width = 0.3
  in_l=[v[1] for k, v in out_in.items()]
  out_l=[v[0] for k, v in out_in.items()]
  in_bar = ax.bar(x - width/2,in_l ,width, label='in')
  out_bar = ax.bar(x + width/2, out_l, width, label='out')
  ax.set_ylabel('In/Out degrees')
  ax.set_xlabel('Nodes')
  ax.set_title('In/Out degrees of nodes in graph')
  ax.set_xticks(x, list(out_in.keys()))
  ax.legend()
  ax.bar_label(in_bar, padding=5)
  ax.bar_label(out_bar, padding=5)
  ax.set_ylim([0, max([max(in_l),max(out_l)])+1])
  fig.tight_layout()
  plt.savefig(filename)
  plt.close(fig)  
  return None 