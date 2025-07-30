
# Check if .venv directory exists, if not, create it
if (-Not (Test-Path -Path ".\.venv")) {
    python3 -m venv .venv
}

# Activate the virtual environment
.\.venv\Scripts\activate

# Upgrade pip to the latest version
pip install --upgrade pip

# Install required packages from requirements.txt
pip install -r requirements.txt

# Run the main.py script
python main.py