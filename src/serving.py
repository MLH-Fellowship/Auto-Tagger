from typing import List
import bentoml

import torch

from bentoml.frameworks.pytorch import PytorchModelArtifact
from bentoml.adapters import JsonInput, JsonOutput

import numpy as np

import joblib
import json

from config import config
from dataset import EntityDataset
import utils
from model import EntityModel




meta_data = joblib.load("meta.bin")
enc_pos = meta_data["enc_pos"]
enc_tag = meta_data["enc_tag"]

num_pos = len(list(enc_pos.classes_))
num_tag = len(list(enc_tag.classes_))


@bentoml.env(infer_pip_packages=True)
@bentoml.artifacts([PytorchModelArtifact('ner')])
class PyTorchModel(bentoml.BentoService):
    
    '''
    @bentoml.utils.cached_property  # reuse transformer
    def transform(self):
        return transforms.Compose([transforms.CenterCrop((29, 29)), transforms.ToTensor()])
    '''
    
    @bentoml.api(input=JsonInput(), output=JsonOutput(), batch=True)
    def predict(self, input_json) -> List[str]:

        sentence = input_json[0]['sentence']

        tokenized_sentence = config.TOKENIZER.encode(sentence)

        sentence = sentence.split()
        #print(sentence)
        #print(tokenized_sentence)

        test_dataset = EntityDataset(
            texts=[sentence], 
            pos=[[0] * len(sentence)], 
            tags=[[0] * len(sentence)]
        )

        device = torch.device("cpu")

        with torch.no_grad():
            data = test_dataset[0]
            for k, v in data.items():
                data[k] = v.to(device).unsqueeze(0)
            tag, pos, _ = self.artifacts.ner(**data)

            tags = enc_tag.inverse_transform(
                    tag.argmax(2).cpu().numpy().reshape(-1)
                )[:len(tokenized_sentence)]

            i= 0
            names = []
            while i < len(tags):
                item = tags[i]
                indices = []
                if (item == "B-per"):
                    while (item == "B-per"):
                        indices.append(i)
                        i += 1
                        item = tags[i]
                    tokenized_name = tokenized_sentence[indices[0]:indices[-1]+1]
                    name = config.TOKENIZER.decode(tokenized_name)
                    names.append(name)
                indices=[]
                i += 1

            resp = ','.join(names)

            return [resp]



if __name__ == "__main__":


    device = torch.device("cpu")
    model = EntityModel(num_tag=num_tag, num_pos=num_pos)
    model.load_state_dict(torch.load(config.MODEL_PATH, map_location='cpu'))
    model.to(device)

    # 2) `pack` it with required artifacts
    bento_svc = PyTorchModel()
    bento_svc.pack('ner', model)

    # 3) save your BentoSerivce
    saved_path = bento_svc.save()