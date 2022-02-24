# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import collections


def oceansFlowGrid(pacificGrid, heights):
    q = collections.deque()
    visit = set()
    rows = len(pacificGrid)
    cols = len(pacificGrid[0])
    for i in range(0, rows):
        for j in range(0, cols):
            if pacificGrid[i][j]:
                q.append((i, j))
                visit.add((i, j))

    while q:
        currentR, currentC = q.popleft()
        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        for dr, dc in directions:
            r, c = currentR + dr, currentC + dc
            if r in range(0, rows) and c in range(0, cols) and (r, c) not in visit and heights[currentR][currentC] <= heights[r][c]:
                q.append((r, c))
                visit.add((r, c))
                pacificGrid[r][c] = True
    return pacificGrid


class Solution:
    def pacificAtlantic(self, heights):
        m = len(heights[0])
        n = len(heights)
        pacificGrid = []
        for i in range(0, n):
            col = []
            for j in range(0, m):
                if i == 0 or j == 0:
                    col.append(True)
                else:
                    col.append(False)
            pacificGrid.append(col)
        pacificGrid = oceansFlowGrid(pacificGrid, heights)
        atlanticGrid = []
        for i in range(0, n):
            col = []
            for j in range(0, m):
                if i == n - 1 or j == m - 1:
                    col.append(True)
                else:
                    col.append(False)
            atlanticGrid.append(col)
        atlanticGrid = oceansFlowGrid(atlanticGrid, heights)
        output = []
        for i in range(0, n):
            for j in range(0, m):
                atlanticGrid[i][j] = pacificGrid[i][j] and atlanticGrid[i][j]
                if atlanticGrid[i][j]:
                    output.append([i, j])
        return output


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
