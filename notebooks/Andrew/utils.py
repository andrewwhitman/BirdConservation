# imports
from sklearn.metrics import roc_curve, auc, recall_score, f1_score, plot_confusion_matrix
import matplotlib.pyplot as plt
from pandas import DataFrame

# functions
def evaluate(model, X_tr, y_tr, X_te, y_te, grid_search=False):
    """
    Fit a model to train data and calculate classification metrics for train and test data.
    Plot the confusion matrix and ROC curve for test data.
    
    Inputs:
        model: sklearn-like model object
            The model to be fit.
        X_tr: array-like
            The input samples for train set.
        y_tr: array-like
            The target values for train set.
        X_te: array-like
            The input samples for test set.
        y_te: array-like
            The target values for test set.
        grid_search: boolean, default=False
            False: The model is not a grid search object.
            True: The model is a grid search object. The best parameters and the CV results will be displayed.
        
    Outputs:
        None    
    """
    
    # fit the model
    model.fit(X_tr, y_tr)
    
    # predictions
    trn_preds = model.predict(X_tr)
    tst_preds = model.predict(X_te)
    tst_proba = model.predict_proba(X_te)[:,1]
    
    # roc auc calcs
    fpr, tpr, _ = roc_curve(y_te, tst_proba)
    auc_text = f"AUC Score: {auc(fpr, tpr):.3f}"
    
    
    print("Training Metrics")
    # Recall
    print(f"Recall: {recall_score(y_tr, trn_preds):.3f}")
    # f1
    print(f"f1: {f1_score(y_tr, trn_preds):.3f}")
    print('----')
    print("Testing Metrics")
    # Recall
    print(f"Recall: {recall_score(y_te, tst_preds):.3f}")
    # f1
    print(f"f1: {f1_score(y_te, tst_preds):.3f}")
    
    
    # create fig, axes
    fig, (ax1, ax2) = plt.subplots(2, figsize=(8, 12))
    
    # confusion matrix
    plot_confusion_matrix(model, X_te, y_te, cmap='Blues', ax=ax1)
    ax1.set_title('Confusion Matrix for Test Data')
    ax1.grid(False)
    
    # roc curve
    ax2.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve')
    ax2.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    ax2.set_title('Receiver operating characteristic (ROC) Curve for Test Data')
    ax2.set_xlabel('False Positive Rate')
    ax2.set_ylabel('True Positive Rate')
    ax2.set_xlim([0.0, 1.0])
    ax2.set_ylim([0.0, 1.05])
    ax2.text(x=0.72, y=0.15, s=auc_text, fontsize=14)
    ax2.legend(loc='lower right', fontsize=14)
    
    # display grid search results
    if grid_search:
        print(f"\nBest Parameters for Recall\n{model.best_params_}")
        display(DataFrame(model.cv_results_).sort_values('rank_test_recall'))