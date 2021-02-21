import pandas as pd


def one_hot_encode(df: pd.DataFrame, col: "list or string", top: "either None or an integer" = None) -> pd.DataFrame:
    if type(col) != list:
        col = [col]

    if top is None:
        return pd.get_dummies(df, columns=col)

    else:
        for column in col:
            # Get the top N column values - but thru pandas?
            freq_values = df[column].value_counts()[:top].index.tolist()
            # Create a new column to do the OneHot
            df[f'{column}_Other'] = [1 if value not in freq_values else 0 for value in df[column]]

            for value in freq_values:
                df[f'{column}_{value}'] = (df[column] == value).astype(int)
            df = df.drop(column, axis=1)

        return df


def label_encode(df, col, top=None):
    if type(col) != list:
        col = [col]

    if top is None:
        for c in col:
            df[f'{c}_LE'] = df[c].astype('category').cat.codes
            df.drop(c, axis=1, inplace=True)
            return df

    else:
        for c in col:
            freq_values = df[c].value_counts()[:top].index.tolist()
            d = dict.fromkeys(list(df[c]))

            for val in df[c]:
                if val not in freq_values:
                    d[val] = 'Other'
                else:
                    d[val] = val

            df[f'{c}_cat'] = df[c].map(d).astype('category')
            df[f'{c}_LE'] = df[f'{c}_cat'].cat.codes
            df = df.drop([c, f'{c}_cat'], axis=1)

        return df


def find_fill_na(df, col=None, strategy='mean'):
    if col is None:  # Search all, fill all
        col = list(df.columns)

    if type(col) != list:
        col = [col]

    for c in col:
        nulls = df[c].isnull().sum()
        if nulls == 0:
            continue

        if str(df[c].dtype) in ['object', 'category']:
            df[c] = df[c].fillna(df[c].mode())
        else:
            if strategy.strip().lower() == 'mean':
                val = df[c].mean()
            elif strategy.strip().lower() == 'median':
                val = df[c].median()
            else:
                raise ValueError('strategy must be either mean or median.')

            df[c] = df[c].fillna(val)

    return df


if __name__ == '__main__':
    import doctest
    doctest.testmod()
