#!/usr/bin/env python3
"""
Clean Jupyter Notebooks for Git Upload
This script removes execution counts and outputs from notebooks
"""

import json
import os
import glob

def clean_notebook(notebook_path):
    """Clean a single notebook by removing execution counts and outputs"""
    print(f"Cleaning {notebook_path}...")
    
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Clean each cell
        for cell in notebook.get('cells', []):
            if cell.get('cell_type') == 'code':
                # Remove execution count
                if 'execution_count' in cell:
                    cell['execution_count'] = None
                
                # Remove outputs
                if 'outputs' in cell:
                    cell['outputs'] = []
                
                # Remove metadata execution info
                if 'metadata' in cell:
                    if 'execution' in cell['metadata']:
                        del cell['metadata']['execution']
        
        # Clean notebook metadata
        if 'metadata' in notebook:
            if 'execution' in notebook['metadata']:
                del notebook['metadata']['execution']
        
        # Write cleaned notebook back
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
        
        print(f"✅ Cleaned {notebook_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error cleaning {notebook_path}: {e}")
        return False

def main():
    """Clean all notebooks in the current directory"""
    print("🧹 Cleaning Jupyter Notebooks for Git Upload")
    print("=" * 50)
    
    # Find all .ipynb files
    notebook_files = glob.glob("*.ipynb")
    
    if not notebook_files:
        print("No notebook files found in current directory")
        return
    
    print(f"Found {len(notebook_files)} notebook(s):")
    for nb in notebook_files:
        print(f"  - {nb}")
    
    print("\nCleaning notebooks...")
    
    success_count = 0
    for notebook_file in notebook_files:
        if clean_notebook(notebook_file):
            success_count += 1
    
    print(f"\n✅ Successfully cleaned {success_count}/{len(notebook_files)} notebooks")
    print("\nYour notebooks are now ready for Git upload!")
    print("All execution counts and outputs have been removed.")

if __name__ == "__main__":
    main()
