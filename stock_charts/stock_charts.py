# python3
class StockCharts:
    def read_data(self):
        n, k = map(int, input().split())
        stock_data = [list(map(int, input().split())) for _ in range(n)]
        return stock_data

    def write_response(self, result):
        print(result)

    def min_charts(self, stock_data):
        n = len(stock_data)
        can_follow = [[] for _ in range(n)]
        for first in range(n):
            for second in range(n):
                if first != second and all(
                    a < b for a, b in zip(stock_data[first], stock_data[second])
                ):
                    can_follow[first].append(second)

        matched_right = [-1] * n

        def augment(stock, visited):
            for next_stock in can_follow[stock]:
                if visited[next_stock]:
                    continue
                visited[next_stock] = True
                if matched_right[next_stock] == -1 or augment(
                    matched_right[next_stock], visited
                ):
                    matched_right[next_stock] = stock
                    return True
            return False

        matching_size = 0
        for stock in range(n):
            if augment(stock, [False] * n):
                matching_size += 1
        return n - matching_size

    def solve(self):
        stock_data = self.read_data()
        result = self.min_charts(stock_data)
        self.write_response(result)


if __name__ == '__main__':
    stock_charts = StockCharts()
    stock_charts.solve()
