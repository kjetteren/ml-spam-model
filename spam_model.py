from ucimlrepo import fetch_ucirepo

def spam_model():
    """Spam model based on the PhiUSIIL Phishing URL (Website) Model
    (https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset)
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