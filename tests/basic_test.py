import sys
import os
# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

# Try to install required packages if missing
try:
    import gymnasium
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "gymnasium"])
    import gymnasium

from test_build import test_imports
from test_examples import test_learn
test_imports()
test_learn()