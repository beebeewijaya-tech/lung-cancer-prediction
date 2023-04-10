from src.model.person import Person
import pickle

dt_model = pickle.load(open("models/decision_tree.pkl", "rb"))
dt_sc = pickle.load(open("models/decision_tree_scaler.pkl", "rb"))


def predicting_lung_cancer(body: Person):
    print(body)
    payload = [[body.age, body.alcohol_consuming,
                body.allergy, body.chest_pain, body.wheezing]]

    sc_payload = dt_sc.transform(payload)
    result = dt_model.predict(sc_payload)

    return result[0]
