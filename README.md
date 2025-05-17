# js-module-extractor

**js-module-extractor** is a lightweight Python utility for extracting and formatting JavaScript modules from a plain text file. It targets lines that use the `__d("moduleName", ...)` pattern, extracting the module name, beautifying the code, and saving it to individual `.js` files.

## Features

* Detects and extracts lines beginning with `__d("...")`.
* Uses regular expressions to determine the module name.
* Beautifies the code using `jsbeautifier` for readability.
* Saves each module to a separate `.js` file in the `output_modules` directory.

## Requirements

* Python 3.6 or higher
* [jsbeautifier](https://pypi.org/project/jsbeautifier/)

Install the required dependency:

```bash
pip install jsbeautifier
```

## Usage

```bash
python module_generator.py input_file.txt
```

* `input_file.txt`: A UTF-8 text file containing one or more lines with `__d("moduleName", ...)` JavaScript module definitions.

## Output

The script creates an `output_modules/` folder (if it doesn’t exist already) and writes each extracted module into its own file. Files are named using the module name (e.g., `MyModule.js`) and contain the formatted module content.

## Example

Given an input line like:

```javascript
__d("MyModule", function(global, require, module, exports) { /* module code */ }, 123);
```

The script will generate:

```
output_modules/
└── MyModule.js
```

## Logging

The script provides logging messages to indicate:

* When it starts and finishes
* If the output folder is created
* Each module successfully processed
* Any lines that couldn't be parsed
* Errors encountered during processing

## License

This tool is provided under an open license for educational and practical use. Feel free to modify or extend it to fit your needs.
