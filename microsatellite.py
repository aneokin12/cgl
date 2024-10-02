def microsatellite_compression(sequence: str) -> str:
    compressed = []
    i = 0  # Start index

    while i < len(sequence) - 1:
        pair = sequence[i:i+2]  # Get the current pair of nucleotides
        
        # If this is the first pair or it doesn't match the previous one
        if len(compressed) == 0 or sequence[i:i+2] != sequence[i-2:i]:
            compressed.append(pair[0])  # Add only the first character of the current pair
            i += 1  # Move to the next overlapping pair
        else:
            # If the current pair matches the last one, skip the entire pair
            i += 2
    
    # Add the last character if we have an odd-length sequence
    if i == len(sequence) - 1:
        compressed.append(sequence[-1])
    
    # Join the list back into a string and return the result
    return ''.join(compressed)

# Example usage:
sequence = "TATATACCTCTAGGACCGCGCATATAC"
compressed_sequence = microsatellite_compression(sequence)
print(compressed_sequence)
