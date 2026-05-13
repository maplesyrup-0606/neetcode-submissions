class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n);
        for (auto& e : edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }

        vector<bool> visited(n, false);

        function <void(int, int)> dfs = [&] (int node, int parent) -> void {
            visited[node] = true;

            for (int nei : graph[node]) {
                if (visited[nei]) continue;
                if (parent == nei) continue;
                dfs(nei, node);
            }
            return;
        };

        int connected = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, -1);
                connected++;
            }
        }

        return connected;
    }
};
