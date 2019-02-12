CC	= gcc
LD	= ld
CFLAGS	= -L/home/pi/rfid_reader/Access_Control -lODALID -pthread -D_REENTRANT -g -Wall -W
LDFLAGS	= -L/home/pi/rfid_reader/Access_Control -lODALID -pthread -D_REENTRANT -g -Wall -W
EXEC	= Access_Control
SRC	= $(wildcard *.c)
OBJ	= $(SRC:.c=.o)

all: $(EXEC)

Access_Control: $(OBJ)
				$(CC) -o $@ $^ $(LDFLAGS)
	
clean:
	rm -f *.o core

mrproper: clean

	rm -f $(EXEC)
	
