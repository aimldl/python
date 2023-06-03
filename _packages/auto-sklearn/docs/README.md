[auto-sklearn > APIs](https://automl.github.io/auto-sklearn/master/api.html)

```bash
autosklearn.classification.AutoSklearnClassifier(time_left_for_this_task=3600, per_run_time_limit=360, initial_configurations_via_metalearning=25, ensemble_size: int = 50, ensemble_nbest=50, max_models_on_disc=50, ensemble_memory_limit=1024, seed=1, ml_memory_limit=3072, include_estimators=None, exclude_estimators=None, include_preprocessors=None, exclude_preprocessors=None, resampling_strategy='holdout', resampling_strategy_arguments=None, tmp_folder=None, output_folder=None, delete_tmp_folder_after_terminate=True, delete_output_folder_after_terminate=True, shared_mode=False, n_jobs: Optional[int] = None, disable_evaluator_output=False, get_smac_object_callback=None, smac_scenario_args=None, logging_config=None, metadata_directory=None)[source]¶
```



```bash
get_models_with_weights(self)
Return a list of the final ensemble found by auto-sklearn.

Returns
[(weight_1, model_1), …, (weight_n, model_n)]
```



```bash
get_params(self, deep=True)
Get parameters for this estimator.

Parameters
deepbool, default=True
If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns
paramsmapping of string to any
Parameter names mapped to their values.
```



Classification metrics

The default `autosklearn.metrics.f1`, `autosklearn.metrics.precision` and `autosklearn.metrics.recall` built-in metrics are applicable only for binary classification. In order to apply them on multilabel and multiclass classification, please use the corresponding metrics with an appropriate averaging mechanism, such as `autosklearn.metrics.f1_macro`. For more information about how these metrics are used, please read [this scikit-learn documentation](http://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-and-f-measures).



```bash
autosklearn.metrics.accuracy
autosklearn.metrics.balanced_accuracy
autosklearn.metrics.f1
autosklearn.metrics.f1_macro
autosklearn.metrics.f1_micro
autosklearn.metrics.f1_samples
autosklearn.metrics.f1_weighted
autosklearn.metrics.roc_auc
autosklearn.metrics.precision
autosklearn.metrics.precision_macro
autosklearn.metrics.precision_micro
autosklearn.metrics.precision_samples
autosklearn.metrics.precision_weighted
autosklearn.metrics.average_precision
autosklearn.metrics.recall
autosklearn.metrics.recall_macro
autosklearn.metrics.recall_micro
autosklearn.metrics.recall_samples
autosklearn.metrics.recall_weighted
autosklearn.metrics.log_loss
Regression metrics
autosklearn.metrics.r2
autosklearn.metrics.mean_squared_error
autosklearn.metrics.mean_absolute_error
autosklearn.metrics.median_absolute_error
```

