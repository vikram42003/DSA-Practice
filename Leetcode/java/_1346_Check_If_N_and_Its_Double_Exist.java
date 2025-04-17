import java.util.Arrays;

public class _1346_Check_If_N_and_Its_Double_Exist {
    public boolean checkIfExist(int[] arr) {
        Arrays.sort(arr);
        int zeroCount = 0;
        for (int num : arr) {
            if (num == 0) {
                zeroCount++;
                if (zeroCount == 2)
                    return true;
                continue;
            }
            if (Arrays.binarySearch(arr, num * 2) >= 0)
                return true;
        }
        return false;
    }
}
