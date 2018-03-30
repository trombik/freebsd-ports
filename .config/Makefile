SUBDIR += options

install:
.for D in ${SUBDIR}
	${MAKE} -C ${.CURDIR}/${D} install
.endfor
