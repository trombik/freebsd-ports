# $FreeBSD$

PORTNAME=	stb
#PORTVERSION=
DISTVERSION=	20180819
CATEGORIES=	devel
#MASTER_SITES=

MAINTAINER=	y@trombik.org
COMMENT=	Single-file public domain (or MIT licensed) libraries for C/C++

LICENSE=	PD
#LICENSE_FILE=

USE_GITHUB=	yes
GH_TAGNAME=	e6afb9cb
GH_ACCOUNT=	nothings
NO_BUILD=	yes

do-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/include/${PORTNAME}
	${CP} ${WRKSRC}/*.c ${STAGEDIR}${PREFIX}/include/${PORTNAME}
	${CP} ${WRKSRC}/*.h ${STAGEDIR}${PREFIX}/include/${PORTNAME}

.include <bsd.port.mk>
