RM := rm -f

ifeq ($(CUDATOOLKIT_HOME),)
    $(error module load craype-accel-nvidia60)
endif

ifeq ($(PE_ENV),PGI)
    CFLAGS += -acc -ta=tesla,cc60
endif

ifeq ($(PE_ENV),CRAY)
    CFLAGS += -hacc -hnoomp
endif

ifeq ($(PE_ENV),GNU)
    CFLAGS += -fopenacc -lm
endif

.SUFFIXES: .o .c

clean:
	-$(RM) *.o
