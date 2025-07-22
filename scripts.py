import json
import os


def extract_commands_only(notebook_path):
    """
    Extracts only the code commands (input) from code cells in a Jupyter notebook.
    """
    extracted_commands = []

    if not os.path.exists(notebook_path):
        return f"Error: Notebook not found at '{notebook_path}'"

    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook_data = json.load(f)

    for i, cell in enumerate(notebook_data["cells"]):
        if cell["cell_type"] == "code":
            code_input = "".join(cell["source"])

            extracted_commands.append(f"--- Cell {i+1} (Code) ---\n")
            extracted_commands.append(code_input.strip() + "\n")
            extracted_commands.append("\n")  # Add a blank line for separation

    return "\n".join(extracted_commands)


# --- How to use it ---
# IMPORTANT: Make sure this path points correctly to your crops_train.ipynb file
notebook_file_path = "C:/projects/fyp/crops_train.ipynb"  # Adjust if necessary

extracted_text = extract_commands_only(notebook_file_path)
print(extracted_text)

# Optional: Save to a text file
with open("extracted_commands.txt", "w", encoding="utf-8") as f:
    f.write(extracted_text)
print("\nExtracted commands saved to 'extracted_commands.txt'")
