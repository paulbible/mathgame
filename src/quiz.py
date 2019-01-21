"""A program to generate a random quiz
"""
import sympy
from src.mathqtools import SimplePoly1Generator

def quiz_preamble():
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

\\class{{\\Large CATS 171: Procedural Programming}}
\\examname{Exam 1, 100 points}

\\makeatletter
\\renewcommand\\namedata{
	Name: \\hrulefill \\\\[\\namedata@vspace]
	Date: \\hrulefill}
\\makeatother

\\begin{document}
'''
    return pre


def start_question_block():
    block = '''\\begin{shortanswer}[title={Short Answer (4 points each)}, rearrange=no,resetcounter=no,suppressprefix]
    '''
    return block


def end_question_block():
    end = '''\\end{shortanswer}'''
    return end


def print_question(expr):
    question = '''\\begin{question}
	%s
	\\vspace{1cm}
	\\begin{answer}
		%s
	\\end{answer}
\\end{question}'''%(sympy.latex(expr), sympy.solveset(expr))
    return question


def end_document():
    return '\\end{document}'


def main():
    qGen = SimplePoly1Generator()
    doc = ''
    doc += quiz_preamble() + '\n'
    doc += start_question_block() + '\n'
    for i in range(5):
        doc += print_question(qGen.Low_Whole_Eq()) + '\n'
    doc += end_question_block() + '\n'
    doc += end_document()

    with open('data/quiz.tex', 'w') as fout:
        fout.write(doc)


main()
