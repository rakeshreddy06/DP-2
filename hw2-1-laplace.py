import pandas as pd
import numpy as np

path = "adult.data"
columns = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship",
           "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "salary"]
df = pd.read_csv(path, names=columns, skipinitialspace=True)


def avg_age():
    return df[df['age'] > 25]['age'].mean()


def age_global_sensitivity():
    filtered_df = df[df['age'] > 25]
    min_age = filtered_df['age'].min()
    max_age = filtered_df['age'].max()
    count = filtered_df['age'].shape[0]
    return (max_age - min_age) / count


def laplace_noise(epsilon, gf):
    b = gf / epsilon
    noise = np.random.laplace(loc=0, scale=b)

    return noise


def privacy_function(epsilon):
    age_avg = avg_age()
    gf = age_global_sensitivity()
    noise = laplace_noise(epsilon, gf)
    return age_avg + noise


print(privacy_function(1))
