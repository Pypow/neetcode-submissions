public class Solution {
    public int HammingWeight(uint n) {
        int res = 0;

        while (n != 0) {
            if (n % 2 != 0) {
                res += 1;
            }
            n = n >> 1;
        }
        return res;
    }
}
