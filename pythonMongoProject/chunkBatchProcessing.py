import os
import threading

def process_chunk(chunk, incomplete_message):
    # Split the chunk into lines
    lines = (incomplete_message + chunk).split('\n')
    # Process each complete message
    for message in lines[:-1]:
        print("Processing message:", message)
    # Store the last incomplete message for the next chunk
    incomplete_message = lines[-1]
    return incomplete_message

def process_large_file(file_path, num_threads=4, chunk_size=4096):
    with open(file_path, 'r') as file:
        incomplete_messages = [''] * num_threads
        threads = []

        while True:
            chunks = [file.read(chunk_size) for _ in range(num_threads)]
            if not any(chunks):  # End of file
                break
            for i in range(num_threads):
                thread = threading.Thread(target=process_chunk, args=(chunks[i], incomplete_messages[i]))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

if __name__ == "__main__":
    file_path = "/path/to/large/file"
    process_large_file(file_path)
