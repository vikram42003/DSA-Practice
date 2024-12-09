class Roof_Top {
    // Function to find maximum number of consecutive steps
    // to gain an increase in altitude with each step.
    public int maxStep(int arr[]) {
        int steps = 0, maxSteps = 0;

        for (int i = 1; i < arr.length; i++) {
            if (arr[i - 1] < arr[i]) {
                steps++;
                maxSteps = Math.max(maxSteps, steps);
            } else {
                steps = 0;
            }
        }

        return maxSteps;
    }
}