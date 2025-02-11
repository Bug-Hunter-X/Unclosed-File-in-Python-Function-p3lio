def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # ... some code that processes the file ...
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")    