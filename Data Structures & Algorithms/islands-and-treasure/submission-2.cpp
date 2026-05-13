class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        deque<pair<int, int>> points;
        int m = grid.size();
        int n = grid[0].size();
        int TREASURE = 0;
        vector<vector<bool>> visited(m, vector<bool>(n, false));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == TREASURE) {
                    points.push_back({i, j});
                    visited[i][j] = true;
                }
            }
        }


        int distance = 0;
        while(points.size()) {
            int level_len = points.size();

            vector<pair<int, int>> directions = {{1,0},{-1,0},{0,1},{0,-1}};

            for(int i = 0; i < level_len; i++) {
                pair<int, int> node = points[0];
                points.pop_front();

                // mark visited
                grid[node.first][node.second] = distance;
                // append directions
                for (auto& direction : directions) {
                    int nx = direction.first + node.first;
                    int ny = direction.second + node.second;

                    if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                    if (grid[nx][ny] == -1) continue;
                    if (grid[nx][ny] == 0) continue;
                    if (visited[nx][ny]) continue;
                    
                    visited[nx][ny] = true;
                    points.push_back({nx, ny});
                }
            }
            distance++;
        }
    }
};
