#!/usr/bin/env python3
"""
PhoneSee API Handler
Created by Raj Gautam
Version: 1.0.0
Open Source Project

This module handles all external API integrations for PhoneSee.
Supports multiple providers for phone metadata and reputation lookup.
"""

import os
import json
import requests
from typing import Dict, Any, Optional, List
from pathlib import Path
from abc import ABC, abstractmethod
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class APIError(Exception):
    """Custom exception for API errors"""
    pass

class BaseProvider(ABC):
    """Abstract base class for all providers"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
        self.timeout = 10
    
    @abstractmethod
    def get_phone_metadata(self, phone_number: str) -> Dict[str, Any]:
        """Get phone metadata from provider"""
        pass
    
    @abstractmethod
    def get_reputation(self, phone_number: str) -> Dict[str, Any]:
        """Get reputation data from provider"""
        pass
    
    def _make_request(self, url: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Make HTTP request with error handling
        """
        try:
            response = requests.get(
                url,
                params=params,
                timeout=self.timeout,
                headers={"User-Agent": f"PhoneSee/1.0.0"}
            )
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                raise APIError("Invalid API key")
            elif response.status_code == 404:
                raise APIError("Resource not found")
            elif response.status_code == 429:
                raise APIError("Rate limit exceeded")
            else:
                raise APIError(f"API error: {response.status_code}")
                
        except requests.exceptions.Timeout:
            raise APIError("Request timeout")
        except requests.exceptions.ConnectionError:
            raise APIError("Connection error")
        except requests.exceptions.RequestException as e:
            raise APIError(f"Request failed: {str(e)}")

class NumverifyProvider(BaseProvider):
    """Numverify API Provider for phone metadata"""
    
    def __init__(self):
        super().__init__(os.getenv("NUMVERIFY_API_KEY"))
        self.base_url = "http://apilayer.net/api/validate"
    
    def get_phone_metadata(self, phone_number: str) -> Dict[str, Any]:
        """Get phone metadata from Numverify"""
        if not self.api_key:
            raise APIError("Numverify API key not configured")
        
        params = {
            "access_key": self.api_key,
            "number": phone_number,
            "format": 1
        }
        
        data = self._make_request(self.base_url, params)
        
        # Normalize response to PhoneSee format
        return {
            "valid": data.get("valid", False),
            "type": self._normalize_type(data.get("line_type", "UNKNOWN")),
            "country": data.get("country_name", "UNKNOWN"),
            "region": data.get("location", "UNKNOWN"),
            "carrier": data.get("carrier", "UNKNOWN"),
            "timezone": "UNKNOWN",  # Numverify doesn't provide timezone
            "country_code": data.get("country_code", ""),
            "local_format": data.get("local_format", ""),
            "international_format": data.get("international_format", phone_number),
        }
    
    def get_reputation(self, phone_number: str) -> Dict[str, Any]:
        """Numverify doesn't provide reputation data"""
        return {
            "spam_risk": "UNKNOWN",
            "reports": 0,
            "confidence": 0
        }
    
    def _normalize_type(self, line_type: str) -> str:
        """Normalize line type to standard format"""
        type_mapping = {
            "mobile": "MOBILE",
            "landline": "LANDLINE",
            "fixed_line": "LANDLINE",
            "tollfree": "TOLL_FREE",
            "premium": "PREMIUM",
            "voip": "VOIP",
            "unknown": "UNKNOWN",
            "special_services": "SPECIAL_SERVICES"
        }
        return type_mapping.get(line_type.lower(), "UNKNOWN")

class AbstractAPIProvider(BaseProvider):
    """Abstract API Provider for phone validation"""
    
    def __init__(self):
        super().__init__(os.getenv("ABSTRACT_API_KEY"))
        self.base_url = "https://phonevalidation.abstractapi.com/v1/"
    
    def get_phone_metadata(self, phone_number: str) -> Dict[str, Any]:
        """Get phone metadata from Abstract API"""
        if not self.api_key:
            raise APIError("Abstract API key not configured")
        
        params = {
            "api_key": self.api_key,
            "phone": phone_number
        }
        
        data = self._make_request(self.base_url, params)
        
        # Normalize response to PhoneSee format
        return {
            "valid": data.get("valid", False),
            "type": self._normalize_type(data.get("type", "UNKNOWN")),
            "country": data.get("country", {}).get("name", "UNKNOWN"),
            "region": data.get("location", "UNKNOWN"),
            "carrier": data.get("carrier", "UNKNOWN"),
            "timezone": "UNKNOWN",
            "country_code": data.get("country", {}).get("code", ""),
            "local_format": data.get("local_format", ""),
            "international_format": data.get("international_format", phone_number),
        }
    
    def get_reputation(self, phone_number: str) -> Dict[str, Any]:
        """Abstract API doesn't provide reputation data"""
        return {
            "spam_risk": "UNKNOWN",
            "reports": 0,
            "confidence": 0
        }
    
    def _normalize_type(self, phone_type: str) -> str:
        """Normalize phone type to standard format"""
        type_mapping = {
            "mobile": "MOBILE",
            "landline": "LANDLINE",
            "fixed_line": "LANDLINE",
            "voip": "VOIP",
            "toll_free": "TOLL_FREE",
            "premium": "PREMIUM",
            "unknown": "UNKNOWN",
            "invalid": "UNKNOWN"
        }
        return type_mapping.get(phone_type.lower(), "UNKNOWN")

class TruecallerProvider(BaseProvider):
    """Truecaller Provider (Unofficial - Educational Use Only)"""
    
    def __init__(self):
        super().__init__(None)  # Truecaller uses session-based auth
        self.installation_id = os.getenv("TRUECALLER_INSTALLATION_ID")
    
    def get_phone_metadata(self, phone_number: str) -> Dict[str, Any]:
        """
        Get phone metadata from Truecaller
        Note: This is for educational purposes only
        Requires valid Truecaller session
        """
        if not self.installation_id:
            raise APIError("Truecaller Installation ID not configured")
        
        # This is a placeholder - actual implementation requires Truecaller session
        # For educational purposes, return UNKNOWN values
        return {
            "valid": True,
            "type": "UNKNOWN",
            "country": "UNKNOWN",
            "region": "UNKNOWN",
            "carrier": "UNKNOWN",
            "timezone": "UNKNOWN",
        }
    
    def get_reputation(self, phone_number: str) -> Dict[str, Any]:
        """Truecaller reputation data (educational use)"""
        return {
            "spam_risk": "UNKNOWN",
            "reports": 0,
            "confidence": 0
        }

class MockProvider(BaseProvider):
    """Mock Provider for testing and development"""
    
    def __init__(self):
        super().__init__("mock_key")
    
    def get_phone_metadata(self, phone_number: str) -> Dict[str, Any]:
        """Return mock data for testing"""
        # Simple country detection from country code
        country_code = phone_number[1:3] if phone_number.startswith('+') else ""
        
        country_map = {
            "91": ("India", "Asia/Kolkata"),
            "1": ("United States", "America/New_York"),
            "44": ("United Kingdom", "Europe/London"),
            "86": ("China", "Asia/Shanghai"),
            "81": ("Japan", "Asia/Tokyo"),
            "49": ("Germany", "Europe/Berlin"),
            "33": ("France", "Europe/Paris"),
            "7": ("Russia", "Europe/Moscow"),
            "55": ("Brazil", "America/Sao_Paulo"),
            "61": ("Australia", "Australia/Sydney"),
        }
        
        country, timezone = country_map.get(country_code, ("UNKNOWN", "UNKNOWN"))
        
        return {
            "valid": True,
            "type": "MOBILE",
            "country": country,
            "region": "UNKNOWN",
            "carrier": "UNKNOWN",
            "timezone": timezone,
            "country_code": country_code,
            "local_format": phone_number[3:],
            "international_format": phone_number,
        }
    
    def get_reputation(self, phone_number: str) -> Dict[str, Any]:
        """Return mock reputation data"""
        # Return random-looking but deterministic data
        import hashlib
        hash_val = int(hashlib.md5(phone_number.encode()).hexdigest(), 16)
        
        spam_risk = ["LOW", "MEDIUM", "HIGH"][hash_val % 3]
        reports = hash_val % 100
        confidence = 50 + (hash_val % 50)
        
        return {
            "spam_risk": spam_risk,
            "reports": reports,
            "confidence": confidence
        }

class APIHandler:
    """Main API Handler for PhoneSee"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.providers = {}
        self.metadata_provider = None
        self.reputation_provider = None
        
        # Initialize providers
        self._init_providers()
    
    def _init_providers(self):
        """Initialize all available providers"""
        # Register all providers
        self.providers = {
            "numverify": NumverifyProvider(),
            "abstract": AbstractAPIProvider(),
            "truecaller": TruecallerProvider(),
            "mock": MockProvider()
        }
        
        # Set metadata provider from config
        metadata_config = self.config.get("apis", {}).get("phone_metadata", {})
        if metadata_config.get("enabled", True):
            provider_name = metadata_config.get("provider", "mock")
            self.metadata_provider = self.providers.get(provider_name, self.providers["mock"])
        
        # Set reputation provider from config
        reputation_config = self.config.get("apis", {}).get("reputation", {})
        if reputation_config.get("enabled", False):
            provider_name = reputation_config.get("provider", "mock")
            self.reputation_provider = self.providers.get(provider_name)
    
    def get_phone_metadata(self, phone_number: str) -> Dict[str, Any]:
        """
        Get phone metadata from configured provider
        Falls back to mock if provider fails
        """
        if not self.metadata_provider:
            return self._get_default_metadata()
        
        try:
            return self.metadata_provider.get_phone_metadata(phone_number)
        except APIError as e:
            print(f"[!] Metadata API error: {e}")
            print("[*] Falling back to mock data...")
            return self.providers["mock"].get_phone_metadata(phone_number)
        except Exception as e:
            print(f"[!] Unexpected error: {e}")
            return self._get_default_metadata()
    
    def get_reputation(self, phone_number: str) -> Dict[str, Any]:
        """
        Get reputation data from configured provider
        Returns default if provider not configured
        """
        if not self.reputation_provider:
            return self._get_default_reputation()
        
        try:
            return self.reputation_provider.get_reputation(phone_number)
        except APIError as e:
            print(f"[!] Reputation API error: {e}")
            return self._get_default_reputation()
        except Exception as e:
            print(f"[!] Unexpected error: {e}")
            return self._get_default_reputation()
    
    def _get_default_metadata(self) -> Dict[str, Any]:
        """Get default metadata when no provider available"""
        return {
            "valid": False,
            "type": "UNKNOWN",
            "country": "UNKNOWN",
            "region": "UNKNOWN",
            "carrier": "UNKNOWN",
            "timezone": "UNKNOWN",
        }
    
    def _get_default_reputation(self) -> Dict[str, Any]:
        """Get default reputation when no provider available"""
        return {
            "spam_risk": "UNKNOWN",
            "reports": 0,
            "confidence": 0
        }
    
    def get_available_providers(self) -> List[str]:
        """Get list of available providers"""
        return list(self.providers.keys())
    
    def check_provider_status(self) -> Dict[str, bool]:
        """Check which providers have API keys configured"""
        status = {}
        for name, provider in self.providers.items():
            status[name] = provider.api_key is not None
        return status

class PhoneNumberParser:
    """Utility class for phone number parsing and validation"""
    
    @staticmethod
    def parse_country_code(phone_number: str) -> str:
        """Extract country code from phone number"""
        if not phone_number.startswith('+'):
            return ""
        
        # Common country codes (1-3 digits)
        for length in [3, 2, 1]:
            code = phone_number[1:1+length]
            if PhoneNumberParser.is_valid_country_code(code):
                return code
        
        return phone_number[1:3]  # Default to 2-digit
    
    @staticmethod
    def is_valid_country_code(code: str) -> bool:
        """Check if country code is valid"""
        # This is a simplified validation
        valid_codes = {
            "1", "7", "20", "27", "30", "31", "32", "33", "34", "36",
            "39", "40", "41", "43", "44", "45", "46", "47", "48", "49",
            "51", "52", "53", "54", "55", "56", "57", "58", "60", "61",
            "62", "63", "64", "65", "66", "81", "82", "84", "86", "90",
            "91", "92", "93", "94", "95", "98", "211", "212", "213", "216",
            "218", "220", "221", "222", "223", "224", "225", "226", "227",
            "228", "229", "230", "231", "232", "233", "234", "235", "236",
            "237", "238", "239", "240", "241", "242", "243", "244", "245",
            "246", "247", "248", "249", "250", "251", "252", "253", "254",
            "255", "256", "257", "258", "260", "261", "262", "263", "264",
            "265", "266", "267", "268", "269", "290", "291", "297", "298",
            "299", "350", "351", "352", "353", "354", "355", "356", "357",
            "358", "359", "370", "371", "372", "373", "374", "375", "376",
            "377", "378", "380", "381", "382", "383", "385", "386", "387",
            "389", "420", "421", "423", "500", "501", "502", "503", "504",
            "505", "506", "507", "508", "509", "590", "591", "592", "593",
            "594", "595", "596", "597", "598", "599", "670", "672", "673",
            "674", "675", "676", "677", "678", "679", "680", "681", "682",
            "683", "685", "686", "687", "688", "689", "690", "691", "692",
            "850", "852", "853", "855", "856", "880", "886", "960", "961",
            "962", "963", "964", "965", "966", "967", "968", "970", "971",
            "972", "973", "974", "975", "976", "977", "992", "993", "994",
            "995", "996", "998"
        }
        return code in valid_codes
    
    @staticmethod
    def format_e164(phone_number: str) -> str:
        """Format phone number to E.164 standard"""
        # Remove all non-numeric characters
        digits = ''.join(filter(str.isdigit, phone_number))
        
        # Ensure it starts with country code
        if not phone_number.startswith('+'):
            # Assume local number, add default country code
            digits = "91" + digits.lstrip('0')  # Default to India
        
        return f"+{digits}"
    
    @staticmethod
    def get_number_type(phone_number: str) -> str:
        """Determine phone number type based on pattern"""
        digits = ''.join(filter(str.isdigit, phone_number))
        
        # Mobile numbers typically start with 6-9 in India
        if len(digits) == 10 and digits[0] in "6789":
            return "MOBILE"
        
        # Landline numbers
        if len(digits) == 10 and digits[0] in "2345":
            return "LANDLINE"
        
        # Toll-free numbers
        if digits.startswith("1800") or digits.startswith("800"):
            return "TOLL_FREE"
        
        # Premium numbers
        if digits.startswith("900"):
            return "PREMIUM"
        
        return "UNKNOWN"

# Utility functions for API response processing
def process_api_response(response: Dict[str, Any]) -> Dict[str, Any]:
    """Process and normalize API response"""
    processed = {
        "valid": response.get("valid", False),
        "type": response.get("type", "UNKNOWN"),
        "country": response.get("country", "UNKNOWN"),
        "region": response.get("region", "UNKNOWN"),
        "carrier": response.get("carrier", "UNKNOWN"),
        "timezone": response.get("timezone", "UNKNOWN"),
        "country_code": response.get("country_code", ""),
        "local_format": response.get("local_format", ""),
        "international_format": response.get("international_format", "")
    }
    
    return processed

def merge_responses(primary: Dict[str, Any], secondary: Dict[str, Any]) -> Dict[str, Any]:
    """Merge multiple API responses, preferring non-UNKNOWN values"""
    merged = primary.copy()
    
    for key, value in secondary.items():
        if key not in merged or merged[key] == "UNKNOWN":
            merged[key] = value
    
    return merged

def format_for_display(data: Dict[str, Any]) -> str:
    """Format API response for display"""
    lines = []
    for key, value in data.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                lines.append(f"{key}.{sub_key}: {sub_value}")
        else:
            lines.append(f"{key}: {value}")
    
    return "\n".join(lines)

# Main entry point for testing
if __name__ == "__main__":
    print("PhoneSee API Handler")
    print("Created by Raj Gautam")
    print("Version: 1.0.0")
    print()
    
    # Test API handler
    handler = APIHandler()
    print(f"Available providers: {handler.get_available_providers()}")
    print(f"Provider status: {handler.check_provider_status()}")
    
    # Test phone number parsing
    test_numbers = [
        "+919876543210",
        "+14155552671",
        "+442071838750",
        "9876543210",  # Missing country code
        "+8613800138000"
    ]
    
    print("\nTesting phone number parsing:")
    for number in test_numbers:
        print(f"\n{number}:")
        print(f"  Country code: {PhoneNumberParser.parse_country_code(number)}")
        print(f"  Type: {PhoneNumberParser.get_number_type(number)}")
        print(f"  E.164: {PhoneNumberParser.format_e164(number)}")
        
        # Test mock metadata
        metadata = handler.get_phone_metadata(number)
        print(f"  Metadata: {json.dumps(metadata, indent=2)}")