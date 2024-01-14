import os
import argparse
import importlib.util
import subprocess
from pydantic import BaseModel
from typing import get_type_hints


def load_py_module(file_path, module_name):
    """Dynamically loads a Python module from the given file path."""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def python_type_to_typescript(type_hint):
    """
    Converts a Python type hint to a TypeScript type.
    Add mappings as needed based on your project's types.
    """
    mapping = {
        int: 'number',
        float: 'number',
        str: 'string',
        bool: 'boolean',
        # Add other type mappings here
    }
    return mapping.get(type_hint, 'any')  # Default to 'any' for unmapped types

def convert_to_typescript(model_class):
    """Generates a TypeScript interface from a Pydantic model class."""
    type_hints = get_type_hints(model_class)
    fields = [f'{field}: {python_type_to_typescript(type_hint)};' for field, type_hint in type_hints.items()]
    ts_interface = f'export interface {model_class.__name__} {{\n  ' + '\n  '.join(fields) + '\n}\n'
    return ts_interface


def write_ts_file(model_name, ts_interface, output_folder):
    """Writes the TypeScript interface to a file."""
    with open(os.path.join(output_folder, f"{model_name}.ts"), "w") as file:
        file.write(ts_interface)


def main(source_folder, output_folder):

    # Exit if no input folder is specified
    if not source_folder or not os.path.isdir(source_folder):
        print("Invalid input folder specified.")
        return

    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)

    # Remove all existing TypeScript files from the output directory
    for file in os.listdir(output_folder):
        if file.endswith(".ts"):
            os.remove(os.path.join(output_folder, file))

    interface_names = set()

    # Process each Python file in the source directory
    for file in os.listdir(source_folder):
        if file.endswith(".py") and file != "__init__.py":
            model_file_path = os.path.join(source_folder, file)
            model_name = file[:-3]

            # Load the model as a Python module
            model_module = load_py_module(model_file_path, model_name)

            # Find all model classes in the module
            for model_name in dir(model_module):
                attribute = getattr(model_module, model_name)
                if isinstance(attribute, type) and issubclass(attribute, BaseModel) and attribute is not BaseModel:
                    # Convert the model to TypeScript
                    ts_interface = convert_to_typescript(attribute)
                    write_ts_file(model_name, ts_interface, output_folder)
                    interface_names.add(model_name)
                    print(f"Converted {model_name} to TypeScript interface.")

    # Create index.ts file
    with open(os.path.join(output_folder, "index.ts"), "a") as index_file:
        for model_name in interface_names:
            index_file.write(f"export * from './{model_name}';\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate TypeScript interfaces from Pydantic models.")
    parser.add_argument(
        "source_folder", help="The source folder containing Pydantic models.")
    parser.add_argument(
        "output_folder", help="The output folder for TypeScript interfaces.")
    args = parser.parse_args()

    main(args.source_folder, args.output_folder)
