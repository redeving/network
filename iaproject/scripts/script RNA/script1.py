import pandas as pd
import tensorflow as tf





def getClassifier(featureColumns):
    classifier = tf.estimator.DNNClassifier(
        feature_columns = featureColumns,
        hidden_units = [10, 500, 10],
        n_classes = 10,
        optimizer=tf.train.GradientDescentOptimizer(
        learning_rate=0.1,)
    )
    return classifier

def getData():
    trainingData = pd.read_csv("training.csv", header=None).values
    testData = pd.read_csv("test.csv", header=None).values

    return trainingData, testData

def separateFeaturesAndCategories(trainingData, testData):
    trainingFeatures = formatFeatures(trainingData[:, :-1])
    trainingCategories = trainingData[:, -1:]
    testFeatures = formatFeatures(testData[:, :-1])
    testCategories = testData[:, -1:]

    return trainingFeatures, trainingCategories, testFeatures, testCategories

def formatFeatures(features):
    formattedFeatures = dict()
    numColumns = features.shape[1]

    for i in range(0, numColumns):
        formattedFeatures[str(i)] = features[:, i]

    return formattedFeatures

def getFeatures(features):
    featureColumns = []

    for key in features.keys():
        featureColumns.append(tf.feature_column.numeric_column(key=key))

    return featureColumns

def train(features, labels, batchSize):
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

    return dataset.shuffle(1000).repeat().batch(batchSize)

def test(features, labels, batchSize):
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels)).batch(batchSize)
    return dataset

def traning(classifier, trainingFeatures, trainingCategories):
    classifier.train(
        input_fn = lambda:train(trainingFeatures, trainingCategories, 100),
        steps = 50
    )

def testing(classifier, testFeatures, testCategories):
    accuracy = classifier.evaluate(
        input_fn = lambda:test(testFeatures, testCategories, 100)
    )
    return accuracy









def main():
    trainingData, testData = getData()
    trainingFeatures, trainingCategories, testFeatures, testCategories = \
        separateFeaturesAndCategories(trainingData, testData)

    featureColumns = getFeatures(trainingFeatures)
    classifier = getClassifier(featureColumns)
    traning(classifier, trainingFeatures, trainingCategories)
    accuracy = testing(classifier, testFeatures, testCategories)
    print('Test accuracy: {accuracy:0.3f}\n'.format(**accuracy))

if __name__ == "__main__":
    main()
