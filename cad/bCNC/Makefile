# $FreeBSD$

PORTNAME=	bCNC
PORTVERSION=	0.9.11
CATEGORIES=	cad
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	y@trombik.org
COMMENT=	GRBL CNC command sender, autoleveler and g-code editor

LICENSE=	GPLv2
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}tkinter>0:x11-toolkits/py-tkinter@${FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}serial>0:comms/py-serial@${FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}opencv>0:graphics/py-opencv@${FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}pillow>0:graphics/py-pillow@${FLAVOR}

USES=	python:2.7 shebangfix
USE_PYTHON=	flavors
SHEBANG_FILES=	bCNC.py \
	plugins/bowl.py \
	plugins/box.py \
	plugins/driller.py \
	plugins/flatten.py \
	plugins/gear.py \
	plugins/halftone.py \
	plugins/heightmap.py \
	plugins/hilbert.py \
	plugins/midi2cnc.py \
	plugins/pyrograph.py \
	plugins/sketch.py \
	plugins/spirograph.py \
	plugins/text.py \
	plugins/tile.py \
	plugins/zigzag.py

USE_GITHUB=	yes
GH_ACCOUNT=	vlachoudis
GH_PROJECT=	${PORTNAME}
GH_TAGNAME=	${PORTVERSION}
NO_BUILD=	yes

.include <bsd.port.pre.mk>

pre-install:
	${REINPLACE_CMD} -e 's|%%PORTNAME%%|${PORTNAME}|g' \
		-e 's|%%PYTHON_CMD%%|${PYTHON_CMD}|g' \
		-e 's|%%LOCALBASE%%|${LOCALBASE}|g' \
		${WRKSRC}/bCNC

do-install:
	${PYTHON_CMD} -O -m py_compile ${WRKSRC}/*.py
	${RM} ${WRKSRC}/.git_cache_meta
	${INSTALL} -d ${STAGEDIR}${PREFIX}/${PORTNAME}
	(cd ${WRKSRC} && ${COPYTREE_SHARE} . ${STAGEDIR}${PREFIX}/${PORTNAME}/)
	${CHMOD} 755 ${STAGEDIR}${PREFIX}/${PORTNAME}/bCNC
	${MV} ${STAGEDIR}${PREFIX}/${PORTNAME}/bCNC ${STAGEDIR}${PREFIX}/bin/
	${CHMOD} 755 ${STAGEDIR}${PREFIX}/${PORTNAME}/bCNC.py

.include <bsd.port.post.mk>
