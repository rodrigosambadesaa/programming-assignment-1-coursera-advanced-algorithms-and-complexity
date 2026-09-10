# python3
class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        matching = [-1] * n

        matching_right = [-1] * m

        def augment(flight, visited):
            for crew in range(m):
                if adj_matrix[flight][crew] and not visited[crew]:
                    visited[crew] = True
                    other = matching_right[crew]
                    if other == -1 or augment(other, visited):
                        matching[flight] = crew
                        matching_right[crew] = flight
                        return True
            return False

        for flight in range(n):
            augment(flight, [False] * m)
        return matching

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
