from data_generator import load_dummy_data_from_hard_disc, save_dummy_data
import pandas

# save_dummy_data(path='static/', name='research_data.csv')

research_data = load_dummy_data_from_hard_disc(path='static/', name='research_data.csv')


def calc_sup(item_set):
    item_set = list(set(item_set))
    rules = [research_data[column_name] == 1 for column_name in item_set]
    df = pandas.DataFrame({"col_{0}".format(i): value for i, value in enumerate(rules)})
    mask = df.apply(lambda x: all(x), axis=1)
    return float(len(df[mask])) / len(research_data)


print calc_sup(["Alcohol Abuse", "Amputation of Limb"])

def calc_conf(item_set_a, item_set_b):
    return calc_sup(item_set_a + item_set_b) / calc_sup(item_set_b)

# print calc_conf(["Alcohol Abuse", "Amputation of Limb"], ["Alcohol Abuse"])

