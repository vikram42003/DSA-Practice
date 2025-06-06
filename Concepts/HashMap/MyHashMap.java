package Concepts.HashMap;

// Problem Statement

// Design and implement a generic HashMap<K, V> class from scratch, supporting the following operations:
// `
// void put(K key, V value);
// V get(K key);
// V remove(K key);
// boolean containsKey(K key);
// int size();
// `
// Your HashMap must use separate chaining for collision resolution and support automatic resizing when the load factor
// exceeds 0.75. It should not use any Java built-in collection classes like HashMap, LinkedHashMap, HashSet, TreeMap, etc., 
// but you can use arrays or create your own LinkedList class if needed.
// You must use the hashCode() and equals() methods on keys properly to allow support for arbitrary objects.

// Constraints
// - The initial capacity is 16.
// - Load factor threshold = 0.75 → resize to double capacity when exceeded.
// - Keys can be null or any Object.
// - Must handle collisions correctly.
// - You must not use java.util.* (besides perhaps Arrays or Objects for null checks).
// - null keys are allowed and should be handled separately.

class HashMap {
    public static void main(String[] args) {
        MyHashMap<String, Integer> map = new MyHashMap<>();
        map.put("apple", 5);
        // map.put("banana", 10);
        // map.put("orange", 7);

        // System.out.println(map.get("apple")); // 5
        // System.out.println(map.get("grape")); // null
        // System.out.println(map.containsKey("banana")); // true
        // System.out.println(map.size()); // 3

        // map.put("apple", 99); // Update value
        // System.out.println(map.get("apple")); // 99

        // System.out.println(map.remove("orange")); // 7
        // System.out.println(map.get("orange")); // null
        // System.out.println(map.size()); // 2

    }
}

class LinkedList<K, V> {
    K key;
    V value;
    LinkedList<K, V> next;

    public LinkedList(K key, V value) {
        this.key = key;
        this.value = value;
        this.next = null;
    }
}

class MyHashMap<K, V> {
    private LinkedList<K, V>[] map;
    private V nullVal;
    private boolean isThereANullKey;
    private int curSize;

    @SuppressWarnings("unchecked")
    MyHashMap() {
        this.map = new LinkedList[16];
        this.curSize = 0;
    }

    public void put(K key, V value) {
        if (key == null) {
            insertNullKey(value);
            return;
        }

        int hash = key.hashCode();
        hash = hash < 0 ? -hash : hash;

        int index = hash % map.length;
        this.insert(index, key, value);
    }

    public V get(K key) {
        if (key == null) {
            return this.nullVal;
        }

        int hash = key.hashCode();
        hash = hash < 0 ? -hash : hash;
        int index = hash % this.map.length;

        LinkedList<K, V> curr = this.map[index];

        while (curr != null) {
            if (curr.key.equals(key)) {
                return curr.value;
            }
            curr = curr.next;
        }

        return null;
    }

    public V remove(K key) {
        if (key == null) {
            if (this.isThereANullKey) {
                V toReturn = this.nullVal;
                this.isThereANullKey = false;
                this.curSize--;
                return toReturn;
            }
            return null;
        }

        int hash = key.hashCode();
        hash = hash < 0 ? -hash : hash;
        int index = hash % this.map.length;

        LinkedList<K, V> curr = this.map[index];
        LinkedList<K, V> prev = null;

        while (curr != null) {
            if (curr.key.equals(key)) {
                V toReturn = curr.value;
                if (prev == null) {
                    this.map[index] = curr.next;
                } else {
                    prev.next = curr.next;
                }
                this.curSize--;
                return toReturn;
            }
            prev = curr;
            curr = curr.next;
        }

        return null;
    }

    public boolean containsKey(K key) {
        if (key == null) {
            return isThereANullKey;
        }

        int hash = key.hashCode();
        hash = hash < 0 ? -hash : hash;
        int index = hash % this.map.length;

        LinkedList<K, V> curr = this.map[index];

        while (curr != null) {
            if (curr.key.equals(key)) {
                return true;
            }
            curr = curr.next;
        }

        return false;
    }

    public int size() {
        return this.curSize;
    }

    private void insertNullKey(V value) {
        if (!isThereANullKey) {
            curSize++;
            isThereANullKey = true;
        }
        nullVal = value;
    }

    private void insert(int index, K key, V value) {
        LinkedList<K, V> curr = this.map[index];

        while (curr != null) {
            if (curr.key.equals(key)) {
                curr.value = value;
                return;
            }
            curr = curr.next;
        }

        LinkedList<K, V> newHead = new LinkedList<>(key, value);
        newHead.next = this.map[index];
        this.map[index] = newHead;

        curSize++;
        if (curSize > map.length * 0.75) {
            this.resize();
        }
    }

    @SuppressWarnings("unchecked")
    private void resize() {
        LinkedList<K, V>[] oldList = this.map;

        LinkedList<K, V>[] newList = new LinkedList[this.map.length * 2];

        this.map = newList;
        this.curSize = isThereANullKey ? 1 : 0;

        for (LinkedList<K, V> l : oldList) {
            while (l != null) {
                int hash = l.key.hashCode();
                hash = hash < 0 ? -hash : hash;
                int index = hash % newList.length;

                this.insert(index, l.key, l.value);
                l = l.next;
            }
        }
    }
}
