#!/usr/bin/env python3
"""
Improved extraction of JMC servo parameters with better parsing logic
"""

import re
from pathlib import Path
from bs4 import BeautifulSoup
import json

def extract_jmc_parameters_improved(html_file_path):
    """
    Improved extraction using better text parsing logic
    """
    parameters = {}
    
    try:
        print("Reading HTML file...")
        with open(html_file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        
        print("Parsing HTML content...")
        soup = BeautifulSoup(content, 'html.parser')
        text_content = soup.get_text()
        
        # Use regex to find parameter sections more precisely
        param_pattern = r'P(\d{2})-(\d{2})\s+([^P]+?)(?=P\d{2}-\d{2}|$)'
        matches = re.finditer(param_pattern, text_content, re.DOTALL)
        
        print("Processing parameter matches...")
        
        for match in matches:
            param_code = f"P{match.group(1)}-{match.group(2)}"
            param_content = match.group(3).strip()
            
            # Parse this parameter's content
            param_info = parse_parameter_content_improved(param_code, param_content)
            if param_info:
                parameters[param_code] = param_info
        
        print(f"Extracted {len(parameters)} parameters")
        
    except Exception as e:
        print(f"Error: {e}")
        return {}
    
    return parameters

def parse_parameter_content_improved(param_code, content):
    """
    Improved parsing of parameter content
    """
    # Split into lines and clean
    lines = [line.strip() for line in content.split('\n') if line.strip()]
    
    if not lines:
        return None
    
    parameter_name = ""
    setting_range = ""
    description = ""
    
    # Find the parameter name (usually the first meaningful line)
    name_candidates = []
    desc_lines = []
    in_description = False
    
    for i, line in enumerate(lines):
        # Skip very short lines or obvious artifacts
        if len(line) < 3 or line.startswith(('Just motion', '0755-', 'Page')):
            continue
            
        # Check for setting range
        if re.match(r'Setting?\s+range[：:]', line, re.IGNORECASE):
            setting_range = line
            in_description = True
            continue
        
        # Check for description indicators
        if (in_description or 
            line.startswith(('This parameter', 'When', 'The')) or
            'parameter' in line.lower() or
            any(word in line.lower() for word in ['sets', 'controls', 'defines', 'specifies'])):
            in_description = True
            desc_lines.append(line)
            continue
        
        # Check for numbered options (like 0:, 1:, 2:)
        if re.match(r'^\d+[：:]', line):
            in_description = True
            desc_lines.append(line)
            continue
            
        # If not in description yet, consider it part of the name
        if not in_description and not setting_range:
            name_candidates.append(line)
    
    # Clean up parameter name
    if name_candidates:
        # Take the first line that looks like a proper parameter name
        for candidate in name_candidates:
            # Filter out obvious artifacts
            if (not any(word in candidate.lower() for word in ['just motion', 'control', '0755']) and
                len(candidate) < 200 and  # Not too long
                not re.match(r'^\d+[：:]', candidate)):  # Not a numbered option
                parameter_name = candidate
                break
        
        # If no good candidate, take the first one and clean it
        if not parameter_name and name_candidates:
            parameter_name = name_candidates[0]
    
    # Clean up description
    if desc_lines:
        description = ' '.join(desc_lines)
        # Remove common artifacts
        description = re.sub(r'Just motion control.*?\d{4}-\d{7}.*?\d+', '', description)
        description = re.sub(r'\s+', ' ', description).strip()
    
    # Clean parameter name further
    if parameter_name:
        # Remove setting range if it got mixed in
        parameter_name = re.sub(r'Setting?\s+range[：:].*?(?=\s|$)', '', parameter_name, flags=re.IGNORECASE)
        parameter_name = re.sub(r'\s+', ' ', parameter_name).strip()
        
        # Remove trailing artifacts
        parameter_name = re.sub(r'[：:\-\s]+$', '', parameter_name)
        parameter_name = re.sub(r'^[：:\-\s]+', '', parameter_name)
    
    # Only return if we have meaningful content
    if parameter_name or description:
        return {
            'name': parameter_name or 'Unknown',
            'setting_range': setting_range,
            'description': description or 'No description available'
        }
    
    return None

def save_improved_parameters(parameters, output_format='md'):
    """Save parameters in improved format"""
    
    if output_format == 'json':
        with open('jmc_parameters_improved.json', 'w', encoding='utf-8') as f:
            json.dump(parameters, f, indent=2, ensure_ascii=False)
    
    elif output_format == 'md':
        with open('jmc_parameters_improved.md', 'w', encoding='utf-8') as f:
            f.write("# JMC Servo Parameters (Improved Extraction)\n\n")
            
            for param, info in sorted(parameters.items()):
                f.write(f"## {param}\n\n")
                f.write(f"**Parameter Name:** {info['name']}\n\n")
                
                if info.get('setting_range'):
                    f.write(f"**{info['setting_range']}**\n\n")
                
                if info['description']:
                    f.write(f"**Description:** {info['description']}\n\n")
                    
                f.write("---\n\n")
    
    elif output_format == 'txt':
        with open('jmc_parameters_improved.txt', 'w', encoding='utf-8') as f:
            for param, info in sorted(parameters.items()):
                f.write(f"{param} - {info['name']}\n")
                if info.get('setting_range'):
                    f.write(f"  {info['setting_range']}\n")
                if info['description']:
                    f.write(f"  Description: {info['description']}\n")
                f.write("\n")

def main():
    """Main function"""
    html_file = Path("JMC_servo_tuning/JMC JAND Series AC Servo Driver User Manual (202011).html")
    
    if not html_file.exists():
        print(f"HTML file not found: {html_file}")
        return
    
    print("Extracting JMC servo parameters (improved method)...")
    parameters = extract_jmc_parameters_improved(html_file)
    
    if parameters:
        save_improved_parameters(parameters, 'json')
        save_improved_parameters(parameters, 'md')  
        save_improved_parameters(parameters, 'txt')
        
        print(f"\nExtracted {len(parameters)} parameters")
        print("Files created:")
        print("- jmc_parameters_improved.json")
        print("- jmc_parameters_improved.md")
        print("- jmc_parameters_improved.txt")
        
        # Show specific test parameters
        test_params = ['P08-13', 'P08-17', 'P08-19', 'P01-03']
        print(f"\nTest parameters:")
        for param in test_params:
            if param in parameters:
                info = parameters[param]
                print(f"\n{param} - {info['name']}")
                if info.get('setting_range'):
                    print(f"  {info['setting_range']}")
                if info['description']:
                    desc = info['description'][:150] + "..." if len(info['description']) > 150 else info['description']
                    print(f"  {desc}")
            else:
                print(f"\n{param} - Not found")
    else:
        print("No parameters found")

if __name__ == "__main__":
    main()