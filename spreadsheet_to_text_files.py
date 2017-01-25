"""
convert a spreadsheet to a directory of text files. Rows in Column A become
lines in file A.txt, rows in column B become lines in file B.txt, and so on
"""

import logging
import openpyxl
import os
from openpyxl.utils import get_column_letter
from srhpytools_srh.options.parsers import GenArgParser
from srhpytools_srh.util.mylogging import config_root_file_logger

logger = logging.getLogger('automate_boring.spreadsheet_to_text_files')


def main(filename, outdir):
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    # the (not much of a) trick here will be to not write out a ton of blank
    #  lines at the end of shorter files. it should be fairly
    # straightforward to remove last several blanks from each list of lines
    # i creates
    raise NotImplementedError


if __name__ == '__main__':
    parser = GenArgParser(usage='%(prog)s -f filename [-d outdir] [options]')
    parser.add_argument('-f', '--filename', help='excel file to convert')
    parser.add_argument('-d', '--outdir', help='directory to write text '
                                               'files to')
    args = parser.parse_args()
    config_root_file_logger(args.logfile, args.loglevel, args.logmode)
    main(args.filename, args.outdir)
