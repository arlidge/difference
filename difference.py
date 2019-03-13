import difflib
text1 = "followersOld.txt"
text2 = "followersNew.txt"

text1_lines = open(text1).readlines()
text2_lines = open(text2).readlines()

difference = difflib.HtmlDiff().make_file(text1_lines, text2_lines, text1, text2)
difference_report = open('difference_report','w')
difference_report.write(difference)
difference_report.close()
