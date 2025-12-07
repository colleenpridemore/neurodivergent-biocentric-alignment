#!/usr/bin/env python3
"""Extract license information from the BGINEXUS.io PDF"""

from pypdf import PdfReader
import re

def extract_commons_sections(pdf_path):
    reader = PdfReader(pdf_path)
    full_text = ""
    
    # Extract all pages
    for page in reader.pages:
        full_text += page.extract_text() + "\n"
    
    # Save full text
    with open('BGINEXUS_full_text.txt', 'w') as f:
        f.write(full_text)
    
    print(f"Extracted {len(reader.pages)} pages")
    print(f"Total characters: {len(full_text)}")
    
    # Find sections for each Commons
    commons_list = [
        "Value Commons",
        "Transparency Commons", 
        "Sustainability Commons",
        "Access Commons",
        "Reciprocity Commons",
        "Governance Commons"
    ]
    
    for commons in commons_list:
        print(f"\n{'='*60}")
        print(f"Searching for: {commons}")
        print('='*60)
        
        # Case-insensitive search
        pattern = re.compile(f"3\\.\\d+\\.\\s*{re.escape(commons)}", re.IGNORECASE)
        match = pattern.search(full_text)
        
        if match:
            start_pos = match.start()
            # Get ~2000 characters after the match to see the section
            snippet = full_text[start_pos:start_pos+2000]
            print(snippet[:1500])
        else:
            print(f"Section not found for {commons}")

if __name__ == "__main__":
    extract_commons_sections("5835702.pdf")
