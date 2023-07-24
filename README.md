<h1>Blockchain-Based Note Management System</h1>
<p>This program is a simple <b>blockchain-based</b> note management system implemented in <code>Python</code>. It allows users to create, view, and validate notes using <b>blockchain technology</b> to ensure data integrity. The program makes use of <b>proof-of-work</b> to secure the blockchain.</p>

<h3>:clipboard: Features</h3>

* **Note Class:** Defines the structure of a note, with properties for text, hash, and various methods to manipulate and validate the note.

* **Proof-of-Work:** Implements a <i>proof-of-work algorithm</i> to find a <b>nonce (proof)</b> that, when combined with the note's text, produces a hash with a specified number of leading zeros. This is used to secure the blockchain and prevent tampering.

* **Command Enum:** Defines an enumeration for different commands that the user can choose, including viewing notes, adding a new note, validating the blockchain, and exiting the program.

* **Note Management Functions:** Functions to display all notes, view notes in detail, add new notes, and validate the integrity of the blockchain.

* **File I/O:** Notes are saved and loaded from a JSON file <code>blockchain.json</code> to maintain persistence across program runs.

<h3>:pencil2: How to Use</h3>

1. Run the program, and it will load existing notes from <code>blockchain.json</code> or create a new starting note if the file is empty or not found.

2. The user can choose from different commands by entering the corresponding number:
   - 1: View all note texts
   - 2: View all notes (including hash and detailed information)
   - 3: Add a new note
   - 4: Validate the integrity of the blockchain
   - 5: Exit the program

3. When adding a new note, the program will compute the <b>proof-of-work</b> and update the blockchain with the new note.

4. The blockchain is saved to <code>blockchain.json</code> after each operation.

<h2>Note</h2>

Please ensure that you have the required dependencies

```python
enum
hashlib
json
```

before running the program.
