#!/usr/bin/env python3
"""
Analyze the HTML structure to understand parameter layout
"""

from bs4 import BeautifulSoup
import re

def analyze_html_structure():
    """Analyze HTML structure around parameters"""
    
    with open("JMC_servo_tuning/JMC JAND Series AC Servo Driver User Manual (202011).html", 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find all text nodes containing P08-13 to understand structure
    text_content = soup.get_text()
    
    # Find P08-13 location and extract surrounding context
    p08_13_pos = text_content.find('P08-13')
    if p08_13_pos != -1:
        # Get 500 characters before and after
        start = max(0, p08_13_pos - 500)
        end = min(len(text_content), p08_13_pos + 1000)
        context = text_content[start:end]
        
        print("Context around P08-13:")
        print("Writing context to file...")
        with open('p08_13_context.txt', 'w', encoding='utf-8') as f:
            f.write("Context around P08-13:\n")
            f.write("=" * 60 + "\n")
            f.write(context)
            f.write("\n" + "=" * 60)
    
    # Also look for table structures
    tables = soup.find_all('table')
    print(f"\nFound {len(tables)} tables in the document")
    
    # Look for div structures that might contain parameters
    divs_with_params = []
    all_divs = soup.find_all('div')
    
    for div in all_divs:
        div_text = div.get_text()
        if re.search(r'P\d{2}-\d{2}', div_text):
            divs_with_params.append(div)
    
    print(f"Found {len(divs_with_params)} divs containing parameters")
    
    if divs_with_params:
        # Show first few divs with parameters
        for i, div in enumerate(divs_with_params[:3]):
            print(f"\nDiv {i+1} with parameters:")
            print("-" * 40)
            print(div.get_text()[:200] + "...")

if __name__ == "__main__":
    analyze_html_structure()