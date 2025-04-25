#PDF_Protection.py

# Import necessary libraries
import pikepdf  # pikepdf is used to work with PDF files and apply encryption
import sys      # sys.argv is used to capture command-line arguments

# Function to protect the PDF with a password
def protect_pdf(input_pdf, output_pdf, password):
    try:
        # Open the input PDF file using pikepdf
        pdf = pikepdf.open(input_pdf)
        
        # Save the output PDF with encryption (password protection)
        # We set the owner and user password to the same value here
        # R=4 is the encryption standard (AES-256)
        pdf.save(output_pdf, encryption=pikepdf.Encryption(owner=password, user=password, R=4))
        
        # Print a success message once the PDF is encrypted and saved
        print(f"Password-protected PDF saved as {output_pdf}")
    
    except Exception as e:
        # Handle any exceptions (errors like file not found or invalid password)
        print(f"Error: {e}")

# Main function to handle the command-line arguments
def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        # Display usage instructions if arguments are incorrect
        print("Usage: python3 script.py <input_pdf> <output_pdf> <password>")
        sys.exit(1)  # Exit the program if the arguments are not correct
    
    # Assign the arguments to variables
    input_pdf = sys.argv[1]  # The input PDF file to be protected
    output_pdf = sys.argv[2]  # The output PDF file with encryption
    password = sys.argv[3]    # The password to be used for encryption
    
    # Call the function to protect the PDF
    protect_pdf(input_pdf, output_pdf, password)

# If this script is executed directly (not imported as a module), run the main function
if __name__ == "__main__":
    main()
# Import necessary libraries
import pikepdf  # pikepdf is used to work with PDF files and apply encryption
import sys      # sys.argv is used to capture command-line arguments

# Function to protect the PDF with a password
def protect_pdf(input_pdf, output_pdf, password):
    try:
        # Open the input PDF file using pikepdf
        pdf = pikepdf.open(input_pdf)
        
        # Save the output PDF with encryption (password protection)
        # We set the owner and user password to the same value here
        # R=4 is the encryption standard (AES-256)
        pdf.save(output_pdf, encryption=pikepdf.Encryption(owner=password, user=password, R=4))
        
        # Print a success message once the PDF is encrypted and saved
        print(f"Password-protected PDF saved as {output_pdf}")
    
    except Exception as e:
        # Handle any exceptions (errors like file not found or invalid password)
        print(f"Error: {e}")

# Main function to handle the command-line arguments
def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        # Display usage instructions if arguments are incorrect
        print("Usage: python3 script.py <input_pdf> <output_pdf> <password>")
        sys.exit(1)  # Exit the program if the arguments are not correct
    
    # Assign the arguments to variables
    input_pdf = sys.argv[1]  # The input PDF file to be protected
    output_pdf = sys.argv[2]  # The output PDF file with encryption
    password = sys.argv[3]    # The password to be used for encryption
    
    # Call the function to protect the PDF
    protect_pdf(input_pdf, output_pdf, password)

# If this script is executed directly (not imported as a module), run the main function
if __name__ == "__main__":
    main()
