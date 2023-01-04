from collections import deque

from collections import deque

def find_shortest_paths(connections: str) -> list[list[int]]:
    # create a map of connections between cities
    city_map = {}
    for line in connections.strip().split('\n'):
        a, b, cost = map(int, line.split())
        if a not in city_map:
            city_map[a] = {}
        if b not in city_map:
            city_map[b] = {}
        city_map[a][b] = cost

    # find the first and last cities
    first_city = min(city_map.keys())
    last_city = max(city_map.keys())
    
    # perform breadth-first search to find all the shortest paths
    paths = []
    queue = deque([[first_city]])
    visited = set()
    while queue:
        path = queue.popleft()
        print(path)
        last_city_in_path = path[-1]
        if last_city_in_path == last_city:
            # found a path from the first city to the last city
            paths.append(path)
            print("Path Gevonden!!!!!!")
            print(paths)
        else:
            for neighbor, cost in city_map[last_city_in_path].items():
                if neighbor not in visited :
                    queue.append(path + [neighbor])
                    visited.add(neighbor)
    return paths

# test the function
connections = '''
1 39 271
1 32 65
1 85 162
1 61 108
2 50 80
2 34 203
2 79 177
2 14 225
3 77 175
3 25 227
3 6 79
3 10 190
3 56 109
4 26 73
4 62 102
4 21 249
5 48 251
5 27 75
5 30 197
5 60 153
5 97 244
6 10 92
6 67 104
6 77 110
6 25 170
6 30 58
7 63 292
7 82 254
7 78 204
7 98 117
8 18 137
8 69 73
8 39 111
9 91 214
9 12 251
9 93 271
10 89 200
10 25 132
10 43 210
11 15 231
11 55 264
11 63 72
11 62 224
11 86 80
11 7 157
12 33 285
12 93 188
12 24 136
12 91 253
13 74 139
13 90 291
13 16 277
13 9 287
14 28 210
14 40 267
14 23 136
14 92 110
14 50 188
15 55 78
15 63 139
16 90 150
16 38 55
16 74 282
17 70 114
17 53 123
17 29 169
17 92 150
17 73 225
17 46 59
17 28 136
18 68 230
18 37 125
18 91 92
18 24 101
18 93 292
18 9 230
19 89 192
19 81 59
19 57 294
19 43 203
19 10 266
20 61 113
20 85 298
20 69 66
20 32 293
20 39 264
21 76 196
21 62 106
21 31 288
21 26 245
21 49 117
22 72 166
22 35 130
22 75 217
23 87 238
23 54 150
23 28 113
23 40 227
23 35 83
23 73 103
24 93 289
24 37 177
24 91 78
24 68 172
25 77 195
25 43 151
26 62 237
26 76 261
26 72 132
26 35 120
27 60 268
27 97 94
27 48 119
27 30 80
27 51 253
28 2 236
28 92 73
29 70 68
29 46 179
29 73 108
29 53 153
29 92 217
30 67 244
30 83 212
30 48 227
31 76 200
31 49 74
31 65 140
31 52 187
31 59 174
32 85 97
32 61 179
32 39 297
32 69 254
33 93 89
33 75 170
33 24 56
33 91 206
33 34 123
34 50 100
34 79 210
34 75 121
35 72 261
35 40 219
35 54 129
36 44 63
36 79 59
36 2 228
36 50 234
36 34 143
36 90 164
36 16 82
37 68 193
37 93 95
37 91 179
37 12 169
38 90 92
38 47 192
38 13 180
38 74 152
39 69 85
39 61 288
39 85 256
40 75 87
40 50 116
40 34 181
41 88 232
41 51 150
41 97 118
41 60 107
42 66 254
42 71 200
42 64 227
42 82 155
42 78 207
42 96 241
43 57 101
43 81 264
44 79 208
44 34 256
44 50 253
44 90 113
44 9 140
44 16 116
45 47 219
45 58 130
45 32 62
45 85 291
45 84 70
45 20 164
45 38 132
46 94 131
46 73 278
46 70 175
46 92 189
46 53 201
47 58 90
47 16 187
47 90 94
48 60 62
48 51 284
49 76 66
49 65 293
50 79 253
51 88 295
51 97 185
51 60 186
52 59 134
52 65 297
52 49 161
53 70 131
53 92 294
53 73 214
53 36 158
54 87 187
54 40 233
54 72 131
54 28 150
55 86 286
55 63 101
55 7 111
55 82 55
56 77 217
56 25 261
56 71 94
56 43 208
57 81 141
57 25 114
57 89 81
57 10 299
58 84 64
59 65 187
59 99 80
59 49 76
59 98 122
60 97 163
61 85 108
61 69 289
63 82 57
64 71 121
64 66 142
64 96 289
65 98 88
66 71 164
66 82 182
66 96 134
67 83 240
67 5 111
67 99 198
68 93 114
68 91 93
70 92 211
70 73 105
72 4 168
72 40 229
72 75 244
73 92 272
73 94 53
73 28 84
73 87 153
74 90 110
74 9 279
74 44 211
74 20 65
75 50 111
75 2 159
77 10 234
77 43 214
77 95 79
78 82 279
78 95 76
78 63 273
78 98 57
80 100 146
80 97 125
80 27 166
80 60 236
80 41 129
81 89 52
81 25 274
81 10 256
83 99 61
84 47 112
84 32 254
84 85 124
84 1 260
86 63 185
86 15 182
86 96 169
86 82 278
87 28 159
88 97 171
88 60 66
88 48 289
88 27 298
89 43 155
89 25 288
89 6 85
90 9 67
91 93 235
94 29 99
94 96 169
94 86 76
94 70 185
94 92 197
95 98 121
95 7 167
96 71 208
97 48 263
99 52 295
99 65 192
100 97 200
100 89 103
100 41 226
100 88 157
'''
table = []

for line in connections.strip().split('\n'):
    a, b, cost = map(int, line.split())
    # We maken een lijst met de 3 waardes uit elke rij, en voegen deze toe aan de tabel
    table.append([a, b, cost])

shortesPaths = find_shortest_paths(connections)  # should print [1, 2, 4, 6, 100]

print(shortesPaths) 


cost = 0
mincost = float("inf")
for q in range(len(shortesPaths)):
    for i in range(len(table)):
        for j in range(len(shortesPaths[q])):
            if shortesPaths[q][j] == table[i][0] and shortesPaths[q][j+1] == table[i][1]:
                cost += table[i][2]
    if cost < mincost:
        mincost = cost
        answer = shortesPaths[q]
    cost = 0            
            

print(cost)
print(answer)
print(mincost)