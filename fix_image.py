import os

def fix_and_verify_file():
    target_file = "resilience_test.jpg"
    if not os.path.exists(target_file):
        target_file = "resilience_test.jpg.pdf"
        
    if os.path.exists(target_file):
        print(f"[*] File validated successfully: {target_file}")
        return target_file
    else:
        print("[ERROR] Target file missing from directory.")
        return None

if __name__ == "__main__":
    fix_and_verify_file()

