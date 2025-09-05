# Bridge and Torch Optimization

## 🧠 Problem Summary

Four people need to cross a bridge at night with one torch:

- Person A: 1 minute
- Person B: 2 minutes
- Person C: 7 minutes
- Person D: 10 minutes

Rules:
- Max two people can cross at once.
- They need the torch to cross.
- When two cross together, they walk at the pace of the slower one.
- Someone must bring the torch back each time until all have crossed.

## 🎯 Goal

Minimize the total time required for all four people to cross.

---

## ✅ Optimal Sequence & Reasoning

### Step-by-step Plan:

1. **A and B cross** → 2 minutes  
   (Fastest two cross first)

2. **A returns** → 1 minute  
   (Fastest person brings torch back)

3. **C and D cross** → 10 minutes  
   (Two slowest cross together)

4. **B returns** → 2 minutes  
   (Second fastest brings torch back)

5. **A and B cross again** → 2 minutes  
   (Fastest two cross together again)

---

### ⏱ Total Time:

2 (A & B) + 1 (A back) + 10 (C & D) + 2 (B back) + 2 (A & B again) = 17 minutes
