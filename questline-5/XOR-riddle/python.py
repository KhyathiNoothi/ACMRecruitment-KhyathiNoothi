# Given values
xor_with = 23
result = 45

# Calculate the secret number N
N = xor_with ^ result

print(f"The secret number N is: {N}")

# Verify the XOR operation
verification = N ^ xor_with
print(f"Verification: {N} XOR {xor_with} = {verification}")
