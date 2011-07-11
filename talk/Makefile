hic.pdf: hic.latex usage1.tex styles.tex
	latex -output-format=pdf hic.latex
usage1.tex: usage1.pycon
	pygmentize -l pycon -o usage1.tex usage1.pycon
styles.tex:
	pygmentize -S manni -f latex > styles.tex
