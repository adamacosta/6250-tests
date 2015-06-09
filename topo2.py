# Topology with a single loop
# A --- B --- C
# |     |
# D --- E


topo = { 'A' : ['B', 'D'],
         'B' : ['A', 'C', 'E'],
         'C' : ['B'],
         'D' : ['A', 'E'],
         'E' : ['B', 'D'] }

ans = 'A:A0,B1,C2,D1,E2' + \
      'B:A1,B0,C1,D2,E1' + \
      'C:A2,B1,C0,D3,E2' + \
      'D:A1,B2,C3,D0,E1' + \
      'E:A2,B1,C2,D1,E0'