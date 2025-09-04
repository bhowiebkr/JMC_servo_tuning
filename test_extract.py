#!/usr/bin/env python3

# Test extraction with the sample text you provided
sample_text = """P08-13 
Vibration detection 
threshold of adaptive 
notch filter 
Set range：0-7 
This parameter sets the vibration detection sensitivity of adaptive 
notch filter, and the smaller the parameter value, the more sensitive 
the detection sensitivity is 
P08-17  Speed monitor 
0: TURN OFF Speed Observer   
1: TURN ON SPEED OBSERVER   
2: Speed, Torque Observer 
P08-19 
Feedback speed low-pass 
filter constant 
Set range：0-25.00，Unit：ms 
Feedback speed low-pass filter time constant, when the motor 
running when there is a howling, the value can be set up properly"""

import re

def extract_parameter_from_text(text):
    """Extract individual parameters from sample text"""
    
    # Split by parameter pattern
    param_sections = re.split(r'(P\d{2}-\d{2})', text)
    
    parameters = {}
    
    for i in range(1, len(param_sections), 2):  # Skip every other (non-parameter sections)
        if i + 1 < len(param_sections):
            param_code = param_sections[i].strip()
            param_content = param_sections[i + 1].strip()
            
            lines = [line.strip() for line in param_content.split('\n') if line.strip()]
            
            # Find parameter name (before "Set range")
            name_lines = []
            desc_lines = []
            in_description = False
            
            for line in lines:
                if line.startswith('Set range') or line.startswith('0:') or line.startswith('1:') or line.startswith('2:'):
                    in_description = True
                    continue
                elif in_description:
                    desc_lines.append(line)
                else:
                    name_lines.append(line)
            
            parameter_name = ' '.join(name_lines)
            description = ' '.join(desc_lines)
            
            parameters[param_code] = {
                'name': parameter_name,
                'description': description
            }
    
    return parameters

# Test the extraction
params = extract_parameter_from_text(sample_text)

for param_code, info in params.items():
    print(f"\n{param_code}:")
    print(f"Name: {info['name']}")
    print(f"Description: {info['description']}")