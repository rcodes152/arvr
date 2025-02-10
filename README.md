Setting Up the Virtual Environment

1. Create a Virtual Environment

Run the following command in your terminal or command prompt:

python -m venv venv

2. Activate the Virtual Environment

On Windows:

venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

3. Install Dependencies from requirements.txt

Run the following command to install all required dependencies:

pip install -r requirements.txt

Updating the File Path in generate_depth.py

4. Change the Input and Output Paths

To modify the paths in generate_depth.py, follow these steps:

Open generate_depth.py in VS Code.

Right-click the file or folder you need and select Copy Path.

Paste the absolute path in the script where required.

Example:

input_path = "C:\\Users\\YourName\\Project\\input_file.png"
output_path = "C:\\Users\\YourName\\Project\\output_file.png"

Ensure the paths use double backslashes (\\) in Windows or regular slashes (/) in macOS/Linux.

This guide ensures a smooth setup and correct path modifications for running the script successfully.
