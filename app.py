from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page with a Hello, World! message."""
    return render_template('index.html')

if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=8080, debug=True)