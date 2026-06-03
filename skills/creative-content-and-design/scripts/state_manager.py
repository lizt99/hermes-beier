import json
import os
import argparse
from datetime import datetime

def update_json(path, delta):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Simple recursive merge
    def merge(target, source):
        for k, v in source.items():
            if k in target and isinstance(target[k], dict) and isinstance(v, dict):
                merge(target[k], v)
            elif k in target and isinstance(target[k], list) and isinstance(v, list):
                target[k].extend(v)
            else:
                target[k] = v
    
    merge(data, delta)
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('book_path', help="Path to book directory")
    parser.add_argument('file_name', help="e.g. character_matrix.json")
    parser.add_argument('delta_json', help="JSON string for the update")
    args = parser.parse_args()
    
    full_path = os.path.join(args.book_path, 'story', 'state', args.file_name)
    delta = json.loads(args.delta_json)
    
    if not os.path.exists(full_path):
        print(f"Error: {full_path} not found")
        return
        
    update_json(full_path, delta)
    print(f"Successfully updated {args.file_name}")

if __name__ == "__main__":
    main()
