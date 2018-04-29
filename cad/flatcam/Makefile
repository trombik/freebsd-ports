# $FreeBSD$

PORTNAME=	flatcam
PORTVERSION=	8.5
CATEGORIES=	cad
MASTER_SITES=	https://bitbucket.org/jpcgt/flatcam/get/
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}
DISTNAME=	${FLATCAM_COMMIT_TAG}
#MASTER_SITES=	https://bitbucket.org/jpcgt/flatcam/downloads/
#DISTNAME=	FlatCAM-${PORTVERSION}

MAINTAINER=	y@trombik.org
COMMENT=	Free and Open-source PCB CAM

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}numpy>0:math/py-numpy@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}matplotlib>0:math/py-matplotlib@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}Shapely>0:devel/py-shapely@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}rtree>0:devel/py-rtree@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}simplejson>0:devel/py-simplejson@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}scipy>0:science/py-scipy@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}svg.path>0:graphics/py-svg.path@${PY_FLAVOR}

USES=	python:3.4+ pyqt:4 zip shebangfix
USE_PYQT=	core_run gui_run
NO_ARCH=	yes
NO_BUILD=	yes
FLATCAM_COMMIT_TAG=	46454c293a9b
WRKSRC=	${WRKDIR}/jpcgt-flatcam-${FLATCAM_COMMIT_TAG}
SHEBANG_FILES=	${WRKSRC}/flatcam

do-install:
	${RM} ${WRKSRC}/*.orig
	${MKDIR} ${STAGEDIR}${PREFIX}/${PORTNAME}
	(cd ${WRKSRC} && ${COPYTREE_SHARE} . ${STAGEDIR}${PREFIX}/${PORTNAME})

	${CP}  ${FILESDIR}/flatcam.in ${WRKSRC}/flatcam_wrapper
	@${REINPLACE_CMD} -e 's|%%PREFIX%%|${PREFIX}|g' \
		-e 's|%%PORTNAME%%|${PORTNAME}|g' \
		-e 's|%%PYTHON_CMD%%|${PYTHON_CMD}|g' \
		${WRKSRC}/flatcam_wrapper
	${CHMOD} +x ${WRKSRC}/flatcam_wrapper
	${MV} ${WRKSRC}/flatcam_wrapper ${STAGEDIR}${PREFIX}/bin/flatcam

.include <bsd.port.mk>
