#!/usr/bin/env python3
"""
Clean extraction of JMC servo parameters from HTML manual.
Focuses on extracting parameter tables and individual descriptions.
"""

import re
from pathlib import Path
from bs4 import BeautifulSoup
import json

def extract_jmc_parameters_clean(html_file_path):
    """
    Extract JMC servo parameters using a targeted approach.
    """
    parameters = {}
    
    try:
        print("Reading HTML file...")
        with open(html_file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        
        print("Parsing HTML content...")
        soup = BeautifulSoup(content, 'html.parser')
        
        # Method 1: Look for parameter blocks in text
        text_content = soup.get_text()
        
        # Split text into chunks and find parameter blocks
        param_blocks = re.split(r'(P\d{2}-\d{2})', text_content)
        
        print(f"Found {len(param_blocks)//2} potential parameter blocks")
        
        for i in range(1, len(param_blocks), 2):
            if i + 1 < len(param_blocks):
                param_code = param_blocks[i].strip()
                param_content = param_blocks[i + 1].strip()
                
                # Only process if we don't already have this parameter
                if param_code not in parameters:
                    param_info = parse_parameter_block(param_code, param_content)
                    if param_info:
                        parameters[param_code] = param_info
        
        print(f"Extracted {len(parameters)} parameters")
        
    except Exception as e:
        print(f"Error: {e}")
        return {}
    
    return parameters

def parse_parameter_block(param_code, content):
    """
    Parse a parameter block to extract name and description.
    """
    # Split into lines and clean
    lines = [line.strip() for line in content.split('\n') if line.strip()]
    
    # Stop at next parameter
    clean_lines = []
    for line in lines:
        if re.match(r'P\d{2}-\d{2}', line) and line.strip() != param_code:
            break
        clean_lines.append(line)
    
    if not clean_lines:
        return None
    
    # Find name and description
    name_lines = []
    desc_lines = []
    in_description = False
    
    for line in clean_lines:
        # Skip very short lines that are likely formatting artifacts
        if len(line) < 3:
            continue
            
        # Markers that indicate start of description
        if (line.startswith(('Set range', 'Setting range', 'Set Range')) or 
            re.match(r'^\d+:', line) or  # Numbered options like "0:", "1:"
            'This parameter' in line or
            'When' in line.lower()):
            in_description = True
        
        if in_description:
            # Skip range specifications
            if not (line.startswith(('Set range', 'Setting range', 'Set Range')) and '：' in line):
                desc_lines.append(line)
        else:
            # Collect parameter name
            name_lines.append(line)
    
    # Clean up name and description
    parameter_name = ' '.join(name_lines).strip()
    description = ' '.join(desc_lines).strip()
    
    # Clean artifacts from name
    parameter_name = re.sub(r'^[:\-\s]+', '', parameter_name)
    parameter_name = re.sub(r'[:\-\s]+$', '', parameter_name)
    
    # Only return if we have meaningful content
    if parameter_name or len(description) > 20:
        return {
            'name': parameter_name or 'Unknown',
            'description': description or 'No description available'
        }
    
    return None

def save_clean_parameters(parameters, output_format='md'):
    """Save parameters in clean format"""
    
    if output_format == 'json':
        with open('jmc_parameters_clean.json', 'w', encoding='utf-8') as f:
            json.dump(parameters, f, indent=2, ensure_ascii=False)
    
    elif output_format == 'md':
        with open('jmc_parameters_clean.md', 'w', encoding='utf-8') as f:
            f.write("# JMC Servo Parameters (Clean Extraction)\n\n")
            
            for param, info in sorted(parameters.items()):
                f.write(f"## {param}\n\n")
                f.write(f"**Parameter Name:** {info['name']}\n\n")
                if info['description']:
                    f.write(f"**Description:** {info['description']}\n\n")
                f.write("---\n\n")
    
    elif output_format == 'txt':
        with open('jmc_parameters_clean.txt', 'w', encoding='utf-8') as f:
            for param, info in sorted(parameters.items()):
                f.write(f"{param} - {info['name']}\n")
                if info['description']:
                    f.write(f"Description: {info['description']}\n")
                f.write("\n")

def main():
    """Main function"""
    html_file = Path("JMC_servo_tuning/JMC JAND Series AC Servo Driver User Manual (202011).html")
    
    if not html_file.exists():
        print(f"HTML file not found: {html_file}")
        return
    
    print("Extracting JMC servo parameters (clean method)...")
    parameters = extract_jmc_parameters_clean(html_file)
    
    if parameters:
        save_clean_parameters(parameters, 'json')
        save_clean_parameters(parameters, 'md')  
        save_clean_parameters(parameters, 'txt')
        
        print(f"\nExtracted {len(parameters)} parameters")
        print("Files created:")
        print("- jmc_parameters_clean.json")
        print("- jmc_parameters_clean.md")
        print("- jmc_parameters_clean.txt")
        
        # Show sample
        print("\nSample parameters:")
        count = 0
        for param, info in sorted(parameters.items()):
            if count >= 3:
                break
            print(f"\n{param} - {info['name']}")
            if info['description']:
                desc = info['description'][:100] + "..." if len(info['description']) > 100 else info['description']
                print(f"  {desc}")
            count += 1
    else:
        print("No parameters found")

if __name__ == "__main__":
    main()