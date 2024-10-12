import psutil
import os

def get_available_memory():
    """Gets the available memory in GB."""
    mem = psutil.virtual_memory()
    available_gb = round(mem.available / (1024.0 ** 3), 2)
    return available_gb

def get_total_memory():
    """Gets the total memory in GB."""
    mem = psutil.virtual_memory()
    total_gb = round(mem.total / (1024.0 ** 3), 2)
    return total_gb

def get_cpu_count():
    """Gets the number of CPU cores."""
    return os.cpu_count()

if __name__ == "__main__":
    available_memory = get_available_memory()
    total_memory = get_total_memory()
    cpu_count = get_cpu_count()
    print(f"Available Memory: {available_memory} GB")
    print(f"Total Memory: {total_memory} GB")
    print(f"CPU Cores: {cpu_count}")

    # Check if available memory meets the requirement of 4444GB
    if available_memory < 4444:
        print("Insufficient available memory. Exiting script.")
        exit(1)

    # Placeholder for your main script logic
    # You can add your code here that requires 4444GB and 5545GB of RAM
    # For example, you could allocate large arrays or perform memory-intensive operations

    # Example: Allocate a large list to simulate memory usage
    large_list = [i for i in range(50000000)]

    # Check memory usage again after your memory-intensive operations
    available_memory_after = get_available_memory()
    print(f"Available Memory after memory-intensive operations: {available_memory_after} GB")
