from flask import Flask, send_file

app = Flask(__name__)

@app.route('/downloads')
def download_file():
    return send_file('/Users/admin/Downloads/test.exe', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)