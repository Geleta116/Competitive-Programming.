#include <iostream>
#include <vector>

using namespace std;

class TrieNode {
public:
    TrieNode* children[2];

    TrieNode() {
        children[0] = nullptr;
        children[1] = nullptr;
    }
};

class Trie {
public:
    TrieNode* root;

    Trie() {
        root = new TrieNode();
    }

    void add(int num) {
        string bits = bitset<32>(num).to_string();
        TrieNode* curr = root;

        for (char b : bits) {
            int index = b - '0';

            if (curr->children[index] == nullptr) {
                curr->children[index] = new TrieNode();
            }

            curr = curr->children[index];
        }
    }

    int maxSum(int num1) {
        string bits = bitset<32>(num1).to_string();
        TrieNode* curr = root;
        string sb = "";

        for (char b : bits) {
            int oppositeIndex = (b - '0') ^ 1; // Flipping the bit

            if (curr->children[oppositeIndex] != nullptr) {
                curr = curr->children[oppositeIndex];
                sb += to_string(oppositeIndex);
            } else {
                curr = curr->children[b - '0'];
                sb += to_string(oppositeIndex ^ 1);
            }
        }

        int num2 = stoi(sb, 0, 2);

        return num1 ^ num2;
    }
};


class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        Trie trie;
        int maximum = 0;

        for (int num : nums) {
            trie.add(num);
            int res = trie.maxSum(num);
            maximum = max(res, maximum);
        }

        return maximum;
        
    }
};