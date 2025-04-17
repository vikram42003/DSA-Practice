// link - https://leetcode.com/problems/koko-eating-bananas/description/

public class _875_Koko_Eating_Bananas {
    public static void main(String[] args) {
        int[] piles = { 3, 6, 7, 11 }; // ans = 4
        int h = 8;

        int[] piles2 = { 30, 11, 23, 4, 20 }; // ans = 30
        int h2 = 5;

        System.out.println(minEatingSpeed(piles, h));
        System.out.println(minEatingSpeed(piles2, h2));
    }

    public static int minEatingSpeed(int[] piles, int h) {
        int l = 1, r = 1;
        for (int num: piles) {
            l = Math.min(l, num);
            r = Math.max(r, num);
        }

        if (piles.length == h) return r;

        while (l < r) {
            int speed = l + ((r - l) / 2);

            if (eatTheBananas(speed, piles, h)) {
                r = speed;
            } else {
                l = speed + 1;
            }
        }

        return l;
    }

    public static boolean eatTheBananas(int speed, int[] piles, int h) {
        for (int pile : piles) {
            h -= pile / speed;
            h -= pile % speed == 0 ? 0 : 1;
        }
        return h >= 0;
    }
}
