CXX = g++             
CXXFLAGS = -std=c++23 -Wall  


%: %.cpp             
	$(CXX) $(CXXFLAGS) $< -o $@
                              

.PHONY: clean       
clean:             
	rm -f *.o     

debug:
	@echo "Compiler: $(CXX)"
	@echo "Flags: $(CXXFLAGS)"
