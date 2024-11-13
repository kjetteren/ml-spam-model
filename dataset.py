from ucimlrepo import fetch_ucirepo

def dataset():
    """PhiUSIIL Phishing URL (Website) dataset retrival function.
    (https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset)

    Returns:
        data.features: Pandas DataFrame containing features extracted from the dataset.
        data.targets: Pandas DataFrame containing targets extracted from the dataset.
    """
    # dataset
    phiusiil_phishing_url_website = fetch_ucirepo(id=967)

    # data (as pandas dataframes)
    x = phiusiil_phishing_url_website.data.features
    y = phiusiil_phishing_url_website.data.targets

    # metadata
    print(phiusiil_phishing_url_website.metadata)

    # variable information
    print(phiusiil_phishing_url_website.variables)

    return x, y