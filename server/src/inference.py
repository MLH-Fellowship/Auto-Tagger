import numpy as np

import joblib
import torch

from config import config
from dataset import EntityDataset
import utils
from model import EntityModel


def predict(sentence):
  tokenized_sentence = config.TOKENIZER.encode(sentence)

  sentence = sentence.split()
  #print(sentence)
  #print(tokenized_sentence)

  test_dataset = EntityDataset(
      texts=[sentence], 
      pos=[[0] * len(sentence)], 
      tags=[[0] * len(sentence)]
  )

  device = torch.device("cuda")
  model = EntityModel(num_tag=num_tag, num_pos=num_pos)
  model.load_state_dict(torch.load(config.MODEL_PATH))
  model.to(device)

  with torch.no_grad():
      data = test_dataset[0]
      for k, v in data.items():
          data[k] = v.to(device).unsqueeze(0)
      tag, pos, _ = model(**data)

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


      return names

if __name__ == "__main__":

    meta_data = joblib.load("meta.bin")
    enc_pos = meta_data["enc_pos"]
    enc_tag = meta_data["enc_tag"]

    num_pos = len(list(enc_pos.classes_))
    num_tag = len(list(enc_tag.classes_))

    sentence = 'Hello it\'s Mehdi and Parth'

    names = predict(sentence)
    print(names)