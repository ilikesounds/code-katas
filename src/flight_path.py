"""
Flight path module for code kata assignment.

Simple Graph taken from data-structures assignment.

Thanks to Dave Smith for all his help with this assignment:
https://github.com/Bl41r/code-katas
"""

import json
import io
from simple_graph import SimpleGraph, Node


def calculate_distance(point1, point2):
    """
    Calculate the distance (in miles) between point1 and point2.
    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.

    Modified and converted to Python from:
    http://www.movable-type.co.uk/scripts/latlong.html
    """
    import math

    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3  # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])
    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])

    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * \
        math.cos(phi2) * math.sin(0.5 * delta_lam)**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934  # convert km to miles


def get_json_data(json_file):
    """Retrieve cities from the supplied json file"""
    with io.open(json_file) as json_data:
        data = json.load(json_data)
    city_list = []
    for location in data:
        entry = {}
        entry['city'] = location['city']
        entry['neighbors'] = location['destination_cities']
        entry['lat-lon'] = location['lat_lon']
        city_list.append(entry)
    return city_list


def build_city_graph(new_data):
    """Build a city airport graph."""
    city_graph = SimpleGraph()

    for city in new_data:
        city_graph_node = Node(city['city'], city['lat-lon'])
        try:
            city_graph.add_node(city_graph_node)
        except KeyError:
            pass

    for city in new_data:
        if city['city'] not in city_graph.node_dict.keys():
            continue
        key = city['city']
        for neighbor in city['neighbors']:
            try:
                distance = calculate_distance(
                    city_graph.node_dict[key].data,
                    city_graph.node_dict[neighbor].data
                    )
            except KeyError:
                continue
            city_graph.node_dict[key].neighbors.append((neighbor, distance))
    return city_graph


def flight_path_distance(city_graph, origin, destination):
    """
    This function provides the flight path distance using a depth first
    traversal on the city_graph using an origin and destination.
    """
    current_location = [origin]
    temp = []
    path = []
    distance = 0

    while len(current_location):
        current = current_location.pop()
        temp.append(current.name)
        path.append(current.name)
        if len(path) > 1:
            distance += calculate_distance(
                city_graph.node_dict[path[-2]].data,
                city_graph.node_dict[path[-1]].data
                )
        if current.name == destination.name:
            break
        if len(current.neighbors) == 0:
            path = [origin.name]
            distance = 0
        for city in current.neighbors:
            if city_graph.node_dict[city[0]].name not in temp:
                current_location.append(city_graph.node_dict[city[0]])
    return path, distance
