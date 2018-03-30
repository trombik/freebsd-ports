OPTIONS_DIR?=	devel-options

PREFIX?=	/usr/local
PORTSDIR=	${.CURDIR}/../../
POUDRIERE?=	${PREFIX}/bin/poudriere
POUDRIERE_DIR=	${PREFIX}/etc/poudriere.d

# ignore owner when invokded by root
EUID!=	id -u
.if ${EUID} == "0"
EXTRA_CPIO_FLAGS?=	--no-preserve-owner
.else
EXTRA_CPIO_FLAGS?=
.endif
_SHAREMODE?=	0644

# shamelessly copied from bsd.port.mk with additional flag,
# `--no-preserve-owner`
COPYTREE_SHARE=	${SH} -c '(${FIND} -Ed $$1 $$3 | ${CPIO} ${EXTRA_CPIO_FLAGS} -dumpl $$2 >/dev/null 2>&1) && \
						   ${FIND} -Ed $$1 $$3 \(   -type d -exec ${SH} -c '\''cd '\''$$2'\'' && chmod 755 "$$@"'\'' . {} + \
												 -o -type f -exec ${SH} -c '\''cd '\''$$2'\'' && chmod ${_SHAREMODE} "$$@"'\'' . {} + \)' COPYTREE_SHARE

install:
.for D in ${OPTIONS_DIR}
	${RM} -r ${POUDRIERE_DIR}/.${D}
	${INSTALL} -d ${POUDRIERE_DIR}/.${D}
	(cd ${.CURDIR}/${D} && ${COPYTREE_SHARE} . ${POUDRIERE_DIR}/.${D})
	if [ -e ${POUDRIERE_DIR}/${D} ]; then \
		${RM} -r ${POUDRIERE_DIR}/${D}.old && ${MV} ${POUDRIERE_DIR}/${D} ${POUDRIERE_DIR}/${D}.old; \
	fi
	${MV} ${POUDRIERE_DIR}/.${D} ${POUDRIERE_DIR}/${D}
.endfor

.include <${PORTSDIR}/Mk/bsd.commands.mk>
