// link - https://neetcode.io/problems/string-encode-and-decode

package Misc.Neetcode;

import java.util.ArrayList;
import java.util.List;

public class Encode_And_Decode_Strings {
    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();
        for (String str : strs) {
            encoded.append(str + "ö");
        }
        return encoded.toString();
    }

    public List<String> decode(String str) {
        List<String> list = new ArrayList<>();

        if (str.length() == 0) {
            return list;
        }

        if (str.length() == 1) {
            list.add("");
            return list;
        }

        String[] strs = str.split("ö");
        for (String s : strs) {
            list.add(s);
        }

        return list;
    }
}
