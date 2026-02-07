def solve_gc_content():
    try:
        # 1. Read the file
        with open('rosalind_gc.txt', 'r') as f:
            content = f.read().strip()

        # 2. Split into individual records (starting with '>')
        # We skip the first empty element created by split
        records = content.split('>')[1:]

        highest_id = ""
        highest_gc = -1.0

        for record in records:
            # Split ID from the sequence
            lines = record.splitlines()
            id_name = lines[0]
            # Join the rest of the lines (sequence might be on multiple lines)
            sequence = "".join(lines[1:])

            # 3. Calculate GC content
            g_count = sequence.count('G')
            c_count = sequence.count('C')
            total_len = len(sequence)
            
            gc_percentage = ((g_count + c_count) / total_len) * 100

            # 4. Keep track of the maximum
            if gc_percentage > highest_gc:
                highest_gc = gc_percentage
                highest_id = id_name

        # 5. Output the result
        print(highest_id)
        # Rosalind requires 6 decimal places of precision
        print(f"{highest_gc:.6f}")

    except FileNotFoundError:
        print("Error: 'rosalind_gc.txt' not found.")

solve_gc_content()