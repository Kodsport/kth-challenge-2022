// usage: ./a.out input_file correct_output output_dir < contestants_output
#include <bits/stdc++.h>
using namespace std;

static string input_file, output_dir, answer_file;

void accept() {
    exit(42);
}

void wrong_answer(const string& msg) {
    ofstream(output_dir + "/judgemessage.txt", ofstream::app) << msg; 
    exit(43);
}

void judge_error(const string& msg) {
    ofstream(output_dir + "/judgemessage.txt", ofstream::app) << msg; 
	exit(1);
}

template <class F>
void assert_done(istream& is, F fail) {
    try {
        string dummy;
        is >> dummy;
		if (is) fail("Extraneous data at end of output: " + dummy);
    } catch(...) {}
}

void score(istream& is, vector<vector<int>> graph) {
	int n = graph.size();
    
    int leaves = 0;
    for (int i = 0; i < n; ++i) {
        if (graph[i].size() == 1)
            ++leaves;
    }
    
    auto readint = [&](){
        int m;
        if(!(is >> m)){
            wrong_answer("Failed to read integer.\n");
        }
        return m;
    };

    int m = readint();
    if(m > (leaves + 1)/2) {
        wrong_answer("Answer is not optimal.\n");
    }
    
    vector<vector<int>> end_stop(n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        u = readint();
        v = readint();
        if (u < 1 || u > n) {
            wrong_answer("Node label out of range.\n");
        }
        if (v < 1 || v > n) {
            wrong_answer("Node label out of range.\n");
        }
        --u;
        --v;
        end_stop[u].push_back(i);
        end_stop[v].push_back(i);
    }
	assert_done(is, wrong_answer);

    auto dfs = [&](int node, int p, auto&& self) -> set<int> {
        set<int> my_set;
        for (auto busline : end_stop[node]) {
            if (my_set.count(busline)) {
                my_set.erase(busline);
            } else {
                my_set.insert(busline);
            }
        }
        for (auto nei : graph[node]) {
            if (nei != p){
                set<int> other_set = self(nei, node, self);
                if (my_set.size() < other_set.size()) {
                    my_set.swap(other_set);
                }
                for (auto busline : other_set) {
                    if (my_set.count(busline)) {
                        my_set.erase(busline);
                    } else {
                        my_set.insert(busline);
                    }
                }
            }
        }
        if (node != p && my_set.size() == 0) {
            ostringstream out;
            out << "Bus line missing between" << node + 1 << " and " << p + 1 << ".\n";
            wrong_answer(out.str());
        }
        return move(my_set);
    };
    dfs(0, 0, dfs);
    if (m < (leaves + 1) / 2) {
        judge_error("Judge failed to detect error in solution.\n");
    }
}

int main(int argc, char** argv) {
    if (argc < 4) exit(1);
    cin.sync_with_stdio(0);
    cin.tie(0);

    input_file = argv[1];
    answer_file = argv[2];
    output_dir = argv[3];

    ifstream fin(input_file);
    fin.exceptions(cin.failbit | cin.badbit | cin.eofbit);

    int n;
    fin >> n;

    vector<vector<int>> graph(n);
    for (int i = 0; i < n - 1; ++i) {
        int u,v;
        fin >> u >> v;
        --u;
        --v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    
    fin.close();

    try {
		score(cin, graph);
        accept();
    } catch(...) {
        wrong_answer("IO failure");
    }
}
