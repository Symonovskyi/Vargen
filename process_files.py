import concurrent.futures
from text_variations import generate_text_variations

def process_text_variations(append: bool = False,
                            separator: str = '',
                            input_filename: str = 'vargen_source_text.txt',
                            output_filename: str = 'vargen_result_text.txt',
                            batch_size: int = 10) -> None:
    """
    Processes text variations from a given input file and writes the variations to an output file.
    
    This function reads lines from the input file, generates variations for each line using the
    generate_text_variations function, and writes the variations to the output file. Variations are
    written in batches to reduce the frequency of write operations. A separator can be inserted
    between each batch of variations if specified.
    
    Parameters:
    -----------
    append : bool, optional
        If True, appends the generated text variations to the output file if it exists.
        If False, overwrites the existing file. Default is False.
        
    separator : str, optional
        A string to be used as a separator between each batch of text variations in the output file.
        Default is an empty string, meaning no separator is used.
        
    input_filename : str, optional
        The path to the input file containing the base texts for generating variations.
        Default is 'vargen_source_text.txt'.
        
    output_filename : str, optional
        The path to the output file where the text variations will be written.
        Default is 'vargen_result_text.txt'.
        
    batch_size : int, optional
        The number of text variations to accumulate before writing to the output file.
        Default is 10.
    
    Returns:
    --------
    None
    
    Overview:
    ---------
    The function uses a ThreadPoolExecutor for concurrent processing of text variations to improve
    performance. It leverages the batch_size parameter to control memory usage and the frequency of
    write operations to the output file.
    
    Examples:
    ---------
    Process text variations with default parameters:
        process_text_variations()
    
    Process text variations with custom settings:
        process_text_variations(append=True, separator='---', input_filename='custom_input.txt',
                                output_filename='custom_output.txt', batch_size=20)
    
    Notes:
    ------
    - The function is designed to be efficient with resource usage, using threads for parallel processing
      and batching write operations to minimize disk I/O.
    - Ensure the input file exists and is readable, and that the output file is writable.
    """

    # Initialize an empty list to hold the text lines from the input file.
    texts = []
    
    # Open the input file and read all lines into the 'texts' list.
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        texts = input_file.read().splitlines()

    # Determine the file mode based on whether the user wants to append to the file.
    file_mode = 'a' if append else 'w'
    
    # Open the output file and set up a ThreadPoolExecutor for concurrent processing.
    with open(output_filename, file_mode, encoding='utf-8') as output_file, concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks to the executor for each line of text to generate variations.
        futures = [executor.submit(generate_text_variations, text) for text in texts]
        
        # Initialize an empty list to accumulate results for batch processing.
        results_batch = []
        
        # Wait for futures to complete and process their results.
        for future in concurrent.futures.as_completed(futures):
            # Extend the results batch with the generated variations from each future.
            results_batch.extend(future.result())
            
            # Check if the current batch size meets the threshold for writing to the file.
            if len(results_batch) >= batch_size:
                # Write each variation in the batch to the output file.
                for variation in results_batch:
                    output_file.write(variation + '\n')
                
                # Write the separator to the file if specified.
                if separator:
                    output_file.write(separator + '\n')
                
                # Clear the results batch to start accumulating the next batch.
                results_batch = []

        # After processing all futures, check for any remaining variations in the batch.
        for variation in results_batch:
            output_file.write(variation + '\n')

        # If there are remaining variations and a separator is specified, write it to the file.
        if separator and results_batch:
            output_file.write(separator + '\n')
