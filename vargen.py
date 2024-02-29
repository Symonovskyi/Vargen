from process_files import process_text_variations

def generate_variations(append: bool = None, separator: str = None, input_filename: str = None, output_filename: str = None) -> None:
    """
    Orchestrates the text variation generation process by configuring and executing the
    process_text_variations function with user-specified or default parameters.
    
    Parameters:
    -----------
    append : bool, optional
        Determines whether the output should be appended to the file if it exists.
        If True, appends to the file. If False or None, overwrites the file.
        Default is None, which leads to overwriting.
        
    separator : str, optional
        A string to be used as a separator between different sets of variations in the output file.
        If None or an empty string is provided, no separator is used.
        
    input_filename : str, optional
        The name (and path) of the input file containing the base texts for variation generation.
        Defaults to 'vargen_source_text.txt' if not provided.
        
    output_filename : str, optional
        The name (and path) of the output file where the text variations will be saved.
        Defaults to 'vargen_result_text.txt' if not provided.
        
    Returns:
    --------
    None

    Overview:
    ---------
    This function primarily serves as an entry point to execute the text variations generation process.
    It parses command-line arguments to configure the process settings, including whether to append
    to the output file, what separator to use between variation sets, and the input/output file names.
    It then delegates the execution to process_text_variations function with the configured settings.
    
    Examples:
    ---------
    Consider you have a file named 'vargen_source_text.txt' with the following content:
        "Good [[morning|evening], [John|Jane]| day]!"

    Using the `generate_variations` function with default parameters:
        generate_variations()
    This will process the text variations from 'vargen_source_text.txt' and write the resulting variations into 'vargen_result_text.txt'. The output file will contain:
        Good morning, John!
        Good morning, Jane!
        Good evening, John!
        Good evening, Jane!
        Good day!

    If you want to append the results to the existing output file and use a custom separator '-----':
        generate_variations(append=True, separator='-----')
    Assuming 'vargen_result_text.txt' initially contains some text, the new variations will be appended to the end of this file, separated by '-----' from the previously existing content.

    To specify custom input and output files:
        generate_variations(input_filename='custom_input.txt', output_filename='custom_output.txt')
    This will read the base texts from 'custom_input.txt', generate variations, and save them to 'custom_output.txt', overwriting any existing content in 'custom_output.txt'.

    Console Usage:
    --------------
    This script can be executed from the console (command line) and allows for configuration via command-line arguments. Below are examples of how to run the script from the console with different configurations.

    1. Running the script with default settings (overwrites 'vargen_result_text.txt' using 'vargen_source_text.txt' as input):
        $ python vargen.py
    2. Appending results to the output file and specifying a separator:
        $ python vargen.py append=true separator="-----"
    This command appends generated text variations to 'vargen_result_text.txt', separated by "-----" from any existing content.
    3. Specifying custom input and output files:
        $ python vargen.py input_filename="custom_input.txt" output_filename="custom_output.txt"
    This command reads from 'custom_input.txt', generates text variations, and writes the results to 'custom_output.txt', overwriting it.
    4. Combining all available options:
        $ python vargen.py append=true separator="-----" input_filename="custom_input.txt" output_filename="custom_output.txt"
    This command reads from 'custom_input.txt', appends generated variations to 'custom_output.txt' with "-----" as a separator between existing content and new variations.
    5. Running the script with the first positional argument to enable the performance analysis (display execution time):
        $ python vargen.py true
    This command runs the script with default settings and displays the execution time upon completion.
    6. Specifying whether to append to the output file and use a separator, without custom file names:
        $ python vargen.py true true "-----"
    This command enables performance analysis, appends the generated variations to the default output file ('vargen_result_text.txt'), and uses "-----" as a separator.
    7. Fully specifying all options with positional arguments:
        $ python vargen.py true true "-----" custom_input.txt custom_output.txt
    This command enables performance analysis, appends the generated text variations to 'custom_output.txt', uses "-----" as a separator, and reads the base texts from 'custom_input.txt'.


    Notes:
    ------
    - Ensure Python and all required dependencies are installed in your environment.
    - The script can be configured via command-line arguments, either as key-value pairs (e.g., `append=true`) or positional arguments.
    - Boolean values for parameters like 'append' should be in lowercase (`true` or `false`).
    - Default values are used for any unspecified parameters.
    - The first positional argument enables or disables performance analysis (execution time display).
    - The second positional argument controls the append mode.
    - The third positional argument defines a separator for the output file.
    - The fourth and fifth positional arguments specify custom input and output filenames, respectively.
    - Ensure the input file exists and is accessible, and note that the output file will be created or modified as per the 'append' setting.

    Important: When using positional arguments, maintaining the correct order is crucial for the script to operate as intended.

    """

    # Conditional assignments for each parameter based on user input
    kwargs = {}
    if append is not None:
        kwargs['append'] = append
    if separator is not None:
        kwargs['separator'] = separator
    if input_filename is not None:
        kwargs['input_filename'] = input_filename
    if output_filename is not None:
        kwargs['output_filename'] = output_filename

    # Execute the text processing with the specified or default parameters
    process_text_variations(**kwargs)

if __name__ == '__main__':
    import sys
    import time

    # Initialize variables for command-line arguments
    analyze_speed = None
    append = None
    separator = None
    input_filename = None
    output_filename = None

    # Parse key-value pair arguments from the command line
    key_value_args = [arg for arg in sys.argv[1:] if '=' in arg]
    for arg in key_value_args:
        key, value = arg.split('=', 1)
        # Assign values based on the key
        if key == 'analyze_speed':
            analyze_speed = value.lower() == 'true'
        elif key == 'append':
            append = value.lower() in ['true', 'append']
        elif key == 'separator':
            separator = value
        elif key == 'input_filename':
            input_filename = value
        elif key == 'output_filename':
            output_filename = value

    # If key-value pair arguments are absent, parse positional arguments
    positional_args = [arg for arg in sys.argv[1:] if '=' not in arg]
    if analyze_speed is None and len(positional_args) > 0:
        analyze_speed = positional_args[0].lower() == 'true'
    if append is None and len(positional_args) > 1:
        append = positional_args[1].lower() in ['true', 'append']
    if separator is None and len(positional_args) > 2:
        separator = positional_args[2]
    if input_filename is None and len(positional_args) > 3:
        input_filename = positional_args[3]
    if output_filename is None and len(positional_args) > 4:
        output_filename = positional_args[4]

    # Optional: Analyze execution speed if specified
    if analyze_speed:
        start_time = time.time()

    # Execute the generate_variations function with parsed arguments
    generate_variations(append, separator, input_filename, output_filename)

    # Calculate and print execution time if speed analysis is enabled
    if analyze_speed:
        print(f"Execution time: {time.time() - start_time} seconds")
