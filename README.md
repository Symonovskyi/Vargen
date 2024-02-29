# <img src="https://raw.githubusercontent.com/Symonovskyi/Symonovskyi/main/src/projects/Vargen/Vargen-icon48.png" height="48"/> Vargen

## Description

Vargen is a tool for generating all possible combinations of text from templates that include placeholders in brackets. It's designed for tasks that require multiple versions of a text, simplifying the process with an intuitive bracket notation.

<img src="https://raw.githubusercontent.com/Symonovskyi/Symonovskyi/main/src/projects/Vargen/Vargen-background.webp" alt="background">

## Features

- **Automated Variations**: Generates every possible combination from text templates.
- **Bracket Placeholders**: Easy-to-use notation for placeholders `[option1|option2]`.
- **Command-line Use**: Simple CLI execution with customizable options.
- **Efficient Processing**: Controls for batch size and memory usage optimize performance.
- **Open Source Licensing**: Available under [MIT](./LICENSE_MIT) and [CC BY 4.0](./LICENSE_CC_BY_4.0) licenses for wide use and adaptation.

## Getting Started

Vargen utilizes Python's standard libraries `re` for regular expressions and `concurrent.futures` for parallel execution, requiring no additional installations beyond Python itself.

### Prerequisites

- Python 3.6 or newer.

### Installation

Clone the repository and you're ready to go. Vargen runs directly from the source.

``` bash
git clone https://github.com/Symonovskyi/Vargen.git
```

## Usage

Run Vargen directly from the command line, adjusting parameters as needed for your task.

### Basic Command Structure

``` bash
python vargen.py [options]
```

### Options Overview

- `append`: Append to output file (`true` or `false`).
- `separator`: Separator string between text variations.
- `input_filename`: Path to your input file.
- `output_filename`: Path to your output file.

## Examples

### Command-Line Usage

**Basic Usage**  
Generate variations with default settings:

``` bash
python vargen.py
```

**Appending to Output with a Separator**  
Append to the output file, separating batches with "---":

``` bash
python vargen.py append=true separator="---"
```

**Using Custom Input and Output Files**  
Specify custom input and output files:

``` bash
python vargen.py input_filename="my_input.txt" output_filename="my_output.txt"
```

**Full Command with All Options**  
Append to a custom output file with a separator, using a custom input file:

``` bash
python vargen.py append=true separator="-----" input_filename="custom_input.txt" output_filename="custom_output.txt"
```

**Positional Arguments for Quick Configuration**  
Enable performance analysis, append mode, and set a separator, with custom file names:

``` bash
python vargen.py true true "-----" custom_input.txt custom_output.txt
```

### Python Code Usage

**Default Function Call**  
Invoke `generate_variations` with default parameters from within Python code:

``` python
from vargen import generate_variations
generate_variations()
```

**Custom Configuration**  
Invoke `generate_variations` with custom settings:

``` python
from vargen import generate_variations
generate_variations(append=True, separator="---", input_filename="input.txt", output_filename="output.txt")
```

## License

Vargen is distributed under a dual-license: [MIT](./LICENSE_MIT) License and Creative Commons Attribution 4.0 International ([CC BY 4.0](./LICENSE_CC_BY_4.0)). By using, copying, modifying, or distributing the project, you agree to the terms of both licenses. You must credit the authorship as per [CC BY](./LICENSE_CC_BY_4.0) requirements while also adhering to the freedom of use provided under the [MIT](./LICENSE_MIT) License.

## Notes

- Ensure the input file exists and is readable, and the output file is writable.
- Default values are applied for any unspecified parameters.
- The documentation within the code files provides detailed descriptions of each function's purpose and usage.