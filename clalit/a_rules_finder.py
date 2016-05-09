from data_generator import load_dummy_data_from_hard_disc, save_dummy_data
from itertools import chain, combinations
import datetime
import pandas

# save_dummy_data(path='static/', name='research_data.csv')

research_data = load_dummy_data_from_hard_disc(path='static/', name='research_data.csv')
research_data_len = len(research_data)
statistic_data = pandas.DataFrame.from_csv(path='static/statistics.csv', index_col=False)


def reshape_data(df):
    df = df.applymap(lambda x: str(x).replace('  ', ' '))

    return df

statistic_data = reshape_data(statistic_data)
research_data = reshape_data(research_data)
research_data = research_data.applymap(lambda x: int(x))


def calc_sup(item_set, data_df):
    s = data_df[list(item_set)].all(axis=1).sum()
    return float(s) / research_data_len


def calc_conf(item_set_a, item_set_b, data_df,
              sup_item_set_a=None, sup_item_set_b=None, sup_both_itemesets=None):
    if sup_item_set_b is None:
        sup_item_set_b = calc_sup(item_set_b, data_df)

    if sup_both_itemesets is None:
        sup_both_itemesets = calc_sup(item_set_a + item_set_b, data_df)

    if sup_item_set_b > 0:

        return sup_both_itemesets / sup_item_set_b

    else:
        return 0


def powerset(iterable, max_len):
    xs = list(iterable)
    return chain.from_iterable(combinations(xs, n) for n in range(1, max_len))


def split_data_to_rare_and_common_deseases(min_sup_for_common_disease):
    statistic_data['Percentage'] = statistic_data['Percentage'].apply(lambda x: x.replace("%", ''))
    rare_diseases_columns = statistic_data[
        statistic_data['Percentage'].astype(float) < min_sup_for_common_disease]['Disease']
    common_diseases_columns = statistic_data[
        statistic_data['Percentage'].astype(float) >= min_sup_for_common_disease]['Disease']
    rare_diseases_df = research_data[list(rare_diseases_columns.values)]
    common_diseases_df = research_data[list(common_diseases_columns)]

    common_diseases_df = common_diseases_df.applymap(lambda x: int(x))
    rare_diseases_df = rare_diseases_df.applymap(lambda x: int(x))

    return common_diseases_df, rare_diseases_df


def run_minning():
    print(datetime.datetime.now())
    min_sup_for_common_disease = 1
    final_df = pandas.DataFrame({"base": [], "data": [], "sup": [], "conf": []})
    common_diseases_df, rare_diseases_df = \
        split_data_to_rare_and_common_deseases(min_sup_for_common_disease=min_sup_for_common_disease)
    base_rule_iterator = powerset(common_diseases_df.columns.values[1:], 4)

    i = 0

    for base in base_rule_iterator:
        data_rule_iterator = powerset(common_diseases_df.columns.values[1:], 2)
        for data in data_rule_iterator:
            if data != base:
                base_sup = calc_sup(base, research_data)
                rule_conf = calc_conf(base, data, research_data)
                final_df.ix[len(final_df) + 1] = [base, rule_conf, data, base_sup]

        if len(final_df) > 50000:
            i += 1
            final_df = final_df[['base', 'data', 'sup', 'conf']]
            final_df.to_csv("final_data_{0}.csv".format(i), index=False)
            final_df = pandas.DataFrame({"base": [], "data": [], "sup": [], "conf": []})

    i += 1
    final_df = final_df.replace('(', '')
    final_df = final_df.replace(')', '')
    final_df = final_df.replace("'", '')
    final_df.to_csv("final_data_{0}.csv".format(i), index=False)
    print(datetime.datetime.now())


run_minning()
