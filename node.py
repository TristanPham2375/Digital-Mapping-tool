# Imports


class Node:
    all_nodes = []

    def __init__(self, name):
        """
        Initializes a destination node.
        Use: node = Node(name)
        Parameters: 
        name - destination name, can only be a letter from the english alphabet
        """
        if len(name) == 1 and name.isalpha():
            self.name = name.upper()
            self.neighbors = {}
            Node.all_nodes.append(self)
        else:
            raise ValueError(
                "Name must be a single letter from the English alphabet.")

    def add_neighbor(self, neighbor, distance):
        """
        Adds a neighbor with the specified distance.
        Use: Node.add_neighbor(neighbor, distance)
        Parameters:
        neighbor - the neighboring Node
        distance - the distance to the neighbor
        """
        self.neighbors[neighbor] = distance

    def get_distance(self, node):
        """
        Finds the distance between two connected nodes.
        Use: Node.get_distance(node)
        Parameters:
        node - the neighbor node object to find the distance for
        """
        if node in self.neighbors:
            return self.neighbors[node]
        else:
            return None

    def print_neighbors(self):
        """
        Prints a node's neighbors and distance between them
        Use: Node.print_neighbors()
        """
        print(f"Neighbors of {self.name}: ")
        for neighbor, distance in self.neighbors.items():
            print(f"Neighbor: {neighbor.name}, Distance: {distance}")

    def check_shortest_path(self, end_node):
        """
        Finds the shortest path and distance between the current node and another node.
        Use: Node.check_path(end_name)
        Parameters: 
        end_node - the destination node
        """
        visited = []
        unvisited = []
        # table to store the distances between nodes and its previous node
        table = [[], [], []]

        for node in Node.all_nodes:

            unvisited.append(node.name)

            table[0].append(node.name)

            distance = float('inf')
            table[1].append(distance)

            table[2].append('temp')

        i = 0
        itself_index = 0
        main_node = self

        while i < len(table[0]):
            if table[0][i] == main_node.name:
                itself_index = i
            i += 1
        # distance from a node to itself is 0
        table[1][itself_index] = 0
        # previous node of a node to itself is none
        table[2][itself_index] = 'none'

        total_dist = 0
        while(main_node.name != end_node.name):

            for neighbor, distance in main_node.neighbors.items():
                name = neighbor.name
                real_dist = distance + total_dist

                i = 0
                index = 0
                while i < len(table[0]):
                    if table[0][i] == name:
                        index = i
                    i += 1

                if real_dist < table[1][index]:
                    table[1][index] = real_dist
                    table[2][index] = main_node.name

            for node in unvisited:
                if node == main_node.name:
                    unvisited.remove(node)
                    visited.append(node)

            # choosing new main_node
            shortest_dist = float('inf')
            value = 0
            for neighbor, distance in main_node.neighbors.items():
                j = 0
                index_next = 0
                while j < len(table[0]):
                    if table[0][j] == neighbor.name:
                        index_next = j
                    j += 1

                if table[1][index_next] < shortest_dist:
                    shortest_dist = table[1][index_next]
                    main_node = neighbor
                    value = distance

            total_dist += value

        for node in unvisited:
            if node == main_node.name:
                unvisited.remove(node)
                visited.append(node)

        # producing the path
        path = []
        current = end_node.name
        path.append(current)
        a = 0
        curr_index = 0
        while a < len(table[0]):
            if table[0][a] == current:
                curr_index = a
            a += 1

        current_previous = table[2][curr_index]

        path.append(current_previous)

        while current_previous != 'none':
            current = current_previous
            a = 0
            curr_index = 0
            while a < len(table[0]):
                if table[0][a] == current:
                    curr_index = a
                a += 1

            current_previous = table[2][curr_index]
            path.append(current_previous)

        path.reverse()

        k = 0
        path.pop(0)
        node1 = path[k]
        node2 = path[k + 1]
        total = 0

        while k < len(path) - 1:

            temp1 = None
            temp2 = None

            for items in Node.all_nodes:
                if node1 == items.name:
                    temp1 = items

                if node2 == items.name:
                    temp2 = items

            dist = temp1.get_distance(temp2)

            total += dist

            k += 1
            if node2 != path[len(path) - 1]:
                node1 = path[k]
                node2 = path[k + 1]
            else:
                break

        print(f"The shortest distance is --> {total}")
        print()

        path_str = " --> ".join(path)
        print(f"The shortest path: {path_str}")
