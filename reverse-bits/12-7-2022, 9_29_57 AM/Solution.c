// https://leetcode.com/problems/reverse-bits

#define SINGLES_ODDS (0b10101010101010101010101010101010)
#define DOUBLES_ODDS (0b11001100110011001100110011001100)
#define NIBBLES_ODDS (0b11110000111100001111000011110000)
#define BYTES_ODDS   (0b11111111000000001111111100000000)
#define SHORTS_ODDS  (0b11111111111111110000000000000000)

uint32_t reverseBits(uint32_t n) {
    n = (((n & SINGLES_ODDS) >> 1) | ((n & (~SINGLES_ODDS)) << 1));
    n = (((n & DOUBLES_ODDS) >> 2) | ((n & (~DOUBLES_ODDS)) << 2));
    n = (((n & NIBBLES_ODDS) >> 4) | ((n & (~NIBBLES_ODDS)) << 4));
    n = (((n & BYTES_ODDS) >> 8) | ((n & (~BYTES_ODDS)) << 8));
    return ((n >> 16) | (n << 16));
}