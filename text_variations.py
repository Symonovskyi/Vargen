import re

def generate_text_variations(text: str) -> list:
    """
    Generates all possible text variations based on the options provided within brackets.

    Parameters:
    -----------
    text : str
        The input text containing bracketed options from which to generate variations.

    Returns:
    --------
    list
        A list of all possible text variations generated from the input text.

    Overview:
    ---------
    This function identifies all bracketed sections within the input text and generates
    every possible combination of text variations based on the options provided within
    those brackets. It handles nested bracketed options by recursively generating variations
    for each level of nesting.

    Examples:
    ---------
    >>> generate_text_variations("Hello [World|Universe]!")
    ['Hello World!', 'Hello Universe!']

    >>> generate_text_variations("Good [[morning|evening], [John|Jane]| day]!")
    ['Good morning, John!', 'Good morning, Jane!', 'Good evening, John!', 'Good evening, Jane!', 'Good day!']

    Notes:
    ------
    - The function supports multiple levels of nested brackets, allowing for complex combinations
      of text variations.
    - Options within brackets are separated by '|', and each option can contain further nested
      brackets for additional variations.
    """

    def find_matching_bracket(text: str, start_index: int) -> int:
        """
        Finds the index of the matching closing bracket for an opening bracket in a string.

        Parameters:
        -----------
        text : str
            The string containing brackets to be matched.
        start_index : int
            The index of the opening bracket for which the matching closing bracket is sought.

        Returns:
        --------
        int
            The index of the matching closing bracket, or -1 if no matching bracket is found.

        Overview:
        ---------
        This function iterates through the string starting from the index immediately after
        the opening bracket, tracking the level of nested brackets, and returns the index
        of the closing bracket that matches the opening bracket at start_index.

        Examples:
        ---------
        >>> find_matching_bracket("Example [text with [nested] brackets]", 8)
        36
        """
        # Initialize depth to account for nested brackets
        depth = 1
        for i in range(start_index + 1, len(text)):
            if text[i] == '[':
                depth += 1
            elif text[i] == ']':
                depth -= 1
                if depth == 0:
                    return i  # Matching closing bracket found
        return -1  # No matching closing bracket found

    def split_options(option_text: str) -> list:
        """
        Splits a string by '|' into a list of options, considering nested brackets.

        Parameters:
        -----------
        option_text : str
            The string containing options separated by '|' within possibly nested brackets.

        Returns:
        --------
        list
            A list of options as strings, extracted from the input string.

        Overview:
        ---------
        This function parses the input string, splitting it into options at the '|' character,
        but skips '|' characters that are within nested brackets, thereby preserving the integrity
        of nested options.
        Examples:
        ---------
        >>> split_options("option1|option2")
        ['option1', 'option2']
        >>> split_options("nested [option1|option2]|option3")
        ['nested [option1|option2]', 'option3']
        """
        options, depth, start = [], 0, 0
        for i, char in enumerate(option_text):
            if char == '[': depth += 1
            elif char == ']': depth -= 1
            elif char == '|' and depth == 0:
                options.append(option_text[start:i])  # End of an option
                start = i + 1  # Start of the next option
        options.append(option_text[start:])  # Add the last option
        return options

    def generate_variations_recursive(current_text: str) -> list:
        """
        Recursively generates all possible variations of a text with bracketed options.

        Parameters:
        -----------
        current_text : str
            The input text containing bracketed options to be expanded.

        Returns:
        --------
        list
            A list of all generated text variations.

        Overview:
        ---------
        This function identifies the first set of bracketed options in the input text,
        generates variations for it, and recursively applies itself to the rest of the text,
        combining generated variations to produce all possible outcomes.

        Examples:
        ---------
        >>> generate_variations_recursive("Hello [World|Universe]")
        ['Hello World', 'Hello Universe']
        >>> generate_variations_recursive("Nested [example [one|two]|case]")
        ['Nested example one', 'Nested example two', 'Nested case']
        """
        # Search for the first opening bracket
        match = re.search(r'\[', current_text)
        if not match:
            return [current_text]  # No more variations to generate

        start_index = match.start()
        end_index = find_matching_bracket(current_text, start_index)
        if end_index == -1:
            return [current_text]  # No matching closing bracket found

        # Split the text into prefix, options, and suffix
        prefix = current_text[:start_index]
        suffix = current_text[end_index+1:]
        options = split_options(current_text[start_index+1:end_index])

        # Recursively generate variations for each option
        variations = []
        for option in options:
            for variant in generate_variations_recursive(option):
                for suffix_variant in generate_variations_recursive(suffix):
                    variations.append(f"{prefix}{variant}{suffix_variant}")
        return variations

    # Generate and return variations with extra spaces removed
    return [re.sub(' +', ' ', variation).strip() for variation in generate_variations_recursive(text)]
