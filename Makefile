all: apps
	@true

apps:
	git submodule update --init --recursive
	make -C libopencm3
	make -C fake_mouse
	make -C rng

clean:
	make -C libopencm3 clean
	make -C fake_mouse clean
	make -C rng clean

.PHONY: apps
