import os
from google import genai
from google.genai import types

def run_access_and_analysis():
    client = genai.Client(api_key="AIzaSyBXbiRxlDBtLDxCghIz18wkEHu0zNcthhQ")
    
    pdf_path = "resilience_test.jpg"
    if not os.path.exists(pdf_path):
        pdf_path = "resilience_test.jpg.pdf"

    try:
        with open(pdf_path, "rb") as f:
            raw_bytes = f.read()
            
        pdf_part = types.Part.from_bytes(
            data=raw_bytes,
            mime_type="application/pdf"
        )
        
        prompt = (
            "Analyze this crisis support document. Provide a structured review explaining how "
            "the system delivers an AI safety-first dashboard, verifies real-time critical data engineering, "
            "and supports decision-making during emergencies."
        )
        
        print("[*] Contacting Gemini API for Vision Verification...")
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[pdf_part, prompt]
        )
        
        print("\n=== ACCESS CHECK & ANALYSIS SUCCESS ===")
        print(response.text)
        print("=======================================\n")
        
    except Exception as e:
        print(f"[ACCESS ERROR] API Authentication or payload failed: {e}")

if __name__ == "__main__":
    run_access_and_analysis()

