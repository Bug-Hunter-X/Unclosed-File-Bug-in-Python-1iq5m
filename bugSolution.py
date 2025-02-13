def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # ... some code that processes the file ... 
            contents = f.read()
            return contents
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None