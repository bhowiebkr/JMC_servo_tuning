# JMC Servo Parameter Extraction & Custom Tuning Guide Generator

A Python toolkit for extracting JMC servo parameters from HTML manuals and XML exports, then generating custom servo tuning documentation based on your specific configuration.

## 🎯 What This Tool Does

1. **Extracts parameters** from JMC servo HTML manuals (P##-## format)
2. **Merges XML export data** with manual descriptions  
3. **Generates custom tuning guides** based on your actual servo configuration
4. **Provides expert tuning recommendations** for eliminating servo buzzing and optimizing performance

## 📂 Repository Contents

```
JMC_servo_tuning/
├── README.md                           # This guide
├── JMC_Servo_Tuning_Guide.md          # Expert servo tuning methodology
├── extract_parameters.py              # HTML parameter extraction tool
├── merge_parameters.py                 # XML+JSON merger & report generator
├── requirements.txt                    # Python dependencies
├── run.bat                            # Windows quick-start script
└── examples/
    ├── jmc_parameters_with_values.json # Example merged parameter file
    └── JMC_servo_tuning/               # Example source files
        ├── JMC JAND Series AC Servo Driver User Manual (202011).html
        └── RY_Parameter File0903.xml
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- JMC servo HTML manual file
- JMC servo XML parameter export (optional but recommended)

### Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/JMC_servo_tuning.git
   cd JMC_servo_tuning
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Windows Users - One-Click Setup
Simply double-click `run.bat` to automatically install dependencies and run the extraction process.

## 📋 Step-by-Step Usage Guide

### Step 1: Extract Parameters from HTML Manual

```bash
python extract_parameters.py "path/to/your/manual.html"
```

**What this does:**
- Scans HTML manual for all P##-## parameters
- Extracts parameter names, descriptions, and specifications
- Outputs: `jmc_parameters_extracted.json`

**Example:**
```bash
python extract_parameters.py "examples/JMC_servo_tuning/JMC JAND Series AC Servo Driver User Manual (202011).html"
```

### Step 2: Merge with Your Servo's XML Export (Recommended)

```bash
python merge_parameters.py extracted_file.json your_servo_export.xml
```

**What this does:**
- Combines manual descriptions with your actual servo values
- Creates comprehensive parameter database
- Generates custom tuning analysis
- Outputs: `servo_parameters_merged.json` and analysis report

**Example:**
```bash
python merge_parameters.py jmc_parameters_extracted.json "examples/JMC_servo_tuning/RY_Parameter File0903.xml"
```

### Step 3: Generate Custom Tuning Guide

The merge process automatically generates:
- **Merged JSON file** with your current parameter values + manual descriptions
- **Analysis report** identifying potential buzzing causes
- **Custom recommendations** based on your specific configuration

## 🔧 Understanding the Output

### Generated Files

1. **`jmc_parameters_extracted.json`** - Raw extraction from HTML manual
2. **`servo_parameters_merged.json`** - Your servo data + manual descriptions  
3. **`parameter_analysis_report.md`** - Custom tuning recommendations

### Key Information Extracted

Each parameter includes:
- **Parameter code** (e.g., P01-02, P08-13)
- **Parameter name** and description
- **Your current value** (from XML export)
- **Setting range** and units
- **Tuning recommendations** specific to your configuration

## 🎛️ Common Use Cases

### Case 1: Servo Buzzing/Vibration Issues
The tool will identify parameters like:
- **P01-02** (Manual vs. Automatic rigidity mode)
- **P01-03** (Rigidity level settings)  
- **P08-XX** (Filtering and vibration suppression)

### Case 2: Performance Optimization
Analysis includes:
- **Position loop gains** (P02-XX series)
- **Speed loop parameters** (P02-XX series)
- **Inertia ratio settings** (P01-04)

### Case 3: System Integration
Documentation for:
- **Communication settings** (P00-XX series)
- **I/O configuration** 
- **Brake and safety parameters**

## 📖 Expert Tuning Guide

The included `JMC_Servo_Tuning_Guide.md` provides:

- **Comprehensive tuning philosophy** for JMC servos
- **Step-by-step buzzing elimination** procedures  
- **Parameter optimization strategies**
- **Troubleshooting common issues**
- **Professional tuning methodology**

## 🛠️ Advanced Usage

### Extracting from Multiple Manuals
```bash
python extract_parameters.py manual1.html
python extract_parameters.py manual2.html
# Merge results as needed
```

### Batch Processing XML Files
```bash
for file in *.xml; do
    python merge_parameters.py base_parameters.json "$file"
done
```

### Custom Output Locations
Both scripts support custom output paths:
```bash
python extract_parameters.py manual.html --output custom_params.json
python merge_parameters.py params.json servo.xml --output custom_merged.json
```

## 📝 File Format Details

### HTML Manual Requirements
- JMC servo manual in HTML format
- Parameters must follow P##-## naming convention
- Typically generated from PDF conversion

### XML Export Requirements  
- Export from JMC servo configuration software
- Must contain parameter elements with current values
- Standard JMC XML export format

## ⚠️ Troubleshooting

### Common Issues

**"No parameters found in HTML"**
- Verify HTML file is a JMC servo manual
- Check file encoding (UTF-8 recommended)
- Ensure parameters use P##-## format

**"XML parsing failed"**
- Verify XML file is valid JMC export
- Check file permissions
- Ensure XML contains parameter data

**"Dependencies not found"**
- Run: `pip install -r requirements.txt`
- Ensure Python 3.7+ is installed

### Getting Help

1. Check the example files in `examples/` directory
2. Review `JMC_Servo_Tuning_Guide.md` for parameter details
3. Open an issue with:
   - Error message
   - File types you're processing
   - Python version

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

### Areas for Contribution
- Additional servo manufacturer support
- GUI interface development
- Enhanced parameter analysis algorithms
- Documentation translations

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- JMC servo documentation and parameter specifications
- Python BeautifulSoup and lxml communities
- Servo tuning expertise from industrial automation field

## 📞 Support

For questions, issues, or contributions:
- **GitHub Issues**: Report bugs or request features
- **Discussions**: Share tuning experiences and tips
- **Wiki**: Community-maintained servo tuning knowledge

---

**Made with ❤️ for the industrial automation community**

*Transform your servo tuning from trial-and-error to data-driven precision.*