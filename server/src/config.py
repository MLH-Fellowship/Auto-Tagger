import transformers

class config:
    MAX_LEN = 128
    TRAIN_BATCH_SIZE = 32
    VALID_BATCH_SIZE = 8
    EPOCHS = 5
    BASE_MODEL_PATH = "./"
    MODEL_PATH = "model.bin"
    TRAINING_FILE = "ner_dataset.csv"
    TOKENIZER = transformers.BertTokenizer.from_pretrained(
        BASE_MODEL_PATH,
        do_lower_case=True
    )
