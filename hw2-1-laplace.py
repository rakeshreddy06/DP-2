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


<<<<<<< HEAD
print(privacy_function(1))
=======
DF_0_5=privacy_function(0.5)
DF_1=privacy_function(1)

print(f' average age before laplace noise: {avg_age()}')
print(f'The average age after laplace noise is e=0.5: {DF_0_5}')
print(f'The average age after laplace noise is e=1: {DF_1}')

>>>>>>> bf4d40e (Dp-2)
