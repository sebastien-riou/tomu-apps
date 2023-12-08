all: apps
	@true

apps:
	git submodule update --init --recursive
	make -C libopencm3
	make -C fake_mouse

clean:
	make -C libopencm3 clean
	make -C fake_mouse clean

.PHONY: apps
