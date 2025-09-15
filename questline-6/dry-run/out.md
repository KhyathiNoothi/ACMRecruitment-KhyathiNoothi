# Dry Run of Pseudocode

## Pseudocode

```plaintext
A = 5
B = 3
SUM = 0
print("Initial: A =", A, ", B =", B, ", SUM =", SUM)
for i in range(1, B + 1):
    print(f"\nStep {i}:")
    print("Before: SUM =", SUM)
    SUM = SUM + A
    print(f"Operation: SUM = SUM + A -> {SUM}")
print("\nFinal Output:", SUM)

| Step | SUM before addition | Operation              | SUM after addition |
| ---- | ------------------- | ---------------------- | ------------------ |
| 0    | 0                   | Initialization         | 0                  |
| 1    | 0                   | SUM = SUM + A = 0 + 5  | 5                  |
| 2    | 5                   | SUM = SUM + A = 5 + 5  | 10                 |
| 3    | 10                  | SUM = SUM + A = 10 + 5 | 15                 |

