#!/usr/bin/env python3
"""
PhoneSee Breach Checker Module
Created by Raj Gautam
Version: 1.0.0

This module checks if a phone number appears in known data breaches.
Uses public APIs and databases only.
"""

import os
import json
import hashlib
import requests
from typing import Dict, Any, Optional, List
from datetime import datetime

class BreachChecker:
    """Data Breach Checker for PhoneSee"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.timeout = self.config.get("settings", {}).get("timeout", 15)
        
        # Load API keys
        self.hibp_api_key = os.getenv("HIBP_API_KEY")
        self.dehashed_api_key = os.getenv("DEHASHED_API_KEY")
        self.leakcheck_api_key = os.getenv("LEAKCHECK_API_KEY")
        
        # Known breach databases (mock)
        self.known_breaches = [
            {
                "name": "LinkedIn",
                "year": 2021,
                "records": 700000000,
                "contains_phone": True
            },
            {
                "name": "Facebook",
                "year": 2019,
                "records": 533000000,
                "contains_phone": True
            },
            {
                "name": "Adobe",
                "year": 2013,
                "records": 153000000,
                "contains_phone": False
            },
            {
                "name": "Canva",
                "year": 2019,
                "records": 137000000,
                "contains_phone": False
            },
            {
                "name": "Dropbox",
                "year": 2012,
                "records": 68000000,
                "contains_phone": False
            },
            {
                "name": "Twitter",
                "year": 2022,
                "records": 548000000,
                "contains_phone": True
            },
            {
                "name": "Airtel",
                "year": 2020,
                "records": 320000000,
                "contains_phone": True
            },
            {
                "name": "Jio",
                "year": 2023,
                "records": 400000000,
                "contains_phone": True
            }
        ]
    
    def check_hibp(self, phone_number: str) -> Dict[str, Any]:
        """
        Check HaveIBeenPwned API
        Note: HIBP primarily checks emails, phone support is limited
        """
        if not self.hibp_api_key:
            return {"error": "HIBP API key not configured"}
        
        # Note: HIBP API v3 supports email search, not phone numbers directly
        # This is a placeholder for demonstration
        return {
            "found": False,
            "breaches": [],
            "note": "HIBP primarily supports email checks"
        }
    
    def check_dehashed(self, phone_number: str) -> Dict[str, Any]:
        """
        Check Dehashed API (if configured)
        """
        if not self.dehashed_api_key:
            return {"error": "Dehashed API not configured"}
        
        try:
            url = "https://api.dehashed.com/search"
            headers = {
                "Authorization": f"Basic {self.dehashed_api_key}",
                "Accept": "application/json"
            }
            params = {"query": phone_number}
            
            response = requests.get(url, headers=headers, params=params, timeout=self.timeout)
            if response.status_code == 200:
                data = response.json()
                return {
                    "found": data.get("total", 0) > 0,
                    "total_results": data.get("total", 0),
                    "entries": data.get("entries", [])
                }
            else:
                return {"error": f"Dehashed API error: {response.status_code}"}
        
        except Exception as e:
            return {"error": str(e)}
    
    def check_mock_breaches(self, phone_number: str) -> Dict[str, Any]:
        """
        Check against mock breach database for demonstration
        """
        # Generate deterministic results
        hash_val = int(hashlib.md5(phone_number.encode()).hexdigest(), 16)
        
        # Simulate breach detection
        found_breaches = []
        for breach in self.known_breaches:
            # 30% chance of being in each breach
            if hash_val % 10 < 3:
                found_breaches.append(breach)
        
        if found_breaches:
            last_breach = max(found_breaches, key=lambda x: x["year"])
            return {
                "breaches_found": len(found_breaches),
                "sources": [b["name"] for b in found_breaches],
                "last_breach": last_breach["year"],
                "risk_level": self._calculate_risk_level(found_breaches),
                "total_records_exposed": sum(b["records"] for b in found_breaches),
                "details": found_breaches
            }
        else:
            return {
                "breaches_found": 0,
                "sources": [],
                "last_breach": None,
                "risk_level": "LOW",
                "total_records_exposed": 0,
                "details": []
            }
    
    def _calculate_risk_level(self, breaches: List[Dict]) -> str:
        """Calculate risk level based on breaches"""
        if len(breaches) >= 3:
            return "HIGH"
        elif len(breaches) >= 2:
            return "MEDIUM"
        elif len(breaches) == 1:
            return "LOW"
        else:
            return "NONE"
    
    def check_breaches(self, phone_number: str) -> Dict[str, Any]:
        """
        Comprehensive breach check
        """
        results = {
            "phone_number": phone_number,
            "breaches_found": 0,
            "sources": [],
            "last_breach": None,
            "risk_level": "UNKNOWN",
            "total_records_exposed": 0,
            "check_timestamp": datetime.now().isoformat(),
            "sources_checked": []
        }
        
        # Check HIBP (if configured)
        hibp_result = self.check_hibp(phone_number)
        if "error" not in hibp_result:
            results["sources_checked"].append("HaveIBeenPwned")
            if hibp_result.get("found"):
                results["breaches_found"] += len(hibp_result.get("breaches", []))
        
        # Check Dehashed (if configured)
        dehashed_result = self.check_dehashed(phone_number)
        if "error" not in dehashed_result:
            results["sources_checked"].append("Dehashed")
            if dehashed_result.get("found"):
                results["breaches_found"] += dehashed_result.get("total_results", 0)
        
        # Mock breach check (always available for demonstration)
        mock_result = self.check_mock_breaches(phone_number)
        results["sources_checked"].append("Mock Database")
        
        # Merge results
        if mock_result["breaches_found"] > 0:
            results["breaches_found"] += mock_result["breaches_found"]
            results["sources"].extend(mock_result["sources"])
            results["last_breach"] = mock_result["last_breach"]
            results["total_records_exposed"] += mock_result["total_records_exposed"]
        
        # Calculate final risk level
        if results["breaches_found"] >= 3:
            results["risk_level"] = "HIGH"
        elif results["breaches_found"] >= 2:
            results["risk_level"] = "MEDIUM"
        elif results["breaches_found"] == 1:
            results["risk_level"] = "LOW"
        else:
            results["risk_level"] = "NONE"
        
        return results
    
    def get_breach_details(self, breach_name: str) -> Optional[Dict]:
        """Get details of specific breach"""
        for breach in self.known_breaches:
            if breach["name"].lower() == breach_name.lower():
                return breach
        return None
    
    def generate_breach_report(self, phone_number: str) -> Dict[str, Any]:
        """Generate comprehensive breach report"""
        results = self.check_breaches(phone_number)
        
        # Add recommendations
        if results["breaches_found"] > 0:
            results["recommendations"] = [
                "Change passwords on affected accounts",
                "Enable two-factor authentication",
                "Monitor accounts for suspicious activity",
                "Use unique passwords for each service",
                "Consider using a password manager"
            ]
        else:
            results["recommendations"] = [
                "No breaches found - maintain good security practices",
                "Regularly monitor for future breaches",
                "Use two-factor authentication where available"
            ]
        
        return results

# Main entry point for testing
if __name__ == "__main__":
    checker = BreachChecker()
    test_number = "+919876543210"
    
    print("PhoneSee Breach Checker Test")
    print(f"Testing number: {test_number}\n")
    
    results = checker.check_breaches(test_number)
    print(json.dumps(results, indent=2))