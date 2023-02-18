#include "validator.h"

#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(i, a) for(auto& i : a)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

const int MAXN = 1000;

void run() {
  int n = Int(2,MAXN);
  Endl();

  for(int c1 = 0; c1 < n; c1++){
      string row = Line();
      assert(sz(row) == n);
      for(int c2 = 0; c2 < n; c2++){
          assert(row[c2] == '0' || row[c2] == '1');
      }
  }
  Eof();
}
