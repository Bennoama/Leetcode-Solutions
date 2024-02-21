// https://leetcode.com/problems/guess-number-higher-or-lower

/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        long currGuess = n / 2;
        long lowerLimit = 0;
        long upperLimit = n;
        long status = 0;
        while (0 != (status = guess(currGuess))) {
            if (status == -1){
                upperLimit = currGuess;
                currGuess = (lowerLimit + currGuess) / 2;
            }
            else {
                lowerLimit = currGuess;
                currGuess = (upperLimit + currGuess) / 2 + 1;
            }
        }
        return currGuess;
    }

};