from flight_path import(
    get_json_data,
    build_city_graph,
    flight_path_distance
    )


def test_get_json_data_length():
    """Confirm that the length """
    data = get_json_data('./data/cities_with_airports.json')
    assert len(data) > 0


def test_get_json_data_container_type():
    """Confirm that the container is a list"""
    data = get_json_data('./data/cities_with_airports.json')
    assert type(data) is list


def test_get_json_data_item():
    """Confirm that the items in the list is a dict"""
    data = get_json_data('./data/cities_with_airports.json')
    assert type(data[0]) is dict


def test_build_city_graph_edges():
    """Assert city graph edges are built."""
    data = get_json_data('./data/cities_with_airports.json')
    city_graph = build_city_graph(data)
    assert len(city_graph.edges()) > 0


def test_build_city_graph_node_dict():
    """Assert city graph node dictionary is populated."""
    data = get_json_data('./data/cities_with_airports.json')
    city_graph = build_city_graph(data)
    assert len(city_graph.node_dict) > 0


def test_build_city_graph_nodes():
    """Assert city graph nodes are created."""
    data = get_json_data('./data/cities_with_airports.json')
    city_graph = build_city_graph(data)
    assert len(city_graph.nodes()) > 0


def test_build_city_graph_neighbors():
    """Assert city graph nodes are created."""
    data = get_json_data('./data/cities_with_airports.json')
    city_graph = build_city_graph(data)
    assert len(city_graph.neighbors(city_graph.node_dict['Charlotte'])) > 70


def test_flight_path_distance():
    """Assert search was completed."""
    data = get_json_data('./data/cities_with_airports.json')
    city_graph = build_city_graph(data)
    distance = flight_path_distance(
        city_graph,
        city_graph.node_dict['Charlotte'],
        city_graph.node_dict['Honolulu']
        )
    assert distance[0][0] == 'Charlotte' and distance[0][-1] == 'Honolulu'
