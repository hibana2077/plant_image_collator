example_data = [
    {
        "feature1": 1,
        "feature2": 2,
        "feature3": 3,
    },
    {
        "feature1": 4,
        "feature2": 5,
        "feature3": 6,
    },
    {
        "feature1": 7,
        "feature2": 8,
        "feature3": 9,
    }
]

import pandas as pd

df = pd.DataFrame(example_data)

print(df)