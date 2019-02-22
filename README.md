# password-audit-reporting-and-graphing
## Password Audit Reporting and Graphing

This is a Python3 tool used as part of a password audit. It is used for reporting and graphing.

This takes an input file (regular text file with passwords per line) and creates statistics and graphs.

```
usage: pw_audit_graphing.py [-h] [-c COMPANY_NAME] [-i INPUT_FILE]
                            [-o OUTPUT_FILE] [-s STYLE]

Password Audit Reporting and Graphing by GameOfPWNZ (https://gameofpwnz.com).
This Python3 tool takes an input file with passwords and counts characters,
searches for strings, and creates statistics and graphs.

optional arguments:
  -h, --help       show this help message and exit
  -c COMPANY_NAME  Company name or initials (String)
  -i INPUT_FILE    Input file (eg. input.txt)
  -o OUTPUT_FILE   Output file (HTML)
  -s STYLE         MatPlotLib Style: Default (seaborn-darkgrid)
                   https://tonysyu.github.io/raw_content/matplotlib-style-
                   gallery/gallery.html
```
## Example Output

![Example HTML Output](https://gameofpwnz.com/wp-content/uploads/2019/02/html_output.png)
