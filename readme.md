# Bank Branches API

This project is a Django-based GraphQL API that allows users to query bank branch data and associated bank information. The API supports GraphQL queries for retrieving branches and their corresponding bank details.

## Features
- Fetch branches with their details (IFSC, branch name, address, etc.)
- Fetch the associated bank's name for each branch
- GraphQL API available at `/gql` endpoint
- Comprehensive test cases to ensure code quality

## Prerequisites
To install and run this project locally, you'll need:

- Python 3.8+
- pip (Python package installer)
- Git

## Installation

Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/bank-branches-api.git
cd bank-branches-api

pip install -r requirements.txt

Then run the project by the following command:
python manage.py runserver
