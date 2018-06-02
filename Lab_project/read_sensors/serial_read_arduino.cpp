//get serial data on USB port from arduino

#include <unistd.h>
#include <fcntl.h>
#include <termios.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int serial_device = 0;

int conf_serial()
{
	serial_device = open("/dev/ttyUSB0" , O_RDWR | O_NOCTTY);
	if (serial_device < 0)
	{
		printf("error %d opening /dev/ttyUSB0: %s", errno,  strerror(errno));
		return -1;
	}
	struct termios tty;
	memset(&tty, 0, sizeof(tty));
	if (tcgetattr (serial_device, &tty) != 0)
	{
		printf("error %d from tcgetattr", errno);
		return -1;
	}
	cfsetospeed (&tty ,B9600);
	cfsetispeed (&tty ,B9600);
	tty.c_cflag = (tty.c_cflag & ~CSIZE) | CS8;

	tty.c_iflag &= ~IGNBRK;
	tty.c_lflag = 0;

	tty.c_oflag = 0;
	tty.c_cc[VMIN] = 0;
	tty.c_cc[VTIME] = 5;

	tty.c_iflag &= ~(IXON | IXOFF | IXANY);

	tty.c_cflag |= (CLOCAL | CREAD);

	tty.c_cflag &= ~(PARENB | PARODD);
	tty.c_cflag |= 0;
	tty.c_cflag &= ~CSTOPB;
	tty.c_cflag &= ~CRTSCTS;
	
	if(tcsetattr(serial_device, TCSANOW, &tty) != 0)
	{
		printf("error %d from tcsetaddr:%s \n", errno, strerror(errno));
		return -1;
	}

	return 0;
}

int send_read_request()
{
	char lRequestString[5] = "read";
	
	if(write(serial_device, lRequestString, 5) < 0)
	{
		printf("Error writing to /dev/ttyUSB0: %d: %s \n", errno,  strerror(errno));
		return -1;
	}
	return 0;
}

int get_data(char* lDataString)
{
	if(read(serial_device, lDataString, 40) < 0)
	{
		printf("Error reading from /dev/ttyUSB0: %d: %s \n", errno,  strerror(errno));
		return -1;
	}
	return 0;
}

int main()
{
	char* lInputBuffer;
	lInputBuffer = (char *)malloc(sizeof(char)*40);
	conf_serial();
	send_read_request();
	get_data(lInputBuffer);
	printf("%s", lInputBuffer);
	return 0;
}
