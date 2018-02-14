import argparse
import numpy as np
import pandas
from sklearn import metrics


def score_submission(submission, check, target_metrics):
    col_scores = {}
    submission.reindex(check.index.values)

    for metric in target_metrics:
        try:
            scores = [getattr(metrics, metric)(check[col], submission[col]) for col in check.keys()]
        except AttributeError:
            print('Metric {} does not exist'.format(metric))

        col_scores[metric] = scores

    return col_scores


def parse_args():
    parser = argparse.ArgumentParser(description='Macine learning submissions scoring tool',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s', '--submission', default='submission.csv', help='The submission file, must be in csv format')
    parser.add_argument('-c', '--check', default='check.csv', help='The checking file, must be in csv format')

    parser.add_argument('-m', '--metric', dest='metrics', action='append', default=[], help='Which metric(s) to use')
    parser.add_argument('-i', '--index', default=None, help='Specify index column')

    return parser.parse_args()


def main():
    args = parse_args()

    submission = pandas.read_csv(args.submission, index_col=args.index)
    check = pandas.read_csv(args.check, index_col=args.index)

    if submission.shape != check.shape:
        print('Submission and check have different shape, aborting')
        return

    if np.any(submission.keys() != check.keys()):
        print('Submission and check have different column names, aborting')
        return

    if not args.metrics:
        args.metrics = ['accuracy_score']

    col_scores = score_submission(submission, check, args.metrics)

    print(' ' * max([len(metric_name) for metric_name in args.metrics]) + '\t' +
          '\t'.join(list(submission.keys()) + ['mean columnwise']))

    for metric in args.metrics:
        print_str = metric
        for i, score in enumerate(np.round(col_scores[metric], 3)):
            print_str += '\t' + str(score) + ' ' * max(0, len(str(submission.keys()[i])) - 5)

        print_str += '\t' + str(np.round(np.mean(col_scores[metric]), 3))
        print(print_str)


if __name__ == '__main__':
    main()
