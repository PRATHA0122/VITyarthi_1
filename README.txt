VIT Bank Management System (VITyarthi)

Overview
The VIT Bank Management System is a CLI (Command Line Interface) application developed in Python. It simulates core banking functionalities, allowing users to manage accounts, perform transactions, and track financial history securely.
The system uses a JSON database for data persistence, ensuring that account details and transaction logs are saved between sessions.

Features
* User Authentication: Secure login with ID and PIN.
* Masked Input: Passwords and PINs are masked with asterisks (*) during typing for security.
* Account Registration: Automated generation of unique 5-digit Account IDs.
* Banking Operations: Support for Deposits, Withdrawals, and Fund Transfers.
* Account Recovery: "Forgot PIN" functionality using security questions.
* Transaction History: Detailed logs of all account activities with timestamps.

System Requirements
* Operating System: Windows (Required due to the use of the msvcrt library).
* Language: Python 3.x.

Installation and Run Instructions
1. Download the Source Code Save the provided Python script as bank_system.py.
2. Run the Application Open your terminal or command prompt, navigate to the folder containing the file, and run:
3. python bank_system.py
4. Data Storage Upon the first execution, the program will automatically generate a bank_data.json file in the same directory. Do not delete this file, as it contains all user records.

Usage Guide
Main Menu
* Login: Access an existing account.
* Create Account: Register a new user. You will be asked to set a 4-digit PIN and choose a security question.
* Forgot PIN: Reset credentials by answering your security question.
User Dashboard (After Login)
* Deposit: Add funds to your account.
* Withdraw: Remove funds (checks for sufficient balance).
* Transfer: Send money to another User ID.
* History: View the last 7 transactions.

Project Structure
* bank_system.py: Main application source code.
* bank_data.json: Database file storing user profiles and logs.

Author Information
Developed By: Keshav Maheshwari 
Registration Number: 25BAI11223

