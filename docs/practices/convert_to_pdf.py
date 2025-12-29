#!/usr/bin/env python3
"""
Simple Markdown to PDF converter using markdown and weasyprint
"""
import sys
import subprocess

def install_packages():
    """Install required packages"""
    packages = ['markdown', 'weasyprint']
    for package in packages:
        try:
            __import__(package)
            print(f"✓ {package} already installed")
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--user', package])

def convert_md_to_pdf(md_file, pdf_file):
    """Convert markdown file to PDF"""
    try:
        import markdown
        from weasyprint import HTML, CSS

        # Read markdown file
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # Convert to HTML
        html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])

        # Add CSS styling
        styled_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            color: #333;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-top: 40px;
        }}
        h2 {{
            color: #34495e;
            border-bottom: 2px solid #95a5a6;
            padding-bottom: 8px;
            margin-top: 30px;
        }}
        h3 {{
            color: #16a085;
            margin-top: 25px;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 12px 8px;
            text-align: left;
        }}
        th {{
            background-color: #3498db;
            color: white;
            font-weight: bold;
        }}
        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
        blockquote {{
            border-left: 4px solid #3498db;
            margin: 20px 0;
            padding: 10px 20px;
            background-color: #ecf0f1;
            font-style: italic;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: "Courier New", monospace;
        }}
        ul, ol {{
            margin: 15px 0;
            padding-left: 30px;
        }}
        li {{
            margin: 8px 0;
        }}
        strong {{
            color: #2c3e50;
        }}
        hr {{
            border: none;
            border-top: 2px solid #ecf0f1;
            margin: 30px 0;
        }}
        @page {{
            size: letter;
            margin: 1in;
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>
"""

        # Convert to PDF
        HTML(string=styled_html).write_pdf(pdf_file)
        print(f"✓ Successfully created PDF: {pdf_file}")
        return True

    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == "__main__":
    md_file = "docs/practices/SM-Strategy-Metrics-Domain-Descriptions.md"
    pdf_file = "docs/practices/SM-Strategy-Metrics-Domain-Descriptions.pdf"

    print("Installing required packages...")
    install_packages()

    print("\nConverting markdown to PDF...")
    if convert_md_to_pdf(md_file, pdf_file):
        print("\n✓ Conversion complete!")
    else:
        print("\n✗ Conversion failed!")
        sys.exit(1)
