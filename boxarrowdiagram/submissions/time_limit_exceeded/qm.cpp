/*
This solution does not keep track of how many references each node has,
instead it calculates it whenever needed.

Should run q*m for well designed input.
*/

#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

const int MAXN = 1001001;
const ll mod = 1000000007;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n,m;
    cin >> n >> m;

    vector<pair<int,int>> edges;
    for (int i = 0; i < m; ++i) {
        int u,v;
        cin >> u;
        cin >> v;
        --u;
        --v;
        edges.push_back({u,v});
    }

    int q;
    cin >> q;

    vector<int> to_be_removed(m);
    vector<pair<int,int>> queries;
    for (int i = 0; i < q; ++i) {
        int x,y;
        cin >> x >> y;
        --y;
        queries.push_back({x,y});
        if (x == 1)
            to_be_removed[y] = 1;
    }
    

    // Add the rest to be remoced at the end
    for (int y = 0; y < m; ++y) {
        if (!to_be_removed[y])
            queries.push_back({1, y});
    }

    vector<int> out;
    vector<int> reachable(n);
    reachable[0] = 1;

    vector<vector<int>> graph(n);
    vector<vector<int>> graph2(n);
    
    reverse(queries.begin(), queries.end());
    for (auto [x,y] : queries) {
        if (x == 1) {
            auto [u,v] = edges[y];
            graph[u].push_back(v);
            graph2[v].push_back(u);
            if (reachable[u]) {
                auto dfs = [&](int node, auto&& self) -> void{
                    while (graph[node].size()) {
                        int nei = graph[node].back();
                        graph[node].pop_back();
                        if (!reachable[nei]) {
                            reachable[nei] = 1;
                            self(nei, self);
                        }
                    }
                };
                dfs(u, dfs);
            }
        } else {
            int s = 0;
            for (auto node : graph2[y])
                s += reachable[node];
            out.push_back(s);
        }
    }

    reverse(out.begin(), out.end());
    for (auto ans : out)
        cout << ans << '\n';
}
