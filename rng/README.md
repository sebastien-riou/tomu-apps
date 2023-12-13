# RNG

This turns TOMU into a random number generator.
It works only if toboot is generating random seed, see the [seed branch](https://github.com/sebastien-riou/toboot/tree/seed)

On the host side, TOMU apears as a UART, just read it to get random numbers.

It toggles the red LED each time a rare condition occurs. The red LED is therefore expected to blink randomly (no matter if the output is read or not).