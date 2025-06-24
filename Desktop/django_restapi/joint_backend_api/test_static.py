#!/usr/bin/env python
"""
Test script to verify static files are accessible
"""
import os
# import requests
from pathlib import Path

def test_static_files():
    """Test if static files exist and are accessible"""
    
    # Check if staticfiles directory exists
    staticfiles_dir = Path('staticfiles')
    if not staticfiles_dir.exists():
        print("❌ staticfiles directory not found!")
        return False
    
    # Check for admin CSS files
    admin_css_dir = staticfiles_dir / 'admin' / 'css'
    if not admin_css_dir.exists():
        print("❌ admin/css directory not found!")
        return False
    
    # Check for key CSS files
    key_files = ['base.css', 'forms.css', 'responsive.css', 'changelists.css']
    missing_files = []
    
    for file in key_files:
        file_path = admin_css_dir / file
        if not file_path.exists():
            missing_files.append(file)
        else:
            print(f"✅ {file} exists")
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return False
    
    print("✅ All key CSS files found!")
    return True

if __name__ == "__main__":
    print("Testing static files...")
    test_static_files() 