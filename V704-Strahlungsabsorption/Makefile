ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  # Unix
  pwd := $$(pwd)
  translate = $1
else
  # Windows mit MSys2/Cygwin
  pwd := $$(cygpath -m "$$(pwd)")
  translate = $(shell echo '$1' | sed 's/:/;/g')
endif

all: build/main.pdf

# hier Python-Skripte:
build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plot.py
<<<<<<< HEAD
build/plot1.pdf: plot1.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plot1.py
||||||| merged common ancestors
=======
build/plotblei.pdf: plotblei.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plotblei.py
>>>>>>> somethiing

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
<<<<<<< HEAD
build/main.pdf: build/plot.pdf build/plot1.pdf
||||||| merged common ancestors
build/main.pdf: build/plot.pdf
=======
build/main.pdf: build/plot.pdf build/plotblei.pdf
>>>>>>> somethiing

build/main.pdf: FORCE | build
	  TEXINPUTS="$(call translate,build:)" \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
