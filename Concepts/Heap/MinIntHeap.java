package Concepts.Heap;

import java.util.Arrays;

class Heap {
    public static void main(String[] args) {
        MinIntHeap heap = new MinIntHeap();
        heap.add(10);
        heap.add(5);
        heap.add(15);
        heap.add(1);
        heap.add(17);

        System.out.println(heap.peek()); // should be 1
        System.out.println(heap.poll()); // should be 1
        System.out.println(heap.poll()); // should be 5
        System.out.println(heap.poll()); // should be 10
        System.out.println(heap.poll()); // should be 15
        System.out.println(heap.poll()); // should be 17

    }
}

class MinIntHeap {
    private int capacity = 10;
    private int size = 0;

    private int[] items = new int[capacity];

    private int getLeftChildIndex(int index) {
        return index * 2 + 1;
    }

    private int getRightChildIndex(int index) {
        return index * 2 + 2;
    }

    private int getParentIndex(int index) {
        return (index - 1) / 2;
    }

    private boolean hasLeftChild(int index) {
        return getLeftChildIndex(index) < size;
    }

    private boolean hasRightChild(int index) {
        return getRightChildIndex(index) < size;
    }

    private boolean hasParent(int index) {
        return index != 0;
    }

    private int leftChild(int index) {
        return items[getLeftChildIndex(index)];
    }

    private int rightChild(int index) {
        return items[getRightChildIndex(index)];
    }

    private int parent(int index) {
        return items[getParentIndex(index)];
    }

    private void swap(int idx1, int idx2) {
        int temp = items[idx1];
        items[idx1] = items[idx2];
        items[idx2] = temp;
    }

    private void ensureCapacity() {
        if (size == capacity) {
            items = Arrays.copyOf(items, capacity * 2);
            capacity *= 2;
        }
    }

    public int peek() {
        if (size == 0)
            throw new IllegalStateException();
        return items[0];
    }

    public int poll() {
        if (size == 0)
            throw new IllegalStateException();
        int item = items[0];
        items[0] = items[size - 1];
        size--;
        heapifyDown();
        return item;
    }

    public void add(int item) {
        ensureCapacity();
        items[size] = item;
        size++;
        heapifyUp();
    }

    private void heapifyDown() {
        int index = 0;
        while (hasLeftChild(index)) {
            int smallerIndex = getLeftChildIndex(index);
            if (hasRightChild(index) && rightChild(index) < leftChild(index)) {
                smallerIndex = getRightChildIndex(index);
            }

            if (items[index] > items[smallerIndex]) {
                swap(index, smallerIndex);
                index = smallerIndex;
            } else {
                return;
            }
        }
    }

    private void heapifyUp() {
        int index = size - 1;
        while (hasParent(index) && items[index] < parent(index)) {
            swap(index, getParentIndex(index));
            index = getParentIndex(index);
        }
    }
}