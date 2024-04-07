function sortByBits(arr: number[]): number[] {
    const sorted:number[] = arr.slice();
    sorted.sort((a:number, b:number) => {
        const aCount = bitCount(a);
        const bCount = bitCount(b);
        if (aCount === bCount) return a - b;
        return aCount - bCount;
    })
    return sorted;
};

function bitCount (n) {
  n = n - ((n >> 1) & 0x55555555)
  n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
  return ((n + (n >> 4) & 0xF0F0F0F) * 0x1010101) >> 24
}
