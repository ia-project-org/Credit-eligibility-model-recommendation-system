import shutil

# Path to the original notebook
original_notebook_path = "model_training.ipynb"

# Path to the new notebook (can be a different directory or name)
new_notebook_path = "notebooks/model_training.ipynb"

# Copy the notebook
shutil.copy(original_notebook_path, new_notebook_path)
