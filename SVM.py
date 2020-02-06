import numpy as np
from sklearn.svm import SVC, LinearSVC, NuSVC
from mushrooms.mushroom_dataset import import_mushrooms_numpy
from titanic.titanic_dataset import import_cleaned_titanic_data
from sklearn.model_selection import ShuffleSplit
from sklearn import preprocessing

from metrics import plot_compare_learning_curve, plot_compare_roc_curve, plot_compare_precision_recall_curve

if __name__ == "__main__":
    cv = ShuffleSplit(n_splits=5, test_size=0.6, random_state=0)

    # clf = SVC(kernel='linear')
    # models = {'linear': clf}
    # x_m, y_m = import_mushrooms_numpy(filepath="mushrooms/mushrooms.csv")
    # plot_compare_precision_recall_curve(models, x_m, y_m)

    models_kernels = {
        'linear' : SVC(kernel='linear'),
        'rbf'    : SVC(kernel='rbf'),
        'poly'   : SVC(kernel='poly'),
        'sigmoid': SVC(kernel='sigmoid')
    }

    models_classes = {
        'SVC'         : SVC(kernel='linear'),
        'LinearSVC'   : LinearSVC(),
        'NuSVC'       : NuSVC(kernel='linear'),
        'NuSVC (poly)': NuSVC(kernel='poly')
    }

    x, y, x_test, test_ids = import_cleaned_titanic_data(directorypath="titanic/")
    x_scaled = preprocessing.scale(x)

    plot_compare_precision_recall_curve(models_kernels, x_scaled, y)
    plot_compare_roc_curve(models_kernels, x_scaled, y)
    plot_compare_learning_curve(models_kernels, x_scaled, y,
                                cv=ShuffleSplit(test_size=0.3),
                                train_sizes=np.linspace(0.2, 1.0, 5))

    plot_compare_precision_recall_curve(models_classes, x_scaled, y)
    plot_compare_roc_curve(models_classes, x_scaled, y)
    plot_compare_learning_curve(models_classes, x_scaled, y,
                                cv=ShuffleSplit(test_size=0.3),
                                train_sizes=np.linspace(0.2, 1.0, 5))

    print("Booty")
