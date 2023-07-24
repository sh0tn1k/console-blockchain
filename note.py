import hashlib

class Note:
    Splitter = "_splitter_"

    def __init__(self, text):
        self.text = text
        self.hash = self.compute_hash(text)

    def compute_hash(self, text):
        sha = hashlib.sha256()
        text_bytes = text.encode('utf-8')
        sha.update(text_bytes)
        return sha.digest()
    
    def ProofOfWork(self):
        proof = 0
        prefix_zeros = "0"
        target_zeros = 2 # Отрегулируйте это значение, чтобы увеличить количество нулей в хэше

        while True:
            data = f"{self.text}{proof}"
            hash_bytes = self.compute_hash(data)
            hash = hash_bytes.hex()
            if hash.startswith(prefix_zeros * target_zeros):
                return proof, hash
            proof += 1


    @property
    def Text(self):
        return self.text

    @property
    def ClearText(self):
        return self.text[self.text.index(Note.Splitter) + len(Note.Splitter):]

    @property
    def PreviousHash(self):
        return self.text[:self.text.index(Note.Splitter)]

    @property
    def HashString(self):
        # Нам необходимо вычислять хэш при каждой проверке.
        # Так мы будем уверены, что он действителен
        proof, hash = self.ProofOfWork()
        return proof, hash

    @property
    def Hash(self):
        return self.hash


note_text = "PreviousHash_splitter_Note 1"
note = Note(note_text)
#print("Text:", note.HashString)
#print("ClearText:", note.ClearText)
#print("PreviousHash:", note.PreviousHash)
#print("HashString:", note.HashString)
#print("HashBytes:", note.Hash)