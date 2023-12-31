import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

test.print(1, 'test.test')

# Carregando o conjunto de dados
data = pd.read_csv('seu_conjunto_de_dados.csv')  # Certifique-se de substituir 'seu_conjunto_de_dados.csv' pelo nome do seu arquivo

# Dividindo em dados de treinamento e teste
X = data['texto']  # Coluna que contém o texto
y = data['sentimento']  # Coluna que contém os rótulos dos sentimentos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pré-processamento e extração de recursos
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Treinando o modelo
model = MultinomialNB()
model.fit(X_train, y_train)

# Realizando previsões
y_pred = model.predict(X_test)

# Avaliando o modelo
accuracy = metrics.accuracy_score(y_test, y_pred)
print('Acurácia:', accuracy)

class T:
    def __init__(self):
        self.a = 1

    def p(self):
        return self.a * 10

while True:
    t = T()

    for i in range(len(2)):
        print(t.p())

    break
