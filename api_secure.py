from flask import Flask, send_file, request
import os
import time

app = Flask(__name__)

# Dictionary to store download counts per IP address
download_counts = {"127.0.0.1": 3}

# Function to limit downloads per IP address
def limit_downloads(ip):
    # Check if IP address exists in dictionary
    if ip in download_counts:
        # Check if IP address has reached the down
        if download_counts[ip] >= 3:
            return False
        else:
            # Increment download count
            download_counts[ip] += 1
            return True
    else:
        # If IP address is not in dictionary, add it with download count 1
        download_counts[ip] = 1
        return True

@app.route('/download')
def download_file():
    # Get client's IP address
    ip_address = request.remote_addr
    
    # Check if client has exceeded download limit
    if not limit_downloads(ip_address):
        return "Download limit exceeded for this IP address.", 403
    
    # Get the absolute path to the Downloads folder inside the user's home directory
    downloads_folder = os.path.expanduser('/Users/admin/Downloads/')
    # Join the absolute path with the filename
    file_path = os.path.join(downloads_folder, 'cv.exe')
    
    # Check if the file exists
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return "File not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
