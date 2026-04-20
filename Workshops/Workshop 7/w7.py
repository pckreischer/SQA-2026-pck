# Paul Kreischer - pck0010@auburn.edu
# SQA Workshop 7

from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets, linear_model
import pandas as pd
import numpy as np
import mnist
from sklearn.model_selection import KFold
from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.keras.utils import to_categorical
from tensorflow import keras
from myLogger import giveMeLoggingObject

# get the logger
logger = giveMeLoggingObject()

def readData():
    iris = datasets.load_iris()
    print(type(iris.data), type(iris.target))
    X = iris.data
    Y = iris.target
    df = pd.DataFrame(X, columns=iris.feature_names)
    print(df.head())

    # LOG 1 - logging the dataset info here to detect poisoning attacks
    # if someone tampered with the iris data file the shape or null count would look wrong
    logger.info(f"readData: loaded iris dataset, shape={df.shape}, nulls={df.isnull().sum().sum()}")

    return df

def makePrediction():
    iris = datasets.load_iris()
    knn = KNeighborsClassifier(n_neighbors=6)
    knn.fit(iris['data'], iris['target'])
    X = [
        [5.9, 1.0, 5.1, 1.8],
        [3.4, 2.0, 1.1, 4.8],
    ]

    # LOG 2 - log the inputs going into the knn model
    # this helps catch poisoning attacks where bad input samples are being passed in
    logger.info(f"makePrediction: input samples = {X}")

    prediction = knn.predict(X)
    print(prediction)

    # LOG 3 - log what the model predicted
    # if the model is being tricked the predictions will be wrong, we can see that here
    logger.info(f"makePrediction: knn predicted {prediction.tolist()}")

def doRegression():
    diabetes = datasets.load_diabetes()
    diabetes_X = diabetes.data[:, np.newaxis, 2]
    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]
    diabetes_y_train = diabetes.target[:-20]
    diabetes_y_test = diabetes.target[-20:]

    # LOG 4 - log dataset sizes before training
    # a poisoning attack might mess with the dataset so the training set ends up empty or wrong
    logger.info(f"doRegression: diabetes dataset - train size={len(diabetes_X_train)}, test size={len(diabetes_X_test)}")

    regr = linear_model.LinearRegression()
    regr.fit(diabetes_X_train, diabetes_y_train)
    diabetes_y_pred = regr.predict(diabetes_X_test)

    # LOG 5 - log the error of the regression model
    # if the model is being tricked, the MSE will be way higher than expected
    mse = np.mean((diabetes_y_pred - diabetes_y_test) ** 2)
    logger.info(f"doRegression: MSE={mse:.4f} - {'looks normal' if mse < 10000 else 'WARNING high error, possible model tricking'}")


def doDeepLearning():


    (train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data()

    # LOG 6 - log the mnist dataset shape right after loading it
    # if an attacker poisoned the dataset file we would see an unexpected shape or missing classes
    logger.info(f"doDeepLearning: MNIST loaded - train={train_images.shape}, test={test_images.shape}, unique labels={np.unique(train_labels).tolist()}")



    train_images = (train_images / 255) - 0.5
    test_images = (test_images / 255) - 0.5


    train_images = np.expand_dims(train_images, axis=3)
    test_images = np.expand_dims(test_images, axis=3)

    num_filters = 8
    filter_size = 3
    pool_size = 2

    model = Sequential([
    Conv2D(num_filters, filter_size, input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=pool_size),
    Flatten(),
    Dense(10, activation='softmax'),
    ])

    # Compile the model.
    model.compile(
    'adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'],
    )

    # Train the model.
    history = model.fit(
    train_images,
    to_categorical(train_labels),
    epochs=3,
    validation_data=(test_images, to_categorical(test_labels)),
    )

    # LOG 7 - log training and validation accuracy after training finishes
    # a model tricking attack would cause the val accuracy to drop or be suspiciously low
    train_acc = history.history['accuracy'][-1]
    val_acc = history.history['val_accuracy'][-1]
    logger.info(f"doDeepLearning: training done - train_acc={train_acc:.4f}, val_acc={val_acc:.4f} - {'OK' if val_acc > 0.8 else 'WARNING low accuracy'}")

    model.save_weights('cnn.weights.h5')

    predictions = model.predict(test_images[:5])

    print(np.argmax(predictions, axis=1)) # [7, 2, 1, 0, 4]

    print(test_labels[:5]) # [7, 2, 1, 0, 4]

    # LOG 8 - compare the models predictions vs the actual labels
    # if the model got tricked the predictions wont match and we can tell from the log
    pred_labels = np.argmax(predictions, axis=1).tolist()
    actual = test_labels[:5].tolist()
    logger.info(f"doDeepLearning: predicted={pred_labels}, actual={actual} - {'match' if pred_labels == actual else 'MISMATCH - possible model tricking'}")

def k_fold_cv_mlp(n_splits):

  iris_data = load_iris()
  X_data = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
  ## to numpy
  X=  X_data.to_numpy()
  y = iris_data.target

  # LOG 9 - log the dataset being used for cross validation
  # want to make sure the data wasn't poisoned before we start training all these folds
  logger.info(f"k_fold_cv_mlp: iris data loaded for CV, shape={X_data.shape}, nulls={X_data.isnull().sum().sum()}, n_splits={n_splits}")

  kf = KFold(n_splits)
  folds = []

  for train_index, test_index in kf.split(X):
      folds.append((train_index, test_index))


  # Initialize machine learning model, MLP
  model = MLPClassifier(hidden_layer_sizes=(256,128,64,32),activation="relu",random_state=1)

  # Initialize a list to store the evaluation scores
  scores = []
  ## Initialize fold index
  fold_index = 0


  # Iterate through each fold
  for train_indices, test_indices in folds:
      X_train, y_train = X[train_indices], y[train_indices]
      X_test, y_test = X[test_indices], y[test_indices]


      fold_index += 1
      print(f"Fold {fold_index}:")

      # scale data
      sc_X = StandardScaler()
      X_train_scaled=sc_X.fit_transform(X_train)
      X_test_scaled=sc_X.transform(X_test)

      # Train the model on the training data
      model.fit(X_train_scaled, y_train)

      # Make predictions on the test data
      y_pred = model.predict(X_test_scaled)

      # Calculate the accuracy score for this fold
      fold_score = accuracy_score(y_test, y_pred)
      print(f"Fold test score {fold_score}:")

      # Append the fold score to the list of scores
      scores.append(fold_score)

  # Calculate the mean accuracy across all folds
  mean_accuracy = np.mean(scores)
  print("K-Fold Cross-Validation Scores:", scores)
  print("Mean Accuracy:", mean_accuracy)

  # LOG 10 - log all the fold scores and mean accuracy for the mlp
  # if the accuracy is really low across all folds that could mean the model is being tricked
  logger.info(f"k_fold_cv_mlp: CV done - scores={[round(s,4) for s in scores]}, mean_accuracy={mean_accuracy:.4f} - {'OK' if mean_accuracy > 0.7 else 'WARNING low accuracy, possible model tricking'}")

if __name__=='__main__':
    data_frame = readData()
    makePrediction()
    doRegression()
    my_k_fold = input('Type in k for cross valdation: ')
    my_k_fold = int(my_k_fold)
    k_fold_cv_mlp(my_k_fold)
    doDeepLearning()
