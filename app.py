from flask import Flask, redirect, request, render_template_string
import logging
from datetime import datetime
import os

app = Flask(__name__)

# Configure logging
# Ensure the logs directory exists
log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file_path = os.path.join(log_dir, 'phishing_clicks.log')
logging.basicConfig(filename=log_file_path, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/phish_link')
def phish_link():
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    log_message = f"Click Detected: IP={ip_address}, User-Agent='{user_agent}', Time={timestamp}"
    logging.info(log_message)
    print(log_message) # Also print to console for immediate feedback

    # Redirect to the training page
    # You can change this URL to your actual training page or a more elaborate simulation feedback page.
    training_url = "https://data.actionfraud.police.uk/cms/wp-content/uploads/2020/09/Phishing-attacks-dealing-with-suspicious-emails.pdf" # Replace with your actual training URL
    # For now, let's use a simple placeholder page that tells them it was a test
    # We'll serve this directly from Flask for simplicity in this step.
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Phishing Simulation Complete</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f0f0f0; }
                .container { background-color: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: inline-block; }
                h1 { color: #d9534f; }
                p { color: #333; }
                .button { background-color: #5cb85c; color: white; padding: 10px 20px; border: none; border-radius: 5px; text-decoration: none; display: inline-block; margin-top: 20px; }
                .button:hover { background-color: #4cae4c; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Phishing Simulation Result</h1>
                <p>Congratulations! You just clicked a simulated phishing link.</p>
                <p>This was a test designed to help you identify real phishing attempts.</p>
                <p>Your click has been logged for educational purposes only.</p>
                <p>It's crucial to always be vigilant about suspicious emails.</p>
                <a href="https://www.example.com/phishing-education" target="_blank" class="button">Learn More About Phishing Prevention</a>
                <p style="font-size: 0.8em; color: #777;">(Note: The 'Learn More' link is a placeholder. You'll replace it with your actual training material.)</p>
            </div>
        </body>
        </html>
    """)


if __name__ == '__main__':
    # IMPORTANT: For production, you would use a more robust web server like Gunicorn or uWSGI
    # and ensure it's accessible externally. For this self-learning project,
    # running directly from Flask's dev server on localhost is fine.
    # We will later discuss how to make it accessible to your employees.
    app.run(debug=True, host='0.0.0.0', port=5000)