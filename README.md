# sscorer
**Scorer for machine learning predictions, similar to one used in online competition services like Kaggle**

## Usage
You can use the script as a command-line tool or import it to your python code directly.  
For command-line use:
```
$ python score.py --help
usage: score.py [-h] [-s SUBMISSION] [-c CHECK] [-m METRICS] [-i INDEX]

Macine learning models scoring tool

optional arguments:
  -h, --help            show this help message and exit
  -s SUBMISSION, --submission SUBMISSION
                        The submission file, must be in csv format (default:
                        submission.csv)
  -t CHECK, --check CHECK
                        The checking file, must be in csv format (default:
                        check.csv)
  -m METRICS, --metric METRICS
                        Which metric(s) to use (default: [])
  -i INDEX, --index INDEX
                        Specify index column (default: None)

$ python score.py -s submission.csv -c check.csv -m roc_auc_score -m log_loss
                column1   column2   column3  column4  column5  column6   mean columnwise
roc_auc_score   0.923     0.973     0.952    0.954    0.946    0.943     0.949
log_loss        0.173     0.031     0.09     0.013    0.103    0.031     0.073

```
For python direct importing:
```
from score import score_submission
print(score_submission(submission, check, ['roc_auc_score', 'log_loss']))

{'log_loss': [0.17269850991822863, 0.030838207413807328, 0.089855679603031799, 0.012972079895657513, 0.10258250873975795, 0.031238315864566841], 'roc_auc_score': [0.923469880129972, 0.97287448208784044, 0.95241365909023679, 0.9540124850945555, 0.94562071596391062, 0.94302913458223192]}
```
For detailed information on available metrics, visit http://scikit-learn.org/stable/modules/classes.html#sklearn-metrics-metrics
