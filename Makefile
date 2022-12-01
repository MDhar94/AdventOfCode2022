DAY=1
newday:
	mkdir $(DAY)
	cp template.py $(DAY)/$(DAY).py
	code .
