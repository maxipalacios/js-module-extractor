import os
import sys
import jsbeautifier
import logging
import re

def main():
    if len(sys.argv) != 2:
        print("Usage: js-module-extractor input_file.txt")
        return

    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Starting the program")

    input_file = sys.argv[1]
    output_folder = 'output_modules'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        logging.info(f"Folder '{output_folder}' created")

    opts = jsbeautifier.default_options()
    opts.indent_size = 4

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('__d("'):
                try:
                    # Use regex to extract the module name
                    match = re.match(r'__d\("([^"]+)"', line)
                    if match:
                        module_name = match.group(1)
                    else:
                        logging.warning(f"Could not extract module name from line: {line}")
                        continue

                    content = line

                    # Beautify the content for readable JSON
                    beautified_content = jsbeautifier.beautify(content, opts)

                    # Save the content to a file
                    filename = f"{module_name}.js"
                    output_path = os.path.join(output_folder, filename)
                    with open(output_path, 'w', encoding='utf-8') as out_file:
                        out_file.write(beautified_content)

                    logging.info(f"Module '{module_name}' saved in '{output_path}'")

                except Exception as e:
                    logging.error(f"Error processing line: {line}")
                    logging.error(e)
                    continue

    logging.info("Program finished")

if __name__ == '__main__':
    main()
