import re
import pickle

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

from configuration import (
    MODEL_PATH,
    TOKENIZER_PATH,
    MAX_LENGTH
)



model = load_model(MODEL_PATH)



with open(TOKENIZER_PATH, "rb") as f:
    tokenizer = pickle.load(f)



def clean_text(text):

    text = text.lower()

    text = re.sub(r"<.*?>", "", text)

    text = re.sub(r"http\S+|www\S+", "", text)

    text = re.sub(r"[^a-z\s]", "", text)

    text = re.sub(r"\s+", " ", text).strip()

    return text



def predict_sentiment(review):

    review = clean_text(review)

    sequence = tokenizer.texts_to_sequences(
        [review]
    )

    padded = pad_sequences(
        sequence,
        maxlen=MAX_LENGTH,
        padding="post"
    )

    prediction = model.predict(
        padded
    )[0][0]

    if prediction >= 0.5:

        sentiment = "POSITIVE"

        confidence = prediction

    else:

        sentiment = "NEGATIVE"

        confidence = 1 - prediction

    print("\nPrediction")
    print("=" * 30)

    print(
        f"Sentiment : {sentiment}"
    )

    print(
        f"Confidence : {confidence*100:.2f}%"
    )



review = input(
    "Enter Review:\n"
)

predict_sentiment(review)