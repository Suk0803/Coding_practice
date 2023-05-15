#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using ld = long double;
const ld EPS = 1e-7;
struct Line {
    ld m, b, x;
    int idx;
    Line() {};
    Line(ld _m, ld _b, ld _x, int _idx) : m(_m), b(_b), x(_x), idx(_idx) {};
    bool operator<(Line& rhs) {
        if (abs(m - rhs.m) < EPS) return b < rhs.b;
        return m > rhs.m;
    }
};

ld minX, maxX;
int N, M;
vector<Line> lines;
vector<pair<ld, int>> queries;
vector<Line> cht;
int ptr;

ld intersect(Line& a, Line& b) {
    return (b.b - a.b) / (a.m - b.m);
}

void addLine(Line& a) {
    if (cht.empty()) {
        cht.push_back(a);
        return;
    }
    while (!cht.empty()) {
        Line top = cht.back();
        if (abs(top.m - a.m) < EPS && top.b < a.b) return;
        if (abs(top.m - a.m) < EPS) cht.pop_back();
        else {
            ld x = intersect(top, a);
            if (x <= top.x) cht.pop_back();
            else break;
        }
    }
    if (cht.empty()) cht.push_back(a);
    else {
        a.x = intersect(cht.back(), a);
        cht.push_back(a);
    }
    if (ptr >= cht.size()) ptr = cht.size() - 1;
    return;
}

int query(ld x) {
    while (ptr < cht.size() - 1 && cht[ptr + 1].x < x + EPS) ++ptr;
    return cht[ptr].idx;
}

int main() {
    cin.tie(nullptr); ios::sync_with_stdio(false);
    cin >> maxX >> minX;
    cin >> N;
    ld dx = maxX - minX;
    for (int i = 0; i < N; ++i) {
        ld upY, lowY;
        cin >> upY >> lowY;
        ld dy = upY - lowY;
        ld m = dy / dx;
        ld b = lowY - m * minX;
        lines.push_back(Line(m, b, minX, i + 1));
    }
    cin >> M;
    for (int i = 0; i < M; ++i) {
        ld x; cin >> x;
        queries.push_back(make_pair(x, i));
    }
    sort(lines.begin(), lines.end());
    sort(queries.begin(), queries.end());
    vector<int> ans(M);
    for (int i = 0; i < N; ++i) addLine(lines[i]);
    for (int i = 0; i < M; ++i) ans[queries[i].second] = query(queries[i].first);
    for (int i = 0; i < M; ++i) cout << ans[i] << '\n';
    return 0;
}