#!/usr/bin/env python3
"""
PhoneSee OSINT Module
Created by Raj Gautam
Version: 1.0.0

This module handles OSINT (Open Source Intelligence) gathering
for phone numbers using public data sources only.
"""

import os
import json
import hashlib
import requests
from typing import Dict, Any, Optional, List
from datetime import datetime
from pathlib import Path

class OSINTModule:
    """OSINT Module for PhoneSee"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.timeout = self.config.get("settings", {}).get("timeout", 15)
        self.results = {}
        
        # Load API keys from environment
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.google_search_engine_id = os.getenv("GOOGLE_SEARCH_ENGINE_ID")
        self.hunter_api_key = os.getenv("HUNTER_API_KEY")
        self.clearbit_api_key = os.getenv("CLEARBIT_API_KEY")
    
    def search_google(self, phone_number: str) -> Dict[str, Any]:
        """
        Search Google for phone number
        Returns public search results
        """
        if not self.google_api_key or not self.google_search_engine_id:
            return {"error": "Google API not configured"}
        
        try:
            url = "https://www.googleapis.com/customsearch/v1"
            params = {
                "key": self.google_api_key,
                "cx": self.google_search_engine_id,
                "q": f'"{phone_number}"',
                "num": 5
            }
            
            response = requests.get(url, params=params, timeout=self.timeout)
            if response.status_code == 200:
                data = response.json()
                results = []
                for item in data.get("items", []):
                    results.append({
                        "title": item.get("title", ""),
                        "link": item.get("link", ""),
                        "snippet": item.get("snippet", "")
                    })
                return {
                    "found": len(results) > 0,
                    "results_count": len(results),
                    "results": results
                }
            else:
                return {"error": f"Google API error: {response.status_code}"}
        
        except Exception as e:
            return {"error": str(e)}
    
    def search_hunter(self, phone_number: str) -> Dict[str, Any]:
        """
        Search Hunter.io for email associated with phone
        """
        if not self.hunter_api_key:
            return {"error": "Hunter.io API not configured"}
        
        try:
            url = "https://api.hunter.io/v2/domain-search"
            # Note: Hunter.io searches by domain, not phone
            # This is a placeholder for demonstration
            return {"found": False, "results": []}
        
        except Exception as e:
            return {"error": str(e)}
    
    def check_public_directories(self, phone_number: str) -> Dict[str, Any]:
        """
        Check public directories (mock implementation)
        """
        # Generate deterministic mock results
        hash_val = int(hashlib.md5(phone_number.encode()).hexdigest(), 16)
        
        directories = {
            "whitepages": hash_val % 3 == 0,
            "spokeo": hash_val % 4 == 0,
            "beenverified": hash_val % 5 == 0,
            "pipl": hash_val % 6 == 0,
            "anywho": hash_val % 7 == 0,
            "411": hash_val % 8 == 0
        }
        
        found_dirs = [name for name, found in directories.items() if found]
        
        return {
            "found": len(found_dirs) > 0,
            "directories": found_dirs,
            "total_checked": len(directories)
        }
    
    def get_domain_info(self, phone_number: str) -> Dict[str, Any]:
        """
        Get domain information if phone number is associated with any domain
        """
        # Mock implementation
        hash_val = int(hashlib.md5(phone_number.encode()).hexdigest(), 16)
        
        if hash_val % 4 == 0:
            return {
                "found": True,
                "domains": ["example.com", "business.in"],
                "registrar": ["GoDaddy", "Namecheap"][hash_val % 2],
                "created": f"20{hash_val % 20:02d}-{hash_val % 12 + 1:02d}-{hash_val % 28 + 1:02d}"
            }
        
        return {"found": False, "domains": []}
    
    def check_business_listings(self, phone_number: str) -> Dict[str, Any]:
        """
        Check business listings (Google My Business, Yelp, etc.)
        """
        # Mock implementation
        hash_val = int(hashlib.md5(phone_number.encode()).hexdigest(), 16)
        
        listings = {
            "google_business": hash_val % 3 == 0,
            "yelp": hash_val % 4 == 0,
            "yellow_pages": hash_val % 5 == 0,
            "justdial": hash_val % 3 == 0,
            "sulekha": hash_val % 4 == 0
        }
        
        found_listings = [name for name, found in listings.items() if found]
        
        return {
            "found": len(found_listings) > 0,
            "listings": found_listings,
            "business_name": f"Business {hash_val % 1000}" if found_listings else None
        }
    
    def gather_osint(self, phone_number: str) -> Dict[str, Any]:
        """
        Gather comprehensive OSINT data
        """
        osint_data = {
            "google_search": self.search_google(phone_number),
            "public_directories": self.check_public_directories(phone_number),
            "domain_info": self.get_domain_info(phone_number),
            "business_listings": self.check_business_listings(phone_number),
            "timestamp": datetime.now().isoformat()
        }
        
        return osint_data
    
    def generate_osint_summary(self, osint_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate summary from OSINT data
        """
        summary = {
            "total_sources_checked": 4,
            "sources_found": 0,
            "risk_indicators": [],
            "confidence_score": 0
        }
        
        # Check Google search
        if "error" not in osint_data.get("google_search", {}):
            if osint_data["google_search"].get("found"):
                summary["sources_found"] += 1
                summary["confidence_score"] += 25
        
        # Check public directories
        if "error" not in osint_data.get("public_directories", {}):
            if osint_data["public_directories"].get("found"):
                summary["sources_found"] += 1
                summary["confidence_score"] += 25
                if len(osint_data["public_directories"].get("directories", [])) > 2:
                    summary["risk_indicators"].append("Multiple public directory listings")
        
        # Check domain info
        if "error" not in osint_data.get("domain_info", {}):
            if osint_data["domain_info"].get("found"):
                summary["sources_found"] += 1
                summary["confidence_score"] += 25
                summary["risk_indicators"].append("Associated with registered domains")
        
        # Check business listings
        if "error" not in osint_data.get("business_listings", {}):
            if osint_data["business_listings"].get("found"):
                summary["sources_found"] += 1
                summary["confidence_score"] += 25
                if osint_data["business_listings"].get("business_name"):
                    summary["risk_indicators"].append("Registered business listing found")
        
        return summary

# Main entry point for testing
if __name__ == "__main__":
    osint = OSINTModule()
    test_number = "+919876543210"
    
    print("PhoneSee OSINT Module Test")
    print(f"Testing number: {test_number}\n")
    
    results = osint.gather_osint(test_number)
    print(json.dumps(results, indent=2))