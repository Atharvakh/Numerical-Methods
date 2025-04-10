CC = g++
CCFLAGS = -I. -Wall -Wextra -pedantic
DEPS = matrix.hpp
TARGET = MATRIX
OBJS = add.o basic.o main.o

%.o: %.cpp $(DEPS)
	$(CC) $(CCFLAGS) -c $< -o $@

$(TARGET): $(OBJS)
	$(CC) $(CCFLAGS) -o $@ $^

clean:
	rm -f $(OBJS) $(TARGET)
