class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if (n - 1 != edges.size()) return false;

        vector<vector<int>> graph(n);

        for (auto& e : edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }

        vector<bool> visited(n, false);

        function <bool(int, int)> dfs = [&] (int node, int parent) -> bool {
            visited[node] = true;

            for (int nei : graph[node]) {
                if (nei == parent) continue;
                if (visited[nei]) return true;
                if (dfs(nei, node)) return true;
            }

            return false;
        };

        if (dfs(0, -1)) return false;

        for (bool v : visited) {
            if (!v) return false;
        }

        return true;
    }
};
