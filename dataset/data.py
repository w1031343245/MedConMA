import os
import jsonlines
import re

class MyDataset:
    def __init__(self):
        self.data = []
        self.text = []
        self.load()
        self.build_choice_ref_MedQA()

    def load(self):
        filename = "。/MedConMA/dataset/MedQA_USMLE/MedQA_USMLE.jsonl"
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File not found: {filename}")
        
        try:
            with open(filename, encoding = 'UTF-8') as f:
                for item in jsonlines.Reader(f):
                    self.data.append(item)
        except Exception as e:
            print(f"Error reading file {filename}: {e}")

    def get_by_idx(self, idx):
        return self.data[idx]
    
    def __len__(self):
        return len(self.data)
    
    def build_ref(self):
        self.ref = []
        for i in range(len(self)):
            item = self.get_by_idx(i)
            self.ref.append({'answers': {'text': item['answer']}, 'id': i})

    def build_choice_ref_MedQA(self):
        self.choice_ref = []
        for i in range(len(self)):
            item = self.get_by_idx(i)
            self.choice_ref.append({
                'answers': {'text': item['answer'], 'choice': item['answer_idx']},
                'options': item['options'],
                'type': item['meta_info'],
                'id': i
            })