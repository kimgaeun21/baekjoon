#include <iostream>
#include <cmath>
using namespace std;

int n, r, c;
int x, y;
int ans=0;
//z=칸의 개수
void find(int x, int y, int z) {
	if (x == r && y == c) {
		cout << ans << "\n";
		return;
	}
	if (z == 1) {
		ans += 1;
		return;
	}
	if (!(x <= r&&r<x+z&&y<= c&&c < y+z)) {
		ans += pow(z,2);
		return;
	}
	
	find(x, y, z / 2);
	find(x, y + z / 2, z / 2);
	find(x + z / 2, y, z / 2);
	find(x + z/ 2, y + z / 2, z / 2);
}
int main() {
	cin >> n >> r >> c;
	find(0, 0, pow(2, n));
	return 0;
}