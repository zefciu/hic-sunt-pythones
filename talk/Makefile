hic.pdf: hic.latex usage1.tex usage2.tex descr1.tex descr2.tex styles.tex versionable.tex problem.tex meta_expl.tex meta.tex Makefile
	latex -output-format=pdf hic.latex

styles.tex: Makefile
	pygmentize -S manni -f latex > styles.tex

usage1.tex: usage1.pycon Makefile
	pygmentize -l pycon -o usage1.tex usage1.pycon

usage2.tex: usage2.pycon Makefile
	pygmentize -l pycon -o usage2.tex usage2.pycon

descr1.tex: descr1.py Makefile
	pygmentize -o descr1.tex descr1.py

descr2.tex: descr2.py Makefile
	pygmentize -o descr2.tex descr2.py

versionable.tex: versionable.py Makefile
	pygmentize -o versionable.tex versionable.py

problem.tex: problem.py Makefile
	pygmentize -o problem.tex problem.py

meta_expl.tex: meta_expl.py Makefile
	pygmentize -o meta_expl.tex meta_expl.py

meta.tex: meta.py Makefile
	pygmentize -o meta.tex meta.py
