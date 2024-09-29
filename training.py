import json
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam


with open('intents.json') as json_file:
    intents = json.load(json_file)


patterns = []
intent_labels = []
for intent in intents['intents']:
    for pattern in intent['patterns']:
        patterns.append(pattern)
        intent_labels.append(intent['tag'])


label_encoder = LabelEncoder()
intent_labels_encoded = label_encoder.fit_transform(intent_labels)


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(patterns)
X = X.toarray()
y = np.array(intent_labels_encoded)


X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)


inputs = Input(shape=(X_train.shape[1],))


x = Dense(128, activation='relu')(inputs)
x = Dropout(0.5)(x)
x = Dense(64, activation='relu')(x)
x = Dropout(0.5)(x)


outputs = Dense(len(np.unique(y_train)), activation='softmax')(x)


model = Model(inputs=inputs, outputs=outputs)


model.compile(optimizer=Adam(learning_rate=0.001),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


history = model.fit(X_train, y_train, epochs=200, batch_size=32, validation_data=(X_valid, y_valid))


loss, accuracy = model.evaluate(X_valid, y_valid)
print(f'Validation Loss: {loss:.4f}, Validation Accuracy: {accuracy:.4f}')


model.save('intent_classification_model_functional.h5')
np.save('label_encoder_functional.npy', label_encoder.classes_)
np.save('vectorizer_functional.npy', vectorizer.vocabulary_)
