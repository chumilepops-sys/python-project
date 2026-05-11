# ============================================
# QUESTION 1
# Text Processing and Analysis Program
# ============================================

# Import required modules
import re
import zlib


# ============================================
# TEXT CLEANING FUNCTIONS
# ============================================

# Function to clean text
def clean_text(text):

    # Remove punctuation
    cleaned = re.sub(r'[^\w\s@.]', '', text)

    # Remove extra spaces
    cleaned = re.sub(r'\s+', ' ', cleaned)

    # Remove spaces at beginning and end
    cleaned = cleaned.strip()

    return cleaned


# Function to extract email addresses
def extract_emails(text):

    # Email pattern
    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

    # Find all emails
    emails = re.findall(email_pattern, text)

    return emails


# ============================================
# TEXT ANALYSIS FUNCTIONS
# ============================================

# Count total words
def count_words(text):

    words = text.split()

    return len(words)


# Count unique words
def count_unique_words(text):

    words = text.lower().split()

    unique_words = set(words)

    return len(unique_words)


# Count sentences
def count_sentences(text):

    sentences = re.split(r'[.!?]+', text)

    sentences = [s for s in sentences if s.strip()]

    return len(sentences)


# ============================================
# COMPRESSION FUNCTION
# ============================================

# Compress and save text
def compress_text(text):

    # Convert text into bytes
    text_bytes = text.encode('utf-8')

    # Compress text
    compressed_data = zlib.compress(text_bytes)

    # Save to binary file
    with open("compressed_text.bin", "wb") as file:
        file.write(compressed_data)

    print("\nCompressed file created successfully.")


# ============================================
# MAIN PROGRAM
# ============================================

def main():

    print("====================================")
    print("TEXT PROCESSING AND ANALYSIS PROGRAM")
    print("====================================")

    # User input
    user_text = input("\nEnter a block of text:\n\n")

    # Clean text
    cleaned_text = clean_text(user_text)

    # Analyse text
    total_words = count_words(cleaned_text)
    unique_words = count_unique_words(cleaned_text)
    sentence_count = count_sentences(user_text)
    emails = extract_emails(user_text)

    # Display results
    print("\n========== RESULTS ==========")

    print(f"\nCleaned Text:\n{cleaned_text}")

    print("\nText Statistics:")
    print(f"Total Words    : {total_words}")
    print(f"Unique Words   : {unique_words}")
    print(f"Sentence Count : {sentence_count}")

    # Display emails
    print("\nExtracted Emails:")

    if emails:
        for email in emails:
            print(f"- {email}")
    else:
        print("No email addresses found.")

    # Compress text
    compress_text(cleaned_text)


# Run the program
main()