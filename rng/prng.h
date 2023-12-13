#pragma once
void prng_seed(
	uint32_t*state	//256 bits seed
	);
void prng_step(
	uint32_t*dst    //128 bit destination buffer
	);

