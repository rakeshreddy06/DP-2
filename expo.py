import pandas as pd
import numpy as np

path = "adult.data"
columns = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship",
           "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "salary"]
df = pd.read_csv(path, names=columns, skipinitialspace=True)


def exponential_mechanism(df, epsilon, sensitivity, utility_function):
    education_values = df['education'].unique()
    utility_scores = [utility_function(df, edu) for edu in education_values]
    scaling_factor = 1000
    utility_scores = [score / scaling_factor for score in utility_scores]
    probabilities = np.exp(epsilon * np.array(utility_scores) / (2 * sensitivity))
    probabilities /= np.sum(probabilities)
    return np.random.choice(education_values, p=probabilities)


def utility_function(df, education):
    return len(df[df['education'] == education])


sensitivity = 1

private_frequent_education_0_5 = exponential_mechanism(df, epsilon=0.5, sensitivity=sensitivity,
                                                       utility_function=utility_function)
print(f"Exponential mechanism  most frequent education (ε = 0.5): {private_frequent_education_0_5}")

private_frequent_education_1 = exponential_mechanism(df, epsilon=1, sensitivity=sensitivity,
                                                     utility_function=utility_function)
print(f"Exponential mechanism frequent education (ε = 1): {private_frequent_education_1}")
