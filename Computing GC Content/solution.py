def solve_gc_content():
    try:
        with open('rosalind_gc.txt', 'r') as f:
            content = f.read().strip()
            
        records = content.split('>')[1:]

        highest_id = ""
        highest_gc = -1.0

        for record in records:
            lines = record.splitlines()
            id_name = lines[0]
            sequence = "".join(lines[1:])

            g_count = sequence.count('G')
            c_count = sequence.count('C')
            total_len = len(sequence)
            
            gc_percentage = ((g_count + c_count) / total_len) * 100

            if gc_percentage > highest_gc:
                highest_gc = gc_percentage
                highest_id = id_name

        print(highest_id)
        print(f"{highest_gc:.6f}")

    except FileNotFoundError:
        print("Error: 'rosalind_gc.txt' not found.")


solve_gc_content()
