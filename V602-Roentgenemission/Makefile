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
build/plot1.pdf: plot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plot.py
build/plotbrom.pdf: plotbrom.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plotbrom.py
build/plotstrontium.pdf: plotstrontium.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plotstrontium.py
build/plotzirconium.pdf: plotzirconium.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plotzirconium.py
build/plotquecksilber.pdf: plotquecksilber.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plotquecksilber.py
build/bragg.pdf: bragg.py matplotlibrc header-matplotlib.tex | build
		TEXINPUTS="$(call translate,$(pwd):)" python bragg.py
build/plotmoseley.pdf: plotmoseley.py matplotlibrc header-matplotlib.tex | build
			TEXINPUTS="$(call translate,$(pwd):)" python plotmoseley.py
# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot.pdf build/plot.pdf build/plotbrom.pdf build/plotstrontium.pdf build/plotzirconium.pdf build/bragg.pdf build/plotquecksilber.pdf
								build/plotmoseley.pdf
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
