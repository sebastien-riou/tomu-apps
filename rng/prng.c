#include "efm32hg309f64.h"
#include "prng.h"

static void aes128_clock_enable(void){
    CMU->HFCORECLKEN0 |= CMU_HFCORECLKEN0_AES;
    
}
static void aes128_enc_mode(void){
    //Select encryption mode.
    AES->CTRL = 0;
}
static void aes128_start(void){
    //Select encryption mode.
    AES->CMD = AES_CMD_START;
}
static void aes128_load_key(uint32_t*key){
    for (unsigned int i = 0; i < 4; i++) {
      AES->KEYLA = key[i];
    }
}
static void aes128_get_key(uint32_t*key){
    for (unsigned int i = 0; i < 4; i++) {
      key[i] = AES->KEYLA;
    }
}
static void aes128_enc_dat(uint32_t*dat){
    for (unsigned int i = 0; i < 4; i++) {
      AES->DATA = dat[i];
    }
    AES->CMD = AES_CMD_START;
}
static void aes128_get_dat(uint32_t*dat){
    // Wait for completion.
    while (AES->STATUS & AES_STATUS_RUNNING);
    for (unsigned int i = 0; i < 4; i++) {
      dat[i] = AES->DATA;
    }
}

void prng_seed(
	uint32_t*seed	//256 bits seed
	){
    (void)aes128_get_key; //remove ununsed warning
    aes128_clock_enable();
    aes128_enc_mode();
	aes128_load_key(seed);
    aes128_enc_dat(seed+4); // this start AES
}
void prng_step(
	uint32_t*dst    //128 bit destination buffer
	){
	aes128_get_dat(dst);
    aes128_start();
}
