#라이브러리 import
import os
from gzip import GzipFile

import numpy as np
import pylab as pl

from scikits.learn.grid_search import GridSearchCV
from scikits.learn.metrics import classification_report
from scikits.learn.metrics import confusion_matrix
from scikits.learn.pca import RandomizedPCA
from scikits.learn.svm import SVC

#dataset 다운로드
url = "https://downloads.sourceforge.net/project/scikit-learn/data/lfw_preprocessed.tar.gz"
archive_name = "lfw_preprocessed.tar.gz"
folder_name = "lfw_preprocessed"

if not os.path.exists(folder_name):
    if not os.path.exists(archive_name):
        import urllib
        print("Downloading data, please Wait (58.8MB)...")
        print(url)
        opener = urllib.urlopen(url)
        open(archive_name, 'wb').write(opener.read())
        print()

    import tarfile
    print("Decompressiong the archive: " + archive_name)
    tarfile.open(archive_name, "r:gz").extractall()
    print()

# dataset 로드
faces_filename = os.path.join(folder_name, "faces.npy.gz")
filenames_filename = os.path.join(folder_name, "face_filenames.txt")

faces = np.load(GzipFile(faces_filename))
face_filenames = [l.strip() for l in file(filenames_filename).readlines()]

#밝기를 기준으로 각 data 일반화(nomalization)
faces -= faces.mean(axis=1)[:, np.newaxis]

categories = np.array([f.rsplit('_', 1)[0] for f in face_filenames])

#각 카테고리별 unique integer
category_names = np.unique(categories)

#integer label에 해당하는 카테로리로 전환
target = np.searchsorted(category_names, categories)

#상위 5개 모델 추출
selected_target = np.argsort(np.bincount(target))[-5:]

mask = np.array([item in selected_target for item in target])

X = faces[mask]
y = target[mask]

n_samples, n_features = X.shape

#dataset 사이즈
print("Dataset size:")
print("n_samples: %d" % n_samples)
print("n_features: %d" % n_features)

split = n_samples * 3 / 4

X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

#pca
n_components = 150

print("Extracting the top %d eigenfaces" % n_components)
pca = RandomizedPCA(n_components=n_components, whiten=True).fit(X_train)

eigenfaces = pca.components_.T.reshape((n_components, 64, 64))
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)


#training set에 적용
print("Fitting the classifier to the training set")
param_grid = {
 'C': [1, 5, 10, 50, 100],
 'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1],
}
clf = GridSearchCV(SVC(kernel='rbf'), param_grid,
                   fit_params={'class_weight': 'auto'})
clf = clf.fit(X_train_pca, y_train)
print("Best estimator found by grid search:")
print(clf.best_estimator)

#test set에 대한 모델 품질 테스트
y_pred = clf.predict(X_test_pca)
print(classification_report(y_test, y_pred, labels=selected_target,
                            class_names=category_names[selected_target]))

print(confusion_matrix(y_test, y_pred, labels=selected_target))


n_row = 3
n_col = 4

#evaluation of the predictions
pl.figure(figsize=(2 * n_col, 2.3 * n_row))
pl.subplots_adjust(bottom=0, left=.01, right=.99, top=.95, hspace=.15)
for i in range(n_row * n_col):
    pl.subplot(n_row, n_col, i + 1)
    pl.imshow(X_test[i].reshape((64, 64)), cmap=pl.cm.gray)
    pl.title('pred: %s\ntrue: %s' % (category_names[y_pred[i]],
                                     category_names[y_test[i]]), size=12)
    pl.xticks(())
    pl.yticks(())

pl.show()