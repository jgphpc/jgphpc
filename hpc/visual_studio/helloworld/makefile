RM := rm -f
CXX := g++-9
CXXFLAGS := --debug -std=c++17
EXECUTABLE := myexe
all: $(EXECUTABLE)

OBJS := hello.o

$(OBJS):
	@echo 'Compiling: $@'
	@echo '$(PREP) $(CXX) $(CXXFLAGS) -c -o $(@) $(@:.o=.cpp)'
	$(PREP) $(CXX) $(CXXFLAGS) -c -o $(@) $(@:.o=.cpp)

$(EXECUTABLE): $(OBJS)
	@echo 'Linking: $@'
	$(PREP) $(CXX) $(CXXFLAGS) $(LDFLAGS) -o $(@) $(OBJS)
	@echo 'Finished building: $@'
	@echo ' '

clean:
	@echo 'Removing objects'
	-$(RM) $(OBJS)
	-@echo ' '

distclean:
	@echo 'Removing objects and executable'
	-$(RM) $(OBJS) $(EXECUTABLE)
	-@echo ' '
