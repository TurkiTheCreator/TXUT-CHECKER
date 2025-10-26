
# TXUT-CHECKER

A Python tool that extracts Instagram profile data including emails, phone numbers, follower counts, and verification status. Features bilingual support (English/French), batch scanning, JSON export, scans public profiles only, with rate limiting protection and comprehensive error handling. Perfect for social media research and profile analysis.

## Key Features & Benefits

*   **Profile Data Extraction:** Extracts essential data points such as emails, phone numbers, follower counts, and verification status.
*   **Bilingual Support:** Offers both English and French language options.
*   **Batch Scanning:** Enables processing of multiple Instagram profiles simultaneously.
*   **JSON Export:** Exports extracted data in a structured JSON format for easy integration and analysis.
*   **Public Profile Scanning:** Focuses solely on scanning publicly available profile information.
*   **Rate Limiting Protection:** Implements mechanisms to avoid rate limiting and ensure continuous operation.
*   **Comprehensive Error Handling:** Provides robust error handling for reliable and stable performance.
*   **Social Media Research:** Ideal for social media researchers and analysts seeking profile insights.
*   **Profile Analysis:** Supports in-depth profile analysis with key metrics.

## Prerequisites & Dependencies

Before you begin, ensure you have the following installed:

*   **Python:** Version 3.6 or higher.
*   **pip:** Python package installer.

Dependencies are listed in the `requirements.txt` file.

## Installation & Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/TurkiTheCreator/TXUT-CHECKER.git
    cd TXUT-CHECKER
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage Examples

To run the `txut_checker.py` script:

```bash
python txut_checker.py
```

The script will then guide you through the process of entering Instagram usernames and other configurations.

**Example Output (JSON):**

```json
[
    {
        "username": "instagram",
        "followers": 650000000,
        "is_verified": true,
        "email": null,
        "phone_number": null
    },
    {
        "username": "nationalgeographic",
        "followers": 300000000,
        "is_verified": true,
        "email": null,
        "phone_number": null
    }
]
```

## Configuration Options

There are no specific configuration files. However, the `txut_checker.py` script might contain configurable variables related to:

*   **Language:** Select between English and French for user interface.
*   **Output File:** Define the name of the JSON output file.
*   **Batch Size:** Specify the number of profiles to process in a single batch.
*   **Delay:** Adjust the delay between requests to avoid rate limiting. (Consult the script itself to see if/how these are implemented and changeable by the user.)

## Contributing Guidelines

We welcome contributions to the TXUT-CHECKER project! To contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with clear, concise messages.
4.  Submit a pull request to the main branch.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.

## License Information

License not specified. All rights reserved to the owner TurkiTheCreator.

## Acknowledgments

This project utilizes the `requests` and `urllib3` libraries.
