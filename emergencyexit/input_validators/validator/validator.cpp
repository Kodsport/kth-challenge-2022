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

const int MAXN = 100;
const int MAXK = 100;

void run() {

  int n = Int(3,MAXN);
  Space();
  int m = Int(3,MAXN);
  Endl();

  int doors = 0;
  int k = 0;

  for(int c1 = 0; c1 < n; c1++){
      string row = Line();
      assert(sz(row) == m);
      for(int c2 = 0; c2 < m; c2++){
          assert(row[c2] == '.' || row[c2] == '#' || row[c2] == 'P');
          if((c1 == 0 || c2 == 0 || c1 == n-1 || c2 == m-1) && row[c2] != '#')doors++;
          if(row[c2] == 'P')k++;
      }
  }
  assert(k <= MAXK);
  assert(doors == 1);
  Eof();
}
