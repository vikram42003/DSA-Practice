import java.util.Arrays;

public class _706_Design_HashMap {
    // Basic Implementation
    // I have done a more comprehensive implementation in github.com/vikram42003 ->
    // DSA-Workspace repo -> Concepts/HashMap/MyHashMap.java
    // So refer to that if youre revisiting this

    class MyHashMap {
        int[] map;

        public MyHashMap() {
            this.map = new int[1000001];
            Arrays.fill(this.map, -1);
        }

        public void put(int key, int value) {
            this.map[key] = value;
        }

        public int get(int key) {
            return this.map[key];
        }

        public void remove(int key) {
            this.map[key] = -1;
        }
    }

    /**
     * Your MyHashMap object will be instantiated and called as such:
     * MyHashMap obj = new MyHashMap();
     * obj.put(key,value);
     * int param_2 = obj.get(key);
     * obj.remove(key);
     */
}
