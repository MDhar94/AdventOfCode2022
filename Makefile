DAY=2
newday:
	cp template.py challenges/Day$(DAY).py
	code .
