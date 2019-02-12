#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "ODALID.h"
#include "MfErrNo.h"

#define MI_OK 		0
#define Auth_KeyA   TRUE
#define Auth_KeyB   FALSE

unsigned char key_ff[6] = { 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF };
unsigned char key1[6] = { 0xA0, 0xA1, 0xA2, 0xA3, 0xA4, 0xA5 };
unsigned char key2[6] = { 0xB0, 0xB1, 0xB2, 0xB3, 0xB4, 0xB5 };
unsigned char key3[6] = { 0xC0, 0xC1, 0xC2, 0xC3, 0xC4, 0xC5 };
unsigned char key4[6] = { 0xD0, 0xD1, 0xD2, 0xD3, 0xD4, 0xD5 };
unsigned char dataToRead[240];
unsigned char dataToWrite[240];
unsigned char result[240];


char version[30];
char stackReader[20];

uint8_t serial[4];
uint8_t atq[2];
uint8_t sak[1];
uint8_t uid[12];
uint16_t uid_len = 12;

uint16_t status = MI_OK;
uint32_t  value = 0;



ReaderName cardReader;


int main(void){

    // 1 - INITIALISATION
    int status = CloseCOM(&cardReader);
    cardReader.Type = ReaderCDC;
    cardReader.device = 0;
    status = OpenCOM(&cardReader);
    RF_Power_Control(&cardReader, TRUE, 0);

    //2 - ACTIVATING
    status = ISO14443_3_A_PollCard(&cardReader, atq, sak, uid, &uid_len);
    if(status == MI_OK) {
        status = LEDBuzzer(&cardReader, LED_GREEN_ON);
        RF_Power_Control(&cardReader, TRUE, 2);
        status = Version(&cardReader, version, serial, stackReader);
    
    //3 - LOADING KEY
        status = Mf_Classic_LoadKey(&cardReader, Auth_KeyA, key1, 2);
        status = Mf_Classic_LoadKey(&cardReader, Auth_KeyB, key2, 2);
        status = Mf_Classic_LoadKey(&cardReader, Auth_KeyA, key3, 3);
        status = Mf_Classic_LoadKey(&cardReader, Auth_KeyB, key4, 3);

    //4 - INCREMENT 
        status = Mf_Classic_Increment_Value(&cardReader, TRUE, 14, 1, 13, Auth_KeyB, 3);
        status = Mf_Classic_Restore_Value(&cardReader, TRUE, 13, 14, Auth_KeyB, 3);
        status = Mf_Classic_Read_Value(&cardReader, TRUE, 13, &value, Auth_KeyA, 3);
        
    //5 - DECREMENT
        status = Mf_Classic_Decrement_Value(&cardReader, TRUE, 14, 1, 13, Auth_KeyA, 3);
        status = Mf_Classic_Restore_Value(&cardReader, TRUE, 13, 14, Auth_KeyA, 3);
        status = Mf_Classic_Read_Value(&cardReader, TRUE, 14, &value, Auth_KeyA, 3);
        printf("%d", value);
    }
    //OFF
    status = 0;
    RF_Power_Control(&cardReader, FALSE, 0);
    status = LEDBuzzer(&cardReader, LED_OFF);
    status = CloseCOM(&cardReader);
    

return 0;
}
