// https://leetcode.com/problems/palindrome-number



int reverse(int x){
    int reverse = 0;
    while (x != 0)
    {
        reverse = (long)reverse*10 + x % 10;
        x /=10;
    }
    return reverse;
}

int isPalindrome(int x){
    
    int y = reverse (x);
    return y == x && x >= 0;
}