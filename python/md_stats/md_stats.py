import os
import glob
import datetime
import csv
import json

def load_config(path):

    with open(path + 'config.json', 'r') as f:
        return json.load(f)

def count_chars_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return len(f.read())

def log_md_files_in_dir(config):
    dirpath = config['directory_path']
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    total_char_count = 0
    md_file_count = 0
    log_file_path = "log.csv"
    
    # Check if file exists
    write_header = not os.path.isfile(log_file_path)
    
    with open(log_file_path, 'a', newline='', encoding='utf-8') as log_file:
        writer = csv.writer(log_file)
        
        # Write headers if file didn't exist
        if write_header:
            writer.writerow(["Timestamp", "Total .md files", "Total characters in .md files"])
        
        for filepath in glob.iglob(dirpath + '**/*.md', recursive=True):
            char_count = count_chars_in_file(filepath)
            total_char_count += char_count
            md_file_count += 1

        # Write row with current data
        writer.writerow([timestamp, md_file_count, total_char_count])

    print(f"Log updated at {log_file_path}")

# Test it out
print(os.getcwd())
config = load_config("python/md_stats/")
log_md_files_in_dir(config)