#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;
vector<vector<int>> adj;
vector<int> par;
vector<ll> sz, sz2;
vector<double> f_val, f_val_rev, f_sum;

template <typename T>
T sqr(T x) { return x*x; }

ll Sz(int u, int p) {
    if (p == -1) return n;
    if (u == -1) return 0;
    if (p == par[u]) return sz[u];
    return n - Sz(p, u);
}

void forw(int u, int p = -1) {
    par[u] = p;
    sz[u] = 1;
    f_sum[u] = 0;
    for (int &v: adj[u]) {
        if (v != p) {
            forw(v, u);
            sz[u] += sz[v];
            sz2[u] += sz[v]*sz[v];
            f_sum[u] += f_val[v];
        }
    }
    f_val[u] = sz[u] + sqr(sz[u]-1) - sz2[u] + f_sum[u];
}

double f(int u, int p) {
    if (p == par[u]) return f_val[u];
    if (p != -1) {
        assert(u == par[p]);
        if (f_val_rev[p] > 0) return f_val_rev[p];
    }
    
    ll s = Sz(u, p);
    
    ll s2 = sz2[u];
    if (p != -1) s2 -= sz[p]*sz[p];
    if (par[u] != -1) s2 += sqr(Sz(par[u], u));
    
    double fs = f_sum[u];
    if (p != -1) fs -= f_val[p];
    if (par[u] != -1) fs += f(par[u], u);
    
    double ans = s + sqr(s-1) - s2 + fs;
    if (p != -1) {
        f_val_rev[p] = ans;
    }
    return ans;
}

int main(void) {
    scanf("%d", &n);
    adj.resize(n+1);
    for (int i = 0; i < n-1; ++i) {
        int u, v;
        scanf("%d%d", &u, &v);
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    par.resize(n+1);
    sz.resize(n+1);
    sz2.resize(n+1);
    f_val.resize(n+1);
    f_val_rev.resize(n+1);
    f_sum.resize(n+1);

    forw(1, -1);
    double opt = 1e99;
    vector<int> optrooms;
    for (int i = 1; i <= n; ++i) {
        double x = f(i, -1) / n;
        //printf("%d %lf\n", i, x);
        if (x < opt - 1e-9) {
            optrooms.clear();
            opt = x;
        }
        if (x < opt + 1e-9) {
            optrooms.push_back(i);
        }
    }
    printf("%d\n", optrooms.size());
    for (int u: optrooms)
        printf("%d\n", u);
}
