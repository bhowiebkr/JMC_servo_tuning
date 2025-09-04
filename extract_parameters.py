#!/usr/bin/env python3
"""
Extract JMC servo parameters from HTML manual file.
Parameters follow format: P##-## (e.g., P08-13)
"""

import re
from pathlib import Path
from bs4 import BeautifulSoup
import json

def extract_jmc_parameters(html_file_path):
    """
    Extract JMC servo parameters and descriptions from HTML file.
    
    Args:
        html_file_path (str): Path to the HTML manual file
        
    Returns:
        dict: Dictionary of parameters with descriptions
    """
    parameters = {}
    
    try:
        print("Reading HTML file...")
        with open(html_file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        
        print("Parsing HTML content...")
        soup = BeautifulSoup(content, 'html.parser')
        
        # Get all text content
        text_content = soup.get_text()
        
        # Split into lines and clean up
        lines = [line.strip() for line in text_content.split('\n') if line.strip()]
        
        print(f"Processing {len(lines)} lines of text...")
        
        # Find parameter patterns
        param_pattern = r'P\d{2}-\d{2}'
        
        for i, line in enumerate(lines):
            param_matches = re.finditer(param_pattern, line)
            
            for match in param_matches:
                param_code = match.group()
                
                # Skip if we already have this parameter
                if param_code in parameters:
                    continue
                
                # Extract parameter info from surrounding lines
                param_info = extract_parameter_info(lines, i, param_code)
                if param_info:
                    parameters[param_code] = param_info
        
        print(f"Found {len(parameters)} unique parameters")
        
    except Exception as e:
        print(f"Error reading file: {e}")
        return parameters
    
    return parameters

def extract_parameter_info(lines, param_line_idx, param_code):
    """
    Extract parameter information from lines of text.
    
    Args:
        lines (list): List of text lines
        param_line_idx (int): Index of line containing the parameter
        param_code (str): Parameter code (e.g., P08-13)
        
    Returns:
        dict: Dictionary with parameter name and description
    """
    # Get the line with the parameter
    param_line = lines[param_line_idx]
    
    # Extract parameter name from the same line or next lines
    parameter_name = ""
    description_lines = []
    
    # Check if parameter name is on the same line after the parameter code
    param_pos = param_line.find(param_code)
    if param_pos != -1:
        text_after_param = param_line[param_pos + len(param_code):].strip()
        if text_after_param and not text_after_param.startswith(('Set range', 'Set Range')):
            parameter_name = text_after_param
    
    # If no name found on same line, check next few lines
    if not parameter_name:
        for i in range(param_line_idx + 1, min(len(lines), param_line_idx + 5)):
            line = lines[i].strip()
            if line and not line.startswith(('Set range', 'Set Range', '0:', '1:', '2:')):
                if not re.match(r'P\d{2}-\d{2}', line):  # Not another parameter
                    parameter_name = line
                    break
    
    # Collect description lines
    start_idx = param_line_idx + 1
    if parameter_name and parameter_name in param_line:
        start_idx = param_line_idx + 1
    elif parameter_name:
        # Find where the parameter name ends
        for i in range(param_line_idx + 1, min(len(lines), param_line_idx + 10)):
            if parameter_name in lines[i]:
                start_idx = i + 1
                break
    
    # Collect description from subsequent lines
    for i in range(start_idx, min(len(lines), start_idx + 15)):
        line = lines[i].strip()
        
        # Stop conditions
        if not line:
            continue
        if re.match(r'P\d{2}-\d{2}', line):  # Hit another parameter
            break
        if line.startswith(('Table', 'Fig', 'Page', '©')):  # Common document artifacts
            break
        if len(line) < 5:  # Too short to be meaningful
            continue
            
        description_lines.append(line)
        
        # Stop if we have enough description
        if len(' '.join(description_lines)) > 300:
            break
    
    if parameter_name or description_lines:
        full_description = ' '.join(description_lines)
        # Clean up description
        full_description = re.sub(r'\s+', ' ', full_description)
        full_description = full_description.strip()
        
        # Clean parameter name
        if parameter_name:
            parameter_name = re.sub(r'\s+', ' ', parameter_name).strip()
            # Remove common artifacts
            parameter_name = re.sub(r'^[:\-\s]+', '', parameter_name)
            parameter_name = re.sub(r'[:\-\s]+$', '', parameter_name)
        
        return {
            'name': parameter_name or 'Unknown',
            'description': full_description or 'No description available',
            'raw_context': param_line[:200]  # Keep some raw context for debugging
        }
    
    return None

def save_parameters(parameters, output_format='json'):
    """
    Save extracted parameters to file.
    
    Args:
        parameters (dict): Dictionary of parameters
        output_format (str): Output format ('json', 'md', 'txt')
    """
    if output_format == 'json':
        with open('jmc_parameters.json', 'w', encoding='utf-8') as f:
            json.dump(parameters, f, indent=2, ensure_ascii=False)
    
    elif output_format == 'md':
        with open('jmc_parameters.md', 'w', encoding='utf-8') as f:
            f.write("# JMC Servo Parameters\n\n")
            for param, info in sorted(parameters.items()):
                if isinstance(info, dict):
                    f.write(f"## {param} - {info.get('name', 'Unknown')}\n\n")
                    f.write(f"**Description:** {info.get('description', 'No description')}\n\n")
                else:
                    f.write(f"## {param}\n")
                    f.write(f"{info}\n\n")
    
    elif output_format == 'txt':
        with open('jmc_parameters.txt', 'w', encoding='utf-8') as f:
            for param, info in sorted(parameters.items()):
                if isinstance(info, dict):
                    f.write(f"{param} - {info.get('name', 'Unknown')}\n")
                    f.write(f"Description: {info.get('description', 'No description')}\n\n")
                else:
                    f.write(f"{param}: {info}\n")

def main():
    """Main function to extract and save JMC parameters."""
    html_file = Path("JMC_servo_tuning/JMC JAND Series AC Servo Driver User Manual (202011).html")
    
    if not html_file.exists():
        print(f"HTML file not found: {html_file}")
        return
    
    print("Extracting JMC servo parameters...")
    parameters = extract_jmc_parameters(html_file)
    
    print(f"Found {len(parameters)} parameters")
    
    if parameters:
        # Save in multiple formats
        save_parameters(parameters, 'json')
        save_parameters(parameters, 'md')
        save_parameters(parameters, 'txt')
        
        print("Parameters saved to:")
        print("- jmc_parameters.json")
        print("- jmc_parameters.md") 
        print("- jmc_parameters.txt")
        
        # Display first few parameters
        print("\nFirst few parameters found:")
        for i, (param, info) in enumerate(sorted(parameters.items())):
            if i >= 5:
                break
            if isinstance(info, dict):
                name = info.get('name', 'Unknown')[:50]
                desc = info.get('description', 'No description')[:100]
                print(f"{param} - {name}: {desc}...")
            else:
                print(f"{param}: {str(info)[:100]}...")
    else:
        print("No parameters found")

if __name__ == "__main__":
    main()