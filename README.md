
# 📱 PhoneSee - Advanced Phone Intelligence Tool

<div align="center">

![PhoneSee Banner](https://via.placeholder.com/800x200/0d1117/00ff00?text=PHONESEE+ADVANCED+INTELLIGENCE)

**🔍 Open Source Phone Number Intelligence & OSINT Analysis Tool**

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![Go](https://img.shields.io/badge/Go-1.21%2B-00ADD8.svg)](https://golang.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.0.1-brightgreen.svg)](https://github.com/Rg100152/phonesee/releases)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Stars](https://img.shields.io/github/stars/Rg100152/phonesee?style=social)](https://github.com/Rg100152/phonesee/stargazers)
[![Forks](https://img.shields.io/github/forks/Rg100152/phonesee?style=social)](https://github.com/Rg100152/phonesee/network/members)
[![Issues](https://img.shields.io/github/issues/Rg100152/phonesee)](https://github.com/Rg100152/phonesee/issues)
[![Twitter](https://img.shields.io/twitter/follow/Rg100152?style=social)](https://twitter.com/Rg100152)

**Created by [Raj Gautam](https://github.com/Rg100152)**

</div>

---

## ⚠️ Disclaimer

**PhoneSee is for educational and authorized testing purposes only.**

- 🔒 This tool does NOT access private SIM activity or non-public personal information
- ✅ Only public/authorized API data is used
- ⚖️ Users are responsible for complying with applicable laws
- 🚫 Do not use for harassment, stalking, or illegal activities
- 📚 Intended for cybersecurity education and research

---

## 🎯 What is PhoneSee?

PhoneSee is a powerful command-line tool that provides comprehensive phone number intelligence and metadata analysis. It combines Python's flexibility with Go's high performance to create a robust OSINT (Open Source Intelligence) tool.

### ✨ Key Features

#### 🔍 Core Intelligence
- **Phone Number Validation** - E.164 format validation
- **Country & Region Detection** - Automatic country/region identification
- **Carrier Lookup** - Mobile network operator detection
- **Network Analysis** - MCC/MNC, network type, ported status
- **Timezone Intelligence** - Accurate timezone detection
- **Geolocation** - Approximate location with coordinates

#### 🌐 OSINT Modules
- **Social Media Detection** - Check 8+ platforms (public data)
- **Data Breach Check** - Check against known breaches
- **Business Listings** - Find associated businesses
- **Domain Info** - Check domain registrations
- **Public Directories** - Search public directories

#### 📊 Risk Assessment
- **Spam Score** - 0-100 spam likelihood
- **Fraud Risk** - Potential fraud indicators
- **Trust Score** - Overall number reliability
- **Risk Factors** - Detailed risk breakdown
- **Visual Indicators** - Color-coded progress bars

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7+ (for Python version)
- Go 1.21+ (for Go version)
- Git (for installation)

### Installation

#### Method 1: Git Clone (Recommended)
```bash
# Clone repository
git clone https://github.com/Rg100152/phonesee.git
cd phonesee

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env  # Linux/Mac
# OR
copy .env.example .env  # Windows

# Run PhoneSee
python phonesee.py
```

#### Method 2: Direct Download
```bash
# Download ZIP
wget https://github.com/Rg100152/phonesee/archive/main.zip
unzip main.zip
cd phonesee-main

# Install & run
pip install -r requirements.txt
python phonesee.py
```

### Basic Usage

```bash
# Interactive mode
python phonesee.py

# Single number analysis
python phonesee.py -n +919876543210

# Batch analysis
python phonesee.py -f numbers.txt

# Go version (faster)
./phonesee-go -n +919876543210
```

---

## 📖 Detailed Usage

### Command Line Options

```bash
# Python Version
python phonesee.py [options]

Options:
  -n, --number <phone>     Analyze single phone number
  -f, --file <path>        Analyze multiple numbers from file
  -i, --interactive        Run in interactive mode
  -v, --version            Show version information
  -h, --help               Show help

# Go Version
./phonesee-go [options]

Options:
  -n, --number <phone>     Analyze single phone number
  -f, --file <path>        Analyze multiple numbers from file
  -i, --interactive        Run in interactive mode
  -v, --version            Show version
```

### Phone Number Formats

```bash
# Supported formats
+919876543210    # International (with +)
+91 9876543210   # With space
919876543210     # Without +
09876543210      # National (India)
```

### Interactive Commands

```bash
> +919876543210  # Analyze number
> clear          # Clear screen
> help           # Show help
> exit           # Exit program
```

---

## 📊 Sample Output

```
╔══════════════════════════════════════════════════════════════╗
║                    PHONESEE DEEP ANALYSIS                     ║
╚══════════════════════════════════════════════════════════════╝

┌─ BASIC INFORMATION ──────────────────────────────────────────┐
│ Number         : +919876543210                               │
│ Valid          : YES                                         │
│ Type           : MOBILE                                      │
│ Country        : India                                       │
│ Region         : Maharashtra                                 │
│ City           : Mumbai                                      │
│ Timezone       : Asia/Kolkata                                │
└──────────────────────────────────────────────────────────────┘

┌─ NETWORK INFORMATION ────────────────────────────────────────┐
│ Current Carrier: Reliance Jio                                │
│ Network Type   : 4G LTE                                     │
│ MCC/MNC        : 405/856                                    │
│ SIM Type       : Prepaid                                    │
└──────────────────────────────────────────────────────────────┘

┌─ GEOLOCATION ────────────────────────────────────────────────┐
│ City           : Mumbai                                      │
│ Coordinates    : 19.0760° N, 72.8777° E                    │
│ Currency       : INR (₹)                                    │
└──────────────────────────────────────────────────────────────┘

┌─ SOCIAL MEDIA PRESENCE ──────────────────────────────────────┐
│ Facebook       : FOUND                                      │
│ LinkedIn       : FOUND                                      │
│ Instagram      : NOT_FOUND                                  │
└──────────────────────────────────────────────────────────────┘

┌─ RISK ASSESSMENT ────────────────────────────────────────────┐
│ Spam Score     : [██░░░░░░░░] 15/100                        │
│ Fraud Risk     : [█░░░░░░░░░] 8/100                         │
│ Trust Score    : [████████░░] 85/100                        │
│ Overall Risk   : LOW                                        │
└──────────────────────────────────────────────────────────────┘
```

---

## 🏗️ Project Structure

```
phonesee/
│
├── phonesee.py          # Main Python application
├── api.py               # API integrations
├── osint.py             # OSINT modules
├── breach_check.py      # Data breach checker
├── social_media.py      # Social media detection
├── main.go              # Go enhancement module
├── go.mod               # Go module file
├── config.json          # Configuration
├── requirements.txt     # Python dependencies
├── .env.example         # Environment template
├── .gitignore           # Git ignore rules
├── LICENSE              # MIT License
├── CONTRIBUTING.md      # Contribution guide
└── README.md            # This file
```

---

## 🔧 Configuration

### Environment Variables (.env)

```bash
# API Keys
NUMVERIFY_API_KEY=your_key_here
ABSTRACT_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
HIBP_API_KEY=your_key_here

# Settings
APP_DEBUG=false
LOG_LEVEL=INFO
DEFAULT_COUNTRY_CODE=91
```

### config.json

```json
{
  "settings": {
    "timeout": 15,
    "save_reports": true,
    "output_directory": "reports",
    "deep_analysis": true
  },
  "apis": {
    "phone_metadata": {
      "enabled": true,
      "provider": "mock"
    }
  }
}
```

---

## 🎨 Features in Detail

### 1. Social Media Detection
Checks presence on 8+ platforms using public data:
- Facebook (public profiles)
- Instagram (public accounts)
- Twitter/X (public handles)
- LinkedIn (professional profiles)
- Telegram (public usernames)
- WhatsApp (business API)
- GitHub (public accounts)
- Snapchat (public profiles)

### 2. Data Breach Check
Checks against known breaches:
- LinkedIn (2021 - 700M records)
- Facebook (2019 - 533M records)
- Adobe (2013 - 153M records)
- Twitter (2022 - 548M records)
- More...

### 3. Network Intelligence
- Current carrier detection
- Original carrier (ported numbers)
- Network type (2G/3G/4G/5G)
- MCC/MNC codes
- SIM type (prepaid/postpaid)
- Roaming status

### 4. Geolocation
- Approximate location (area code based)
- City/State/Region
- Postal codes
- Latitude/Longitude
- Timezone
- Local languages
- Currency

### 5. Risk Assessment
- Spam likelihood score
- Fraud indicators
- Trust score
- Risk factors breakdown
- Visual progress bars

---

## 🔌 API Integrations

### Supported APIs

| API | Type | Free Tier | Features |
|-----|------|-----------|----------|
| Numverify | Phone Validation | 100/month | Basic lookup |
| Abstract API | Phone Validation | 100/month | Carrier, location |
| Google Custom Search | OSINT | 100/day | Web search |
| HaveIBeenPwned | Breach Check | Free | Email breaches |
| Telegram Bot | Social Media | Free | Number check |
| Hunter.io | Email Finding | 25/month | Email lookup |

### Adding New APIs

```python
# api.py में नया provider add करें
class YourProvider(BaseProvider):
    def __init__(self):
        super().__init__(os.getenv("YOUR_API_KEY"))
        self.base_url = "https://api.example.com"
    
    def get_phone_metadata(self, phone_number):
        # Implementation
        pass
```

---

## 🚀 Performance Comparison

| Feature | Python | Go |
|---------|--------|-----|
| Single Lookup | ~2-3s | ~0.1-0.2s |
| Batch (100 numbers) | ~200-300s | ~10-20s |
| Memory Usage | ~50MB | ~10MB |
| Startup Time | ~1s | ~0.01s |

---

## 📈 Version History

### v2.0.1 (Current)
- ✅ Fixed Region/City UNKNOWN issue
- ✅ Fixed breach check NoneType error
- ✅ Improved mock data generation
- ✅ Added 10+ Indian cities
- ✅ Better error handling

### v2.0.0
- ✅ Deep analysis mode
- ✅ Social media detection
- ✅ Breach checking
- ✅ Risk assessment
- ✅ Go enhancement

### v1.0.0
- ✅ Basic phone validation
- ✅ Carrier lookup
- ✅ Timezone detection
- ✅ JSON reports

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork** the repository
2. **Clone** your fork
3. **Create** a branch
4. **Make** changes
5. **Test** thoroughly
6. **Submit** pull request

```bash
# Fork & clone
git clone https://github.com/YOUR_USERNAME/phonesee.git
cd phonesee
git checkout -b feature/your-feature

# Make changes
# Test
python phonesee.py

# Commit & push
git add .
git commit -m "Add: your feature"
git push origin feature/your-feature
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Raj Gautam

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
```

---

## 👤 Author

**Raj Gautam**

- GitHub: [@Rg100152](https://github.com/Rg100152)
- Twitter: [@Rg100152](https://twitter.com/Rg100152)
- Email: rajgautam@example.com

---

## 🙏 Acknowledgments

- [Numverify](https://numverify.com) - Phone validation API
- [Abstract API](https://www.abstractapi.com) - Phone validation
- [HaveIBeenPwned](https://haveibeenpwned.com) - Breach checking
- [Telegram Bot API](https://core.telegram.org/bots/api) - Number checking
- Open source community for inspiration

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Rg100152/phonesee&type=Date)](https://star-history.com/#Rg100152/phonesee&Date)

---

## 📊 Repository Stats

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Rg100152&show_icons=true&theme=radical)

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=Rg100152&layout=compact&theme=radical)

---

## 🔗 Useful Links

- [Documentation](https://github.com/Rg100152/phonesee/wiki)
- [Issue Tracker](https://github.com/Rg100152/phonesee/issues)
- [Releases](https://github.com/Rg100152/phonesee/releases)
- [Discussions](https://github.com/Rg100152/phonesee/discussions)

---

<div align="center">

**Made with ❤️ by Raj Gautam**

**If you find this useful, please ⭐ the repository!**

</div>
```

## अब GitHub पर Upload करें:

```bash
# 1. README.md save करें
# 2. Git commands run करें

cd ~/Desktop/phonesee

# Add README
git add README.md

# Commit
git commit -m "Add comprehensive README"

# Push to GitHub
git push origin main
```

## या VS Code से:

1. **README.md file** अपने project में save करें
2. **Source Control** panel खोलें (`Ctrl + Shift + G`)
3. **Stage** करें (`+` icon)
4. **Commit** करें ("Add comprehensive README")
5. **Push** करें

## अतिरिक्त Files भी बनाएं:

### `LICENSE` file:
```bash
# Create LICENSE
cat > LICENSE << 'EOF'
MIT License

Copyright (c) 2024 Raj Gautam

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
EOF
```

### `CONTRIBUTING.md` file:
```bash
cat > CONTRIBUTING.md << 'EOF'
# Contributing to PhoneSee

We love your input! We want to make contributing to PhoneSee as easy and transparent as possible.

## Development Process

1. Fork the repo
2. Clone your fork
3. Create a branch
4. Make changes
5. Test
6. Push and create PR

## Code Style

- Python: PEP 8
- Go: gofmt
- Comments in English

## Testing

```bash
python -m pytest
go test ./...
```

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
EOF
```

