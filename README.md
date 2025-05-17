# js-module-extractor

**js-module-extractor** is a lightweight Python CLI tool that extracts and beautifies JavaScript modules from a plain text file. It scans for lines using the pattern `__d("moduleName", ...)`, extracts the module name, formats the code, and writes each module to a separate `.js` file.

## Features

* Detects JavaScript module definitions in `__d("...")` format
* Extracts and saves each module into its own file
* Beautifies the code using [jsbeautifier](https://pypi.org/project/jsbeautifier/)
* CLI usage via `js-module-extractor` command

## Installation

Install directly from the GitHub repository:

```bash
pip install git+https://github.com/maxipalacios/js-module-extractor.git
```

## Usage

After installing, you can run it from the command line:

```bash
js-module-extractor input_file.txt
```

* `input_file.txt`: A UTF-8 encoded text file with one or more `__d("moduleName", ...)` lines.

## Output

The tool will create a folder named `output_modules/` (if not already present) and generate one file per module:

```
output_modules/
└── MyModule.js
```

Each file contains beautified code extracted from the original input.

## Example

Input line:

```js
__d("MyModule", function(global, require, module, exports) { /* code */ }, 123);
```

Command:

```bash
js-module-extractor modules.txt
```

Result:

```
output_modules/
└── MyModule.js
```

## Development Setup

Clone the repo and install in editable mode:

```bash
git clone https://github.com/maxipalacios/js-module-extractor.git
cd js-module-extractor
pip install -e .
```

Run locally:

```bash
js-module-extractor path/to/input.txt
```

## License

This tool is provided under an open license for educational and practical use. Feel free to modify or extend it to fit your needs.