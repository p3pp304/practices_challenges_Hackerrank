# Find the Smallest Missing Positive Integer

## 📝 Problem Description
Given an unsorted array of integers, the objective is to find the smallest positive integer (≥ 1) that is not present in the array. The solution must execute in **O(n)** time and use **O(1)** extra space.

## 💡 Example
**Input:** `orderNumbers = [3, 4, -1, 1]`

**Output:** `2`

**Explanation:**
We want to find the smallest positive missing integer by placing each value at its correct index (i.e., value `1` at index `0`, value `2` at index `1`, etc.).
* Start with `[3, 4, -1, 1]`
* `i=0`: value `3` ⇒ swap with index `2` ⇒ `[-1, 4, 3, 1]`
* `i=0`: value `-1` is out of range (ignore)
* `i=1`: value `4` ⇒ swap with index `3` ⇒ `[-1, 1, 3, 4]`
* `i=1`: value `1` ⇒ swap with index `0` ⇒ `[1, -1, 3, 4]`
* Now `1` is at index `0`, `3` at index `2`, `4` at index `3`. `-1` remains at index `1`.

Scanning from index `0` using our variable **x**:
* **x** = 0: index `0` has `1` (correct).
* **x** = 1: index `1` has `-1` (incorrect, we expect `2`).
⇒ The missing positive integer is `2`.

---

## ⚙️ Specifications

### Input Format
1. An integer `n` on the first line, where `0 ≤ n ≤ 1000`.
2. The next `n` lines contain an integer representing `orderNumbers[i]`.

### Constraints
* `0 <= orderNumbers.length <= 1000`
* `-10^9 <= orderNumbers[i] <= 10^9` for all `0 <= i < orderNumbers.length`
* Duplicates are allowed.
* Negative numbers and zero are allowed.

### Output Format
* A single integer denoting the smallest positive order number (≥ 1) that does not appear in the input array.

---

## 🧠 Approach & Optimization (Cyclic Sort)
To achieve the strict **O(n)** time and **O(1)** space constraints, standard sorting (**O(n log n)**) or using a Hash Set (which takes **O(n)** space) are not acceptable. 

The optimal approach is the **Cyclic Sort** pattern:
1. Iterate through the array. If an element is a positive integer smaller than or equal to the array's length, swap it to its "correct" position (e.g., the number `5` goes to index `4`).