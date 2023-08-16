neighbors = {
 'Arad':('Sibiu','Timisoara','Zerind'),
 'Zerind':('Arad','Oradea'),
 'Oradea':('Sibiu','Zerind'),
 'Timisoara':('Arad','Lugoj'),
 'Lugoj':('Mehadia','Timisoara'),
 'Mehadia':('Drobeta','Lugoj'),
 'Drobeta':('Craiova','Mehadia'),
 'Craiova':('Drobeta','Pitesti','Rimnicu'),
 'Sibiu':('Arad','Fagaras','Oradea','Rimnicu'),
 'Fagaras':('Bucareste','Sibiu'),
 'Rimnicu':('Craiova','Pitesti','Sibiu'),
 'Pitesti':('Bucareste','Craiova','Rimnicu'),
 'Neamt':('Iasi',),
 'Iasi':('Neamt','Vaslui'),
 'Vaslui':('Iasi','Urziceni'),
 'Bucareste':('Fagaras','Giurgiu','Pitesti','Urziceni'),
 'Giurgiu':('Bucareste',),
 'Urziceni':('Bucareste','Hirsova','Vaslui'),
 'Hirsova':('Eforie','Urziceni'),
 'Eforie':('Hirsova',),
}

distances={
 'Arad':(140,118,75),
 'Zerind':(75,71),
 'Oradea':(151,71),
 'Timisoara':(118,111),
 'Lugoj':(70,111),
 'Mehadia':(75,70),
 'Drobeta':(120,75),
 'Craiova':(120,138,146),
 'Sibiu':(140,99,151,80),
 'Fagaras':(211,99),
 'Rimnicu':(146,97,80),
 'Pitesti':(101,138,97),
 'Neamt':(87,),
 'Iasi':(87,92),
 'Vaslui':(92,142),
 'Bucareste':(211,90,101,85),
 'Giurgiu':(90,),
 'Urziceni':(85,98,142),
 'Hirsova':(86,98),
 'Eforie':(86,),
}

def our_in(element,L):
    contains = False
    for i in range(len(L)):
        if element == L[i][0][-1]:
            contains = i
            break
    return -1

def objective(state):
    return state=='Bucareste'

def criterion(x):
    return x[1]

initial_state = [['Arad'],0]

B = [] #fila
E = []

B.append(initial_state)
foundIt = False

while not foundIt:
  if (len(B)==0):
    break
  B = sorted(B,key=criterion)
  node = B[0][:]
  del B[0]
  if(objective(node[0][-1])):
    foundIt = True
    break
  E.append(node[0][-1])
  
  for neighbor in neighbors[node[0][-1]]:
      p = our_in(neighbor,B)
      e = neighbors[node[0][-1]].index(neighbor)
      d = distances[node[0][-1]][e]  
      if p == -1 and not neighbor in E:
          B.append([ node[0] + [neighbor], node[1]+ d  ])
      elif ( p!= -1):
          if(B[p][1] > node[1]+ d):
              del B[p]
              B.append([ node[0] + [neighbor], node[1]+ d  ])
          
          
if foundIt: 
  print (node)
else:
  print ('Not found.')
    