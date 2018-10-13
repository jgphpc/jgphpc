CC      = cc
CFLAGS  = -O3 $(INCDIRS)
SYSLIBS = -lpapi -L/opt/cray-hss-devel/default/lib/x86_64 -L/opt/cray/pmi/default/lib64 -dynamic -lrsmsevent -lglib-2.0

INCDIRS =
LIBDIRS =
LIBS =

papi_test: papi_test.o
	$(CC) $(CFLAGS) $(LIBDIRS) $^ -o $@ $(LIBS) $(SYSLIBS)

clean:
	rm -f *.o papi_test *~

