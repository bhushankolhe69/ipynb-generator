import json

# Define the notebook structure
notebook = {
    "cells": [],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.9.5"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

# Define a function to add cells to the notebook
def add_cell(cell_type, source):
    cell = {
        "cell_type": cell_type,
        "metadata": {},
        "source": source
    }
    notebook["cells"].append(cell)

def add_cell1(cell_type, source):
    cell = {
        "cell_type": cell_type,
        "metadata": {},
        "source": source
    }
    notebook["cells"].append(cell)

# Generate the notebook content
add_cell("markdown", "# Welcome to your IPython Notebook!")
add_cell("code", "import pandas as pd\n\n# Your code goes here")

add_cell1("markdown", "# Here's the second cell")
add_cell1("code", "# Your code goes here")
# Save the notebook as an .ipynb file
with open("notebook.ipynb", "w") as f:
    json.dump(notebook, f)

print("Notebook generated successfully!")