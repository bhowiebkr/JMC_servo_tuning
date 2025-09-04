#!/usr/bin/env python3
"""
Merge JMC servo parameters from XML export file with extracted manual documentation.
Creates a comprehensive JSON file with actual servo values and manual descriptions.
"""

import xml.etree.ElementTree as ET
import json
from pathlib import Path
from datetime import datetime

def parse_xml_parameters(xml_file_path):
    """
    Parse XML parameter file and extract all parameter information.
    
    Args:
        xml_file_path (str): Path to the XML parameter file
        
    Returns:
        dict: Dictionary of parameters from XML
    """
    print("Parsing XML parameter file...")
    
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        
        xml_parameters = {}
        
        # Find all parameter elements (they start with P and contain digits and dashes)
        for section in root:
            for param_element in section:
                # Check if this looks like a parameter (P##-##)
                if param_element.tag.startswith('P') and '-' in param_element.tag:
                    param_code = param_element.tag
                    
                    # Extract all the parameter information
                    param_info = {}
                    for child in param_element:
                        param_info[child.tag] = child.text if child.text else ""
                    
                    # Structure the data for our use
                    xml_parameters[param_code] = {
                        'code': param_info.get('Code', param_code),
                        'name': param_info.get('Name', 'Unknown'),
                        'current_value': param_info.get('Current_Value', ''),
                        'setting_range': param_info.get('Setting_range', ''),
                        'unit': param_info.get('Unit', ''),
                        'description': param_info.get('Description', ''),
                        'initialize': param_info.get('Initialize', ''),
                        'minimum': param_info.get('Minimum', ''),
                        'maximum': param_info.get('Maximum', ''),
                        'setting_method': param_info.get('Setting_method', ''),
                        'effective_time': param_info.get('Effective_time', '')
                    }
        
        print(f"Found {len(xml_parameters)} parameters in XML file")
        return xml_parameters
        
    except Exception as e:
        print(f"Error parsing XML file: {e}")
        return {}

def load_json_parameters(json_file_path):
    """
    Load existing JSON parameters with manual descriptions.
    
    Args:
        json_file_path (str): Path to the JSON parameter file
        
    Returns:
        dict: Dictionary of parameters from JSON
    """
    print("Loading existing JSON parameters...")
    
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            json_parameters = json.load(f)
        
        print(f"Loaded {len(json_parameters)} parameters from JSON file")
        return json_parameters
        
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return {}

def merge_parameters(xml_params, json_params):
    """
    Merge XML parameters (actual values) with JSON parameters (manual descriptions).
    
    Args:
        xml_params (dict): Parameters from XML file
        json_params (dict): Parameters from JSON file
        
    Returns:
        dict: Merged parameter data
    """
    print("Merging XML and JSON parameters...")
    
    merged_params = {}
    xml_only = []
    json_only = []
    merged_count = 0
    
    # Start with all parameters from JSON (has manual descriptions)
    all_param_codes = set(json_params.keys()) | set(xml_params.keys())
    
    for param_code in sorted(all_param_codes):
        xml_param = xml_params.get(param_code, {})
        json_param = json_params.get(param_code, {})
        
        # Create merged parameter entry
        merged_param = {}
        
        if param_code in xml_params and param_code in json_params:
            # Both sources available - merge intelligently
            merged_param = {
                'name': xml_param.get('name', json_param.get('name', 'Unknown')),
                'setting_range': xml_param.get('setting_range', json_param.get('setting_range', '')),
                'unit': xml_param.get('unit', ''),
                'current_value': xml_param.get('current_value', ''),
                'default_value': xml_param.get('initialize', ''),
                'minimum': xml_param.get('minimum', ''),
                'maximum': xml_param.get('maximum', ''),
                'description': json_param.get('description', 'No description available'),
                'servo_description': xml_param.get('description', ''),
                'setting_method': xml_param.get('setting_method', ''),
                'effective_time': xml_param.get('effective_time', ''),
                'source': 'merged'
            }
            merged_count += 1
            
        elif param_code in xml_params:
            # Only in XML - use XML data
            merged_param = {
                'name': xml_param.get('name', 'Unknown'),
                'setting_range': xml_param.get('setting_range', ''),
                'unit': xml_param.get('unit', ''),
                'current_value': xml_param.get('current_value', ''),
                'default_value': xml_param.get('initialize', ''),
                'minimum': xml_param.get('minimum', ''),
                'maximum': xml_param.get('maximum', ''),
                'description': 'From servo XML - no manual description available',
                'servo_description': xml_param.get('description', ''),
                'setting_method': xml_param.get('setting_method', ''),
                'effective_time': xml_param.get('effective_time', ''),
                'source': 'xml_only'
            }
            xml_only.append(param_code)
            
        elif param_code in json_params:
            # Only in JSON - use JSON data  
            merged_param = {
                'name': json_param.get('name', 'Unknown'),
                'setting_range': json_param.get('setting_range', ''),
                'unit': '',
                'current_value': '',
                'default_value': '',
                'minimum': '',
                'maximum': '',
                'description': json_param.get('description', 'No description available'),
                'servo_description': '',
                'setting_method': '',
                'effective_time': '',
                'source': 'json_only'
            }
            json_only.append(param_code)
        
        merged_params[param_code] = merged_param
    
    print(f"Merge complete:")
    print(f"  - {merged_count} parameters merged from both sources")
    print(f"  - {len(xml_only)} parameters only in XML")
    print(f"  - {len(json_only)} parameters only in JSON")
    print(f"  - {len(merged_params)} total parameters in output")
    
    return merged_params, {
        'merged_count': merged_count,
        'xml_only': xml_only,
        'json_only': json_only,
        'total_count': len(merged_params)
    }

def save_merged_parameters(merged_params, stats, output_file):
    """
    Save merged parameters to JSON file with metadata.
    
    Args:
        merged_params (dict): Merged parameter data
        stats (dict): Merge statistics
        output_file (str): Output file path
    """
    print(f"Saving merged parameters to {output_file}...")
    
    output_data = {
        'metadata': {
            'created': datetime.now().isoformat(),
            'description': 'JMC servo parameters merged from XML export and manual extraction',
            'xml_source': 'RY_Parameter File0903.xml',
            'json_source': 'jmc_parameters_improved.json',
            'merge_statistics': stats
        },
        'parameters': merged_params
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully saved {len(merged_params)} parameters to {output_file}")

def create_summary_report(merged_params, stats):
    """
    Create a summary report of the merge process.
    
    Args:
        merged_params (dict): Merged parameter data
        stats (dict): Merge statistics
    """
    print("Creating summary report...")
    
    # Analyze the merged data
    has_current_value = sum(1 for p in merged_params.values() if p['current_value'])
    has_manual_desc = sum(1 for p in merged_params.values() if p['description'] and p['description'] != 'No description available')
    has_servo_desc = sum(1 for p in merged_params.values() if p['servo_description'])
    has_units = sum(1 for p in merged_params.values() if p['unit'])
    
    report = f"""
# JMC Servo Parameter Merge Summary Report

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Merge Statistics
- **Total Parameters:** {stats['total_count']}
- **Merged from Both Sources:** {stats['merged_count']}
- **XML Only:** {len(stats['xml_only'])}
- **JSON Only:** {len(stats['json_only'])}

## Data Completeness
- **Parameters with Current Values:** {has_current_value} ({has_current_value/stats['total_count']*100:.1f}%)
- **Parameters with Manual Descriptions:** {has_manual_desc} ({has_manual_desc/stats['total_count']*100:.1f}%)
- **Parameters with Servo Descriptions:** {has_servo_desc} ({has_servo_desc/stats['total_count']*100:.1f}%)
- **Parameters with Units:** {has_units} ({has_units/stats['total_count']*100:.1f}%)

## Key Tuning Parameters (Current Values)
"""
    
    # Add key tuning parameters with their current values
    key_params = [
        'P01-03', 'P01-04', 'P02-00', 'P02-01', 'P02-10', 'P02-11',
        'P02-13', 'P02-14', 'P08-11', 'P08-13', 'P08-19', 'P08-20', 'P08-21'
    ]
    
    for param in key_params:
        if param in merged_params:
            p = merged_params[param]
            current = p['current_value'] if p['current_value'] else 'Not Set'
            unit = f" {p['unit']}" if p['unit'] and p['unit'] != '---' else ''
            report += f"- **{param}** ({p['name']}): {current}{unit}\n"
    
    # Add parameters only in XML (might be new/undocumented)
    if stats['xml_only']:
        report += f"\n## Parameters Only in XML ({len(stats['xml_only'])})\n"
        for param in sorted(stats['xml_only'])[:10]:  # Show first 10
            if param in merged_params:
                p = merged_params[param]
                report += f"- **{param}**: {p['name']}\n"
        if len(stats['xml_only']) > 10:
            report += f"... and {len(stats['xml_only']) - 10} more\n"
    
    # Add parameters only in JSON (might be deprecated)
    if stats['json_only']:
        report += f"\n## Parameters Only in JSON ({len(stats['json_only'])})\n"
        for param in sorted(stats['json_only'])[:10]:  # Show first 10
            report += f"- **{param}**\n"
        if len(stats['json_only']) > 10:
            report += f"... and {len(stats['json_only']) - 10} more\n"
    
    report += "\n## Files Created\n"
    report += "- `jmc_parameters_with_values.json`: Complete merged parameter database\n"
    report += "- `parameter_merge_summary.md`: This summary report\n"
    
    # Save the report
    with open('parameter_merge_summary.md', 'w', encoding='utf-8') as f:
        f.write(report)
    
    print("Summary report saved to parameter_merge_summary.md")
    
    # Also print key statistics to console
    print(f"\n=== MERGE SUMMARY ===")
    print(f"Total Parameters: {stats['total_count']}")
    print(f"With Current Values: {has_current_value}")
    print(f"With Manual Descriptions: {has_manual_desc}")
    print(f"Merge Success Rate: {stats['merged_count']/stats['total_count']*100:.1f}%")

def main():
    """Main function to execute the parameter merge process."""
    
    print("JMC Servo Parameter Merger")
    print("=" * 40)
    
    # File paths
    xml_file = Path("JMC_servo_tuning/RY_Parameter File0903.xml")
    json_file = Path("jmc_parameters_improved.json") 
    output_file = "jmc_parameters_with_values.json"
    
    # Check if files exist
    if not xml_file.exists():
        print(f"ERROR: XML file not found: {xml_file}")
        return
    
    if not json_file.exists():
        print(f"ERROR: JSON file not found: {json_file}")
        return
    
    # Step 1: Parse XML parameters
    xml_params = parse_xml_parameters(xml_file)
    if not xml_params:
        print("ERROR: No parameters found in XML file")
        return
    
    # Step 2: Load JSON parameters
    json_params = load_json_parameters(json_file)
    if not json_params:
        print("ERROR: No parameters found in JSON file")
        return
    
    # Step 3: Merge parameters
    merged_params, stats = merge_parameters(xml_params, json_params)
    
    # Step 4: Save merged parameters
    save_merged_parameters(merged_params, stats, output_file)
    
    # Step 5: Create summary report
    create_summary_report(merged_params, stats)
    
    print("\n=== PROCESS COMPLETE ===")
    print(f"Merged parameter file: {output_file}")
    print(f"Summary report: parameter_merge_summary.md")
    print("\nYou now have a comprehensive parameter database with:")
    print("- Actual current values from your servo")
    print("- Detailed descriptions from the manual")
    print("- Accurate ranges and units")
    print("- Clean parameter names")

if __name__ == "__main__":
    main()