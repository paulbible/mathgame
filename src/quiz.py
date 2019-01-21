"""A program to generate a random quiz
"""
import sympy
from src.mathqtools import SimplePoly1Generator, SimplePoly2Generator

def quiz_preamble(course='MAT', section=101,desc="Mathematics", quiz="Quiz 1", points_each=1):
    use_course = course + ' ' + str(section)
    pre = '''\\documentclass[10pt]{examdesign}
\\usepackage{amsmath}
\\usepackage{pifont}
\\usepackage{fmtcount}

\\setrandomseed{0}
\\SectionFont{\\large\\sffamily}
\\Fullpages
\\ContinuousNumbering
\\DefineAnswerWrapper{}{}
\\NumberOfVersions{1}

\\class{{\\Large %s: %s}}
\\examname{%s}

\\makeatletter
\\renewcommand\\namedata{
	Name: \\hrulefill \\\\[\\namedata@vspace]
	Date: \\hrulefill}
\\makeatother

\\begin{document}
''' % (use_course, desc, quiz)
    return pre


def start_question_block(points_each=1):
    if points_each > 1:
        point_msg = str(points_each) + ' points each'
    else:
        point_msg = str(points_each) + ' point each'
    block = '''\\begin{shortanswer}[title={Short Answer (%s)}, rearrange=no,resetcounter=no,suppressprefix]
    ''' % point_msg
    return block


def end_question_block():
    end = '''\\end{shortanswer}'''
    return end


def print_question(expr):
    question = '''\\begin{question}
	$%s$
	\\vspace{1cm}
	\\begin{answer}
		\{%s\}
	\\end{answer}
\\end{question}'''%(sympy.latex(expr), sympy.solveset(expr))
    return question


def end_document():
    return '\\end{document}'


def main():
    qGen = SimplePoly1Generator()
    qGen2 = SimplePoly2Generator()
    doc = ''
    doc += quiz_preamble() + '\n'
    doc += start_question_block() + '\n'
    for i in range(5):
        doc += print_question(qGen.Low_Whole_Eq()) + '\n'
    doc += print_question(qGen2.Simple_DEGREE2()) + '\n'
    doc += end_question_block() + '\n'
    doc += end_document()

    with open('../data/quiz.tex', 'w') as fout:
        fout.write(doc)

    print('Quiz Generated!')


main()
