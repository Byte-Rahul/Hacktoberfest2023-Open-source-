// C++ implementation of program
#include <bits/stdc++.h>
using namespace std;

// Check if a particular string is
// sorted or not
bool sorted(string s)
{

	for (int i = 0; i < s.size() - 1; i++) {
		if (s[i] > s[i + 1])
			return false;
	}
	return 1;
}

// Function to find the required
// number of pairs
int solve(string S[], int N)
{

	// Boolean array mark to consider only
	// those strings which are sorted and
	// reject those which are not sorted
	bool mark[N + 1] = { 0 };

	for (int i = 0; i < N; i++) {
		if (sorted(S[i])) {
			mark[i] = 1;
		}
	}
	// For every lower_case alphabet find out
	// how many strings start with that
	// particular alphabet
	int nums[26] = { 0 };

	for (int i = 0; i < N; i++) {

		if (mark[i] == 1) {
			int p = S[i][0] - 'a';
			nums[p] += 1;
		}
	}

	// Compute the answer for all
	// the sorted strings
	int ans = 0;
	for (int i = 0; i < N; i++) {
		if (mark[i] == 1) {
			int len = S[i].size();
			int last_char = S[i][len - 1] - 'a';

			for (int j = last_char; j < 26; j++) {
				ans += nums[j];
			}
		}
	}

	// Return the answer
	return ans;
}

// Driver Code
int main()
{

	// Test case 1
	string S[] = { "ac", "df", "pzz" };
	int N = sizeof(S) / sizeof(S[0]);

	// Function call
	cout << solve(S, N) << endl;

	// Test case 2
	string S2[] = { "pqrs", "amq", "bcd" };
	N = sizeof(S2) / sizeof(S2[0]);

	// Function call
	cout << solve(S2, N) << endl;
	return 0;
}
