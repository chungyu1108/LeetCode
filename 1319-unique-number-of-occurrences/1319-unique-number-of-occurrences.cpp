class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> countMap;  
        
        for (int num : arr) {
            countMap[num]++;
        }
        
        unordered_set<int> occurrences;  
        
        for (auto it : countMap) {
            if (occurrences.find(it.second) != occurrences.end()) {
                return false;
            }
            occurrences.insert(it.second); 
        }
        
        return true;
    }
};
