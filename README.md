# tomu-apps
firmwares for TOMU. These projects are simple programs for the [Tomu](http://tomu.im).

## How to build

- if arm-none-eabi-gcc is not in your path, add it. One way is to adapt `setup_gcc` to your local paths and then source it.
- libcm3 needs `python` but on most systems it is called `python3`. One way is to install pipenv and then `pipenv shell`
- then `make` should work as expected.