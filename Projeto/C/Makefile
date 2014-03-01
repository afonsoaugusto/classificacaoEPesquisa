CC = gcc

CFLAGS = -Wall -g

RM = rm -f
OBJS = main.c util.c aleatorio.c define.h selection_sort.c bubble_sort.c

MAIN = atps

$(MAIN): $(OBJS)
	@echo ""
	@echo " --- COMPILANDO PROGRAMA ---"
	@$(CC) $(CFLAGS) $(OBJS) -lm -o $(MAIN)
	@echo ""

%.o: %.c %.h
	@echo " --- COMPILANDO OBJETO \"$@\""
	@$(CC) $(CFLAGS) $< -c 

clean:
	$(RM) $(MAIN) *.o
	clear

run: $(MAIN)
	./$(MAIN) 

