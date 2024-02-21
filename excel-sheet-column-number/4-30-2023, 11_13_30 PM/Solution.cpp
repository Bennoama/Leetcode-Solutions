// https://leetcode.com/problems/excel-sheet-column-number


int LetterToNum(char c){
    static int lut[] =
    {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26};
    return lut[c - 'A'];

}

class Solution {
public:
    int titleToNumber(string columnTitle) {
        int sum = 0;
        int iteration = 0;
        long length = columnTitle.length();
        for (long i = length - 1; i >= 0; --i){
            sum += LetterToNum(columnTitle[i]) * pow(26, iteration);
            ++iteration;
        }
        return sum;
    }
};