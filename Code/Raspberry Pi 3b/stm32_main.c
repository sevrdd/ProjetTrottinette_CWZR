#include "main.h"
#include <string.h>
#include <stdio.h>

#define RX_BUFFER_SIZE 256

char rx_buffer[RX_BUFFER_SIZE];
uint16_t rx_index = 0;

//to put in main while(1)
//this code acts only as a bridge and isn't doing any processing (yet)

uint8_t byte;

if(HAL_UART_Receive(&huart1, &byte, 1, 0) == HAL_OK) //agis comme pass through bridge

    if(HAL_UART_Receive(&huart1, &byte, 1, 0) == HAL_OK)
    {
        HAL_UART_Transmit(&huart2, &byte, 1, HAL_MAX_DELAY);
    }
