def rotate_binary_string(binary_str: str, k: int) -> int:
    
    if not binary_str or not all(c in '01' for c in binary_str):
        raise ValueError("Input must be a valid binary string.")

    n = len(binary_str)
    k = k % n  

    
    rotated = binary_str[-k:] + binary_str[:-k]

    
    return int(rotated, 2)


if __name__ == "__main__":
    print(rotate_binary_string("1011", 1))  
    print(rotate_binary_string("0001", 2))  
    print(rotate_binary_string("1111", 4))  
