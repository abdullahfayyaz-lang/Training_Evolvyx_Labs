# Context Manager:An object which controls the environment seen in a with statement by defining __enter__() and __exit__() methods.


# Using 'with' automatically closes the file after the block ends
with open("data.txt", "w") as file:
    file.write("Hello, World!")

# No need to call file.close() manually



class MyContext:
    def __enter__(self):
        print("Entering the context...")
        return "Resource Ready"
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context...")
        if exc_type:
            print(f"An error occurred: {exc_value}")
        return True  # Suppress exception if True

# Using the context manager
with MyContext() as resource:
    print(resource)
    # Simulate an error
    raise ValueError("Something went wrong!")

print("Program continues...")
