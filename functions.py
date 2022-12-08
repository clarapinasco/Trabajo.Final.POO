import matplotlib.pyplot as plt
import seaborn as sns


def data_dist(df,var):
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    ax[0].set_title(f"Distribucion de {var}")
    sns.histplot(data=df, x=f"{var}", kde=True, ax=ax[0])

    ax[1].set_title(f"Boxplot de{var}")
    sns.boxplot(data=df, x=f"{var}", ax=ax[1])


def valor_atipico(df,var):
   outlier=df[var].quantile(0.75) + 1.5 * (df[var].quantile(0.75) - df[var].quantile(0.25))
   return int(outlier)