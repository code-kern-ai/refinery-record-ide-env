import sys
import pickle

if __name__ == "__main__":

    _, code, record_bytes_path, knowledge_base_path = sys.argv
    with open(record_bytes_path, "rb") as file:
        record = pickle.load(file)

    with open(knowledge_base_path, "rb") as file:
        knowledge_base_source_code = pickle.load(file)
        with open("knowledge.py", "w") as file:
            file.write(knowledge_base_source_code)

    exec(code)
