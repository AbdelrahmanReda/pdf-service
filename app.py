from flask import Flask, request, render_template, send_file
from weasyprint import HTML

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/convert', methods=['POST'])
def convert_to_pdf():
    try:
        html_content = request.form.get('html_content')

        if not html_content:
            return 'HTML content is required', 400

        # Generate PDF from HTML content
        pdf_data = HTML(string=html_content).write_pdf()

        # Save the PDF to a file
        with open('output.pdf', 'wb') as f:
            f.write(pdf_data)

        return send_file('output.pdf', as_attachment=True)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500


if __name__ == '__main__':
    app.run(debug=True)
