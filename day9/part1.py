input_string = """AlphaCentauri to Snowdin = 66
AlphaCentauri to Tambi = 28
AlphaCentauri to Faerun = 60
AlphaCentauri to Norrath = 34
AlphaCentauri to Straylight = 34
AlphaCentauri to Tristram = 3
AlphaCentauri to Arbre = 108
Snowdin to Tambi = 22
Snowdin to Faerun = 12
Snowdin to Norrath = 91
Snowdin to Straylight = 121
Snowdin to Tristram = 111
Snowdin to Arbre = 71
Tambi to Faerun = 39
Tambi to Norrath = 113
Tambi to Straylight = 130
Tambi to Tristram = 35
Tambi to Arbre = 40
Faerun to Norrath = 63
Faerun to Straylight = 21
Faerun to Tristram = 57
Faerun to Arbre = 83
Norrath to Straylight = 9
Norrath to Tristram = 50
Norrath to Arbre = 60
Straylight to Tristram = 27
Straylight to Arbre = 81
Tristram to Arbre = 90"""

distances = input_string.split("\n")
map_graph = {}

for distance in distances:
    distance_split = distance.split(" = ")
    locations = distance_split[0]
    distance_value = int(distance_split[1])

    location_1 = locations.split(" to ")[0]
    location_2 = locations.split(" to ")[1]

    # print(distance_value, location_1, location_2)

    try:
        map_graph[location_1].append({"city": location_2, "distance": distance_value})
    except (KeyError):
        map_graph[location_1] = [{"city": location_2, "distance": distance_value}]

    try:
        map_graph[location_2].append({"city": location_1, "distance": distance_value})
    except (KeyError):
        map_graph[location_2] = [{"city": location_1, "distance": distance_value}]

minimum_spanning_tree = {}
path_weights = []

while minimum_spanning_tree.keys() != map_graph.keys():
    for key in map_graph.keys():
        lowest = 99999
        city = ""
        for distance in sorted(map_graph[key], key=lambda k: k['distance']):
            if distance['distance'] < lowest and (distance['city'] not in minimum_spanning_tree.keys() and key not in minimum_spanning_tree.keys()):
                city = distance['city']
                lowest = distance['distance']

        minimum_spanning_tree[key] = {city: lowest}
        path_weights.append(lowest)
        print(minimum_spanning_tree)
# print(map_graph)
# print(minimum_spanning_tree)
final_distance = 0
for path_weight in path_weights:
    final_distance += path_weight

print(final_distance - 99999)