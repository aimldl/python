* Draft: 2020-05-12 (Thu)

# Validate the Installation of the H2O Python Module (full message)

* The full message to run `python -c "import h2o; h2o.init(); h2o.demo('glm')"` is below. 
* I recommend reading through it because it can serve as a tutorial that teaches "how to use H2O Python package".
* Several parts are edited for better readability without hurting the content.

```bash
$ python -c "import h2o; h2o.init(); h2o.demo('glm')"
Checking whether there is an H2O instance running at http://localhost:54321 ..... not found.
Attempting to start a local H2O server...
  Java Version: openjdk version "1.8.0_252"; OpenJDK Runtime Environment (build 1.8.0_252-8u252-b09-1~18.04-b09); OpenJDK 64-Bit Server VM (build 25.252-b09, mixed mode)
  Starting server from /home/aimldl/anaconda3/lib/python3.7/site-packages/h2o/backend/bin/h2o.jar
  Ice root: /tmp/tmpz6dnq2ox
  JVM stdout: /tmp/tmpz6dnq2ox/h2o_aimldl_started_from_python.out
  JVM stderr: /tmp/tmpz6dnq2ox/h2o_aimldl_started_from_python.err
  Server is running at http://127.0.0.1:54321
Connecting to H2O server at http://127.0.0.1:54321 ... successful.

--------------------------  --------------------------------------------------------------

H2O_cluster_uptime:         01 secs
H2O_cluster_timezone:       Asia/Seoul
H2O_data_parsing_timezone:  UTC
H2O_cluster_version:        3.30.0.3
H2O_cluster_version_age:    7 days, 16 hours and 10 minutes
H2O_cluster_name:           H2O_from_python_aimldl_poqr4h
H2O_cluster_total_nodes:    1
H2O_cluster_free_memory:    1.702 Gb
H2O_cluster_total_cores:    4
H2O_cluster_allowed_cores:  4
H2O_cluster_status:         accepting new members, healthy
H2O_connection_url:         http://127.0.0.1:54321
H2O_connection_proxy:       {"http": null, "https": null}
H2O_internal_security:      False
H2O_API_Extensions:         Amazon S3, XGBoost, Algos, AutoML, Core V3, TargetEncoder, Core V4
Python_version:             3.7.6 final

--------------------------  --------------------------------------------------------------

-------------------------------------------------------------------------------

Demo of H2O's Generalized Linear Estimator.

This demo uploads a dataset to h2o, parses it, and shows a description.
Then it divides the dataset into training and test sets, builds a GLM
from the training set, and makes predictions for the test set.

Finally, default performance metrics are displayed.
-------------------------------------------------------------------------------

>>> # Connect to H2O
>>>
>>> h2o.init()

(press any key)
```

##### When Enter key is pressed, 

```bash
Checking whether there is an H2O instance running at http://localhost:54321 . connected.
--------------------------  --------------------------------------------------------------
H2O_cluster_uptime:         4 mins 37 secs
H2O_cluster_timezone:       Asia/Seoul
H2O_data_parsing_timezone:  UTC
H2O_cluster_version:        3.30.0.3
H2O_cluster_version_age:    7 days, 16 hours and 15 minutes
H2O_cluster_name:           H2O_from_python_aimldl_poqr4h
H2O_cluster_total_nodes:    1
H2O_cluster_free_memory:    1.695 Gb
H2O_cluster_total_cores:    4
H2O_cluster_allowed_cores:  4
H2O_cluster_status:         locked, healthy
H2O_connection_url:         http://localhost:54321
H2O_connection_proxy:       {"http": null, "https": null}
H2O_internal_security:      False
H2O_API_Extensions:         Amazon S3, XGBoost, Algos, AutoML, Core V3, TargetEncoder, Core V4
Python_version:             3.7.6 final
--------------------------  --------------------------------------------------------------

>>> # Upload the prostate dataset that comes included in the h2o python package
>>> prostate = h2o.load_dataset("prostate")

(press any key)
```

##### When Enter key is pressed again and again, the following message appears one after another. The phrase `(press any key)` will be omitted from now on. 

```bash
Parse progress: |█████████████████████████████████████████████████████████████████████████████| 100%

>>> # Print a description of the prostate data
>>> prostate.describe()
Rows:380             
Cols:9
        ID	                …	GLEASON
-------	------------------	…	------------------
type	int	                …	int
mins	1	                …	0
mean	190.5	            …	6.38421052631579
maxs	380	                …	9
sigma	109.840793879141	…	1.09195337442611
zeros	0	                …	2
missing	0	                …	0
0	    1	                …	6
1	    2	                …	7
…       …                   …   …
9	    10	                …	6

>>> # Randomly split the dataset into ~70/30, training/test sets
>>> train, test = prostate.split_frame(ratios=[0.70])
>>> # Convert the response columns to factors (for binary classification problems)
>>> train["CAPSULE"] = train["CAPSULE"].asfactor()
>>> test["CAPSULE"] = test["CAPSULE"].asfactor()
                     
>>> # Build a (classification) GLM
>>> from h2o.estimators import H2OGeneralizedLinearEstimator
>>> prostate_glm = H2OGeneralizedLinearEstimator(family="binomial", alpha=[0.5])
>>> prostate_glm.train(x=["AGE", "RACE", "PSA", "VOL", "GLEASON"],
...                    y="CAPSULE", training_frame=train)

glm Model Build progress: |███████████████████████████████████████████████████████████████████| 100%

>>> # Show the model
>>> prostate_glm.show()
Model Details        
=============
H2OGeneralizedLinearEstimator :  Generalized Linear Modeling
Model Key:  GLM_model_python_1590036930977_1

GLM Model: summary
    family		link	regularization
--	--------	------	---------------------------------------------
    binomial	logit	Elastic Net (alpha = 0.5, lambda = 4.384E-4 )

number_of_predictors_total		number_of_active_predictors		number_of_iterations
----------------------------	-----------------------------	----------------------
5								5								4

training_frame
----------------
py_4_sid_9233

ModelMetricsBinomialGLM: glm
** Reported on train data. **

MSE: 0.1763855282661812
RMSE: 0.4199827713920908
LogLoss: 0.5217637822228672
Null degrees of freedom: 264
Residual degrees of freedom: 259
Null deviance: 357.4914067613288
Residual deviance: 276.53480457811963
AIC: 288.53480457811963
AUC: 0.7956938365077487
AUCPR: 0.7470605225765785
Gini: 0.5913876730154974

Confusion Matrix (Act/Pred) for max f1 @ threshold = 0.4123438381755666: 
       0    1    Error    Rate
-----  ---  ---  -------  ------------
0      120  38   0.2405   (38.0/158.0)
1      29   78   0.271    (29.0/107.0)
Total  149  116  0.2528   (67.0/265.0)

Maximum Metrics: Maximum metrics at their respective thresholds
metric                       threshold    value     idx
---------------------------  -----------  --------  -----
max f1                       0.412344     0.699552  114
max f2                       0.161038     0.799373  208
max f0point5                 0.412344     0.683012  114
max accuracy                 0.412344     0.74717   114
max precision                0.996787     1         0
max recall                   0.0991582    1         241
max specificity              0.996787     1         0
max absolute_mcc             0.412344     0.483095  114
max min_per_class_accuracy   0.412344     0.728972  114
max mean_per_class_accuracy  0.412344     0.744233  114
max tns                      0.996787     158       0
max fns                      0.996787     106       0
max fps                      0.000956782  158       263
max tps                      0.0991582    107       241
max tnr                      0.996787     1         0
max fnr                      0.996787     0.990654  0
max fpr                      0.000956782  1         263
max tpr                      0.0991582    1         241

Gains/Lift Table: Avg response rate: 40.38 %, avg score: 40.38 %
# The following table is reformatted.
   	group	cumulative_data_fraction	lower_threshold		...
--	-------	--------------------------	-----------------	...
   	1		0.0113208					0.982882			...
   	2		0.0226415					0.958494			...
   	3		0.0301887					0.933439			...
   	4		0.0415094					0.928812			...
   	5		0.0528302					0.916957			...
   	6		0.101887					0.792313			...
   	7		0.150943					0.673253			...
   	8		0.2							0.617031			...
   	9		0.301887					0.548867			...
   	10		0.4							0.452304			...
   	11		0.501887					0.34773				...
   	12		0.6							0.279644			...
   	13		0.698113					0.215147			...
   	14		0.8							0.159502			...
   	15		0.898113					0.109572			...
   	16		1							0.000956782			...


lift		cumulative_lift		response_rate	score		...
--------	-----------------	---------------	---------	...
2.47664		2.47664				1				0.991011	...
2.47664		2.47664				1				0.974133	...
2.47664		2.47664				1				0.943735	...
2.47664		2.47664				1				0.932017	...
2.47664		2.47664				1				0.921429	...
2.09561		2.29318				0.846154		0.864053	...
1.33357		1.98131				0.538462		0.725491	...
1.71459		1.91589				0.692308		0.646185	...
1.46764		1.7646				0.592593		0.582228	...
1.33357		1.65888				0.538462		0.502238	...
1.009		1.52695				0.407407		0.400109	...
0.857297	1.41745				0.346154		0.309667	...
0.571531	1.29856				0.230769		0.247785	...
0.458636	1.19159				0.185185		0.191605	...
0.285766	1.09263				0.115385		0.135741	...
0.183454	1					0.0740741		0.0672061	...

cumulative_response_rate	cumulative_score	capture_rate	...
--------------------------	------------------	--------------	...
1							0.991011			0.0280374		...
1							0.982572			0.0280374		...
1							0.972863			0.0186916		...
1							0.961723			0.0280374		...
1							0.953089			0.0280374		...
0.925926					0.91022				0.102804		...
0.8							0.850183			0.0654206		...
0.773585					0.800146			0.0841121		...
0.7125						0.726599			0.149533		...
0.669811					0.671567			0.130841		...
0.616541					0.616459			0.102804		...
0.572327					0.566292			0.0841121		...
0.524324					0.521528			0.0560748		...
0.481132					0.47951				0.046729		...
0.441176					0.441955			0.0280374		...
0.403774					0.403773			0.0186916		...

cumulative_capture_rate		gain		cumulative_gain
-------------------------	--------	-----------------
0.0280374					147.664		147.664
0.0560748					147.664		147.664
0.0747664					147.664		147.664
0.102804					147.664		147.664
0.130841					147.664		147.664
0.233645					109.561		129.318
0.299065					33.3573		98.1308
0.383178					71.4594		91.5888
0.53271						46.7636		76.4603
0.663551					33.3573		65.8879
0.766355					0.899965	52.6948
0.850467					-14.2703	41.7445
0.906542					-42.8469	29.856
0.953271					-54.1364	19.1589
0.981308					-71.4234	9.26333
1							-81.6546	0

Scoring History: 
    timestamp            duration    iterations    negative_log_likelihood    objective
--  -------------------  ----------  ------------  -------------------------  -----------
    2020-05-21 14:29:26  0.000 sec   0             178.746                    0.674512
    2020-05-21 14:29:26  0.018 sec   1             142.071                    0.536528
    2020-05-21 14:29:26  0.023 sec   2             138.434                    0.523033
    2020-05-21 14:29:26  0.026 sec   3             138.269                    0.522477
    2020-05-21 14:29:26  0.027 sec   4             138.267                    0.522475

>>> # Predict on the test set and show the first ten predictions
>>> predictions = prostate_glm.predict(test)
>>> predictions.show()

glm prediction progress: |████████████████████████████████████████████████████████████████████| 100%
  predict        p0        p1
---------  --------  --------
        1  0.464829  0.535171
        0  0.709247  0.290753
        1  0.216106  0.783894
        1  0.259277  0.740723
        1  0.234733  0.765267
        1  0.141134  0.858866
        0  0.598997  0.401003
        0  0.866855  0.133145
        1  0.349384  0.650616
        0  0.720801  0.279199

[115 rows x 3 columns]

>>> # Show default performance metrics
>>> performance = prostate_glm.model_performance(test)
>>> performance.show()

ModelMetricsBinomialGLM: glm
** Reported on test data. **

MSE: 0.18204686229910017
RMSE: 0.4266695000806833
LogLoss: 0.5450204486101323
Null degrees of freedom: 114
Residual degrees of freedom: 109
Null deviance: 154.79949264861418
Residual deviance: 125.35470318033046
AIC: 137.35470318033046
AUC: 0.7898550724637681
AUCPR: 0.7152915858287275
Gini: 0.5797101449275361

Confusion Matrix (Act/Pred) for max f1 @ threshold = 0.32598263261044014: 
       0    1    Error    Rate
-----  ---  ---  -------  ------------
0      44   25   0.3623   (25.0/69.0)
1      7    39   0.1522   (7.0/46.0)
Total  51   64   0.2783   (32.0/115.0)

Maximum Metrics: Maximum metrics at their respective thresholds
metric                       threshold    value     idx
---------------------------  -----------  --------  -----
max f1                       0.325983     0.709091  63
max f2                       0.227658     0.793358  86
max f0point5                 0.587471     0.702247  32
max accuracy                 0.587471     0.747826  32
max precision                0.985077     1         0
max recall                   0.0987423    1         110
max specificity              0.985077     1         0
max absolute_mcc             0.459516     0.480982  48
max min_per_class_accuracy   0.388266     0.724638  52
max mean_per_class_accuracy  0.459516     0.742754  48
max tns                      0.985077     69        0
max fns                      0.985077     45        0
max fps                      0.0400058    69        114
max tps                      0.0987423    46        110
max tnr                      0.985077     1         0
max fnr                      0.985077     0.978261  0
max fpr                      0.0400058    1         114
max tpr                      0.0987423    1         110

Gains/Lift Table: Avg response rate: 40.00 %, avg score: 42.86 %
   	group	cumulative_data_fraction	lower_threshold		...
--	-------	--------------------------	-----------------	...
   	1		0.0173913					0.956849			...
   	2		0.026087					0.953458			...
   	3		0.0347826					0.940891			...
   	4		0.0434783					0.922016			...
   	5		0.0521739					0.910929			...
   	6		0.104348					0.810679			...
   	7		0.156522					0.73798				...
   	8		0.2							0.652851			...
   	9		0.304348					0.574913			...
   	10		0.4							0.497339			...
   	11		0.504348					0.357667			...
   	12		0.6							0.278807			...
   	13		0.695652					0.248248			...
   	14		0.8							0.204899			...
   	15		0.895652					0.140332			...
   	16		1							0.0400058			...

lift		cumulative_lift		response_rate	score		...
--------	-----------------	---------------	--------
2.5			2.5					1				0.971004	...
2.5			2.5					1				0.956346	...
2.5			2.5					1				0.946034	...
2.5			2.5					1				0.933789	...
0			2.08333				0				0.912766	...
2.08333		2.08333				0.833333		0.878893	...
1.25		1.80556				0.5				0.764363	...
2			1.84783				0.8				0.676262	...
1.875		1.85714				0.75			0.605712	...
0.909091	1.63043				0.363636		0.53432		...
1.25		1.55172				0.5				0.407947	...
0.909091	1.44928				0.363636		0.313843	...
0.227273	1.28125				0.0909091		0.268551	...
0.416667	1.16848				0.166667		0.228816	...
0.454545	1.09223				0.181818		0.172153	...
0.208333	1					0.0833333		0.105524	...

cumulative_response_rate	cumulative_score	capture_rate	...
--------------------------	------------------	--------------	...
1							0.971004			0.0434783		...
1							0.966118			0.0217391		...
1							0.961097			0.0217391		...
1							0.955635			0.0217391		...
0.833333					0.94849				0				...
0.833333					0.913692			0.108696		...
0.722222					0.863915			0.0652174		...
0.73913						0.823121			0.0869565		...
0.742857					0.748581			0.195652		...
0.652174					0.697345			0.0869565		...
0.62069						0.637469			0.130435		...
0.57971						0.585877			0.0869565		...
0.5125						0.542245			0.0217391		...
0.467391					0.501363			0.0434783		...
0.436893					0.466204			0.0434783		...
0.4							0.428568			0.0217391		...

cumulative_capture_rate		gain		cumulative_gain
-------------------------	--------	-----------------
0.0434783					150			150
0.0652174					150			150
0.0869565					150			150
0.108696					150			150
0.108696					-100		108.333
0.217391					108.333		108.333
0.282609					25			80.5556
0.369565					100			84.7826
0.565217					87.5		85.7143
0.652174					-9.09091	63.0435
0.782609					25			55.1724
0.869565					-9.09091	44.9275
0.891304					-77.2727	28.125
0.934783					-58.3333	16.8478
0.978261					-54.5455	9.2233
1							-79.1667	0

---- End of Demo ----

Closing connection _sid_9233 at exit
H2O session _sid_9233 closed.
Closing connection _sid_bc7a at exit
H2O session _sid_bc7a closed.
$
```

