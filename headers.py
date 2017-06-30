import argparse
import os.path
import sys

# def parse_args():
#     parser = argparse.ArgumentParser(description="This program is used to convert "
#                                                     "headers into a table of contents")
#     parser.add_argument("-f", "--filename", type=str,  default="input.txt", help="Input filename")
#     return parser
#
# parser = parse_args()
# args = parser.parse_args()
list = []
try:
    out = open(os.path.expanduser("~/Downloads/output.txt"), "w")
    out.write("<style>\n"
            "\ttd {\n"
                "\t\tpadding-right: 10px;\n"
            "\t}\n"
        "</style>\n\n\n\n")
    out.write("<strong>Table of Contents</strong>\n"
	"<table class=\"fixed\" width=\"100%\">\n"
        "<tbody>\n"
        "<col width=\"4%\">\n")
    with open(os.path.expanduser("~/Downloads/input.txt")) as f:
        i = 0
        for line in f:
            list.append(line.strip().split(' ', 1))
            # list[i][1] = ''.join(j for j in list[i][1] if j.isalnum())
            out.write("<tr>\n"
                "<td style=\"text-align:right\">{}</td>\n"
                "<td><a href=\"#{}\">{}</a></td>\n"
                "</tr>\n".format(list[i][0], list[i][0].replace(':', '') + ''.join(j for j in list[i][1] if j.isalnum()), list[i][1]))
            print list[i]
            i = i + 1
    out.write("</tbody>\n"
        "</table>\n\n")
    for item in list:
        # print item
        out.write("<h2 id=\"{}\">{} {}</h2>\n".format(item[0].replace(':', '') + ''.join(j for j in item[1] if j.isalnum()), item[0], item[1]))
except:
    # print parser.print_help()
    raise
