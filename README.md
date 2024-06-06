# File Integrity Monitor (FIM)

This Python script is designed to monitor the integrity of files within a specified directory by calculating and comparing their SHA512 hash values. If any changes are detected, such as creation, modification, or deletion of files, the script will provide notifications accordingly.

## Usage

1. **Clone the Repository:**
   ```
   git clone https://github.com/Rishi-kaul/-File-Integrity-Monitor--FIM-.git
   ```

2. **Navigate to the Project Directory:**
   ```
   cd File-Integrity-Monitor--FIM-
   ```

3. **Run the Script:**
   - To collect a new baseline of file hashes:
     ```
     python main.py
     ```
     Select option 'A' when prompted.
   
   - To begin monitoring files with a saved baseline:
     ```
     python main.py
     ```
     Select option 'B' when prompted.

4. **Follow On-Screen Instructions:**
   - For option 'A', the script will generate a baseline file (`baseline.txt`) containing the hash values of files in the specified directory.
   - For option 'B', the script will continuously monitor the directory for any changes compared to the saved baseline.

## Requirements

- Python 3.x
- hashlib module (usually included in Python standard library)

## Flowchart

![Screenshot 2024-06-06 231356](https://github.com/Rishi-kaul/-File-Integrity-Monitor--FIM-/assets/134297029/084652c3-44e8-4961-80dd-62e468bc90ab)


## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
