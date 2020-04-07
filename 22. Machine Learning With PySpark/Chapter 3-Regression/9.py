# Flight duration model: Regularisation!
# In the previous exercise you added more predictors to the flight duration model. The model performed well on testing data, but with so many coefficients it was difficult to interpret.

# In this exercise you'll use Lasso regression (regularized with a L1 penalty) to create a more parsimonious model. Many of the coefficients in the resulting model will be set to zero. This means that only a subset of the predictors actually contribute to the model. Despite the simpler model, it still produces a good RMSE on the testing data.

# You'll use a specific value for the regularization strength. Later you'll learn how to find the best value using cross validation.

# The data (same as previous exercise) are available as flights, randomly split into flights_train and flights_test.

# Instructions
# 100 XP
# Fit a linear regression model to the training data.
# Calculate the RMSE on the testing data.
# Look at the model coefficients.
# Get the count of coefficients equal to 0.
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

# Fit Lasso model (α = 1) to training data
regression = LinearRegression(labelCol='duration', regParam=1, elasticNetParam=1).fit(flights_train)

# Calculate the RMSE on testing data
rmse = RegressionEvaluator(labelCol='duration').evaluate(regression.transform(flights_test))
print("The test RMSE is", rmse)

# Look at the model coefficients
coeffs = regression.coefficients
print(coeffs)

# Number of zero coefficients
zero_coeff = sum([beta == 0 for beta in regression.coefficients])
print("Number of ceofficients equal to 0:", zero_coeff)