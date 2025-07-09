#!/usr/bin/env python3
"""
✨ Slaycoded Repository Creator
Creates a complete Slaycoded documentation repository with style!
"""

import os
import sys
from pathlib import Path

def create_slaycoded_repo():
    """Create the Slaycoded repository structure with all files."""
    
    ROOT = "Slaycoded"
    
    # File contents dictionary
    files = {
        "README.md": '''# 💅 Slaycoded

Slaycoded is documentation for the human brain—Interactive Documentation for Ease of Audacious Slayage (IDEAS). Created for intermediate-to-expert users who crave clarity, precision, and cognition-friendly guidance.

## 📖 Philosophy
Slaycoded empowers users by leveraging human sensory understanding (visual, auditory, tactile, temporal). Clear context, concise language, no fluff.

## 🚀 Quickstart
- [Slaycoded Philosophy](docs/slaycoded-philosophy.md)
- [Style Guide](docs/style-guide.md)
- [Examples](examples/)
- [Templates](templates/slaycoded-template.md)

## 🌟 Contribute
Feel free to open issues, discussions, or PRs—your slay is welcome!

## 📃 License
MIT License—free and fabulous.
''',

        "docs/slaycoded-philosophy.md": '''# 🌟 Slaycoded Philosophy

Slaycoded isn't simplifying; it's clarifying. Built on:

- **Human Cognition**: Align with natural sensory and cognitive processes.
- **Contextual Clarity**: Always explain the 'why' behind each action.
- **Conciseness**: Detailed, yet free of redundancy or fluff.
- **Respect**: Assume intelligence without patronizing.

Documentation should be a seamless experience, not a chore.
''',

        "docs/style-guide.md": '''# 🎨 Slaycoded Style Guide

## Essentials
- **Dictionary Examples**: Clearly define and exemplify concepts.
- **Analogies**: Relatable, sensory-rich metaphors.
- **Step-by-step clarity**: No ambiguity.

## Example Entry Format

### Term (noun)
*Definition:* Concise explanation.

*Slaycoded example:*
> "Clear, practical usage example here."

*Analogy:* Simple, relatable metaphor.

## Writing Tone
Friendly, clear, concise, respectful. Glamorous, not frivolous.
''',

        "examples/inference-example.md": '''# 🎮 Inference Example

### Inference (noun)
*Definition:* Process of enhancing media using AI models.

*Slaycoded example:*
> "Run inference using 'Apollo' for realism in Topaz Video AI. Preview first to ensure optimal results."

*Analogy:* Like taste-testing while cooking; always sample first!
''',

        "examples/batch-processing-example.md": '''# 🧹 Batch Processing Example

### Batch Processing (noun)
*Definition:* Simultaneous application of settings/effects to multiple files.

*Slaycoded example:*
> "Apply grain reduction to 30 video clips simultaneously, saving hours."

*Analogy:* Meal prepping once for the entire week.
''',

        "examples/directory-structure-example.md": '''# 📂 Directory Structure Example

### Directory Structure (noun)
*Definition:* Organized folder/file hierarchy.

*Slaycoded example:*
```
📁 Project
📝┃📁 Raw_Footage
📝┃📁 Exports
📝└📁 Final_Cut
```

*Analogy:* Closet organization—shirts, pants, shoes separated for easy access.
''',

        "templates/slaycoded-template.md": '''# 🔥 Slaycoded Template

## 📝 Title
Clear goal of this document.

## ✅ Prerequisites
- List needed items upfront (software, tools, money)

## 🛠️ Step-by-Step Guide
1. Step one (concise, clear)
2. Step two (context if choices exist)
3. Final step (confirm completion clearly)

## ❗ Troubleshooting
- Common problem: Concise solution

## 📚 Glossary (Dictionary Style)
### Term (noun)
*Definition:* Explanation

*Slaycoded example:*
> Practical example usage.

*Analogy:* Relatable metaphor
''',

        ".gitignore": '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
''',

        "LICENSE": '''MIT License

Copyright (c) 2024 Slaycoded

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
    }
    
    # Check if directory already exists
    if os.path.exists(ROOT):
        response = input(f"📁 Directory '{ROOT}' already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("❌ Operation cancelled.")
            return False
    
    # Create directory structure and files
    created_files = []
    created_dirs = set()
    
    try:
        for file_path, content in files.items():
            full_path = Path(ROOT) / file_path
            
            # Create directory if it doesn't exist
            full_path.parent.mkdir(parents=True, exist_ok=True)
            created_dirs.add(str(full_path.parent))
            
            # Write file
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            created_files.append(str(full_path))
            
        print("✨ Slaycoded repository created successfully!")
        print(f"📁 Created {len(created_dirs)} directories")
        print(f"📄 Created {len(created_files)} files")
        print(f"\n🚀 Next steps:")
        print(f"   cd {ROOT}")
        print(f"   # Start creating your slaycoded documentation!")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating repository: {e}")
        return False

def main():
    """Main function to run the script."""
    print("💅 Welcome to Slaycoded Repository Creator!")
    print("🎯 This will create a complete documentation repository structure.\n")
    
    if create_slaycoded_repo():
        print("\n🎉 Repository initialization complete! Time to slay! 💪💅")
    else:
        print("\n😞 Repository creation failed. Please try again.")
        sys.exit(1)

if __name__ == "__main__":
    main()
