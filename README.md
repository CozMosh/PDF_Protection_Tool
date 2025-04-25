# PDF_Protection Tool 

## 🎯 Objective

The PDF Protection Tool is designed to add password protection to PDF files. This tool allows users to secure their PDF documents by encrypting them with a password. It uses the pikepdf library to open, encrypt, and save a PDF file with user-defined security settings. This tool is useful for ensuring the confidentiality and protection of sensitive documents by preventing unauthorized access.

### 🧠 Skills Learned

- Working with the pikepdf library for handling PDF files.
- Understanding PDF encryption mechanisms and how to apply them using Python
- Gaining experience in building command-line tools that accept user inputs.
- Handling errors and exceptions effectively in Python scripts.
-Basic usage of sys.argv for command-line arguments in Python.

### 🛠 Tools Used

- **pikepdf**: A library for reading and writing PDF files in Python, with support for encryption.
- **sys.argv**: Used to pass command-line arguments to the script.
- Custom subdomain wordlist **(subdomains.txt)** for testing.
- Python's exception handling: To catch and report errors during file processing.

## 🛠 Step-by-Step Code Breakdown

### **Step 1**: Import Necessary Libraries.
```python
import pikepdf
import sys
```

### **Step 2**:: Define the Function to Protect the PDF.
This function opens the input PDF, applies encryption using the provided password, and saves the output PDF with password protection.
```python
def protect_pdf(input_pdf, output_pdf, password):
    try:
        pdf = pikepdf.open(input_pdf)
        pdf.save(output_pdf, encryption=pikepdf.Encryption(owner=password, user=password, R=4))
        print(f"Password-protected PDF saved as {output_pdf}")
    except Exception as e:
        print(f"Error: {e}")
```

### **Step 3**:: Define the Main Function to Parse Command-Line Arguments.
This function checks if the correct number of arguments are provided. It then calls the protect_pdf function with the input PDF, output PDF, and password.
```python
def main():
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <input_pdf> <output_pdf> <password>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    password = sys.argv[3]

    protect_pdf(input_pdf, output_pdf, password)
```

### **Step 4**:: Run the Script.
If this script is executed directly (not imported as a module), the main() function will be called.
```python
if __name__ == "__main__":
    main()
```

## 🛠 File Structure
```
│
├── input.pdf            # Your source PDF file that you want to protect
├── output.pdf           # The output PDF file with password protection
└── pdf_protection.py    # The Python script that adds password protection to the PDF

```

## 📖 Overall Explanation 
```
- Objective: Describes the purpose of the tool, password-protecting PDF files.
- Skills Learned: Lists the key skills learned while working on this project, such as using pikepdf and handling command-line arguments.
- Tools Used: Details the libraries and tools used to implement the solution.
- Step-by-Step Code Breakdown: Provides a breakdown of each part of the code with explanations.
- File Structure: Shows the structure of files in the repository, including the source and output PDF files, as well as the Python script.

```
## ⚠️ Disclaimer

This tool is intended for personal and authorized use only.
Do not use it to tamper with PDF files that you do not own or have explicit permission to modify.
Unauthorized encryption of files may violate copyright or privacy laws.


## 👤 Author

Made with curiosity and caffeine ☕  
**Gumbo**  
[GitHub Profile](https://github.com/your-username)

