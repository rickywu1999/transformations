run: main.py
	python main.py
	convert pic.ppm pic.png

clean:
	rm *.pyc
	rm pic.ppm
	rm pic.png
