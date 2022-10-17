from graph_lib import * 

def main():
    connections=[(1,2), (1,3),(2,4), (3,1),(3,2)]
    vertices=[1,2,3,4]
    gr1=Graph(vertices,connections)
    print(gr1)
    print(graphStat(gr1.graph))
    serializeToJson(gr1.graph, 'gr1.json')
    print(deserializeFromJson('gr1.json'))
    plotInOutDegrees(gr1.graph, 'gr1.png')
    
    return None


if __name__ == "__main__":
    main()