CFLAGS = -O3 -I.

RM = rm -f

CC = gcc

OBJS = egsa87.o calculate.o
SRCS = egsa87.c calculate.c

calculate: ${OBJS}
	${CC} ${LDFLAGS} -o calculate ${OBJS}

clean:
	${RM} ${OBJS} calculate
