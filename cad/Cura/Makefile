# Created by: Tomoyuki Sakurai <y@trombik.org>
# $FreeBSD$

PORTNAME=	Cura
PORTVERSION=	3.0.3
CATEGORIES=	cad

MAINTAINER=	y@trombik.org
COMMENT=	3D printer / slicing GUI application

LICENSE=	LGPL3
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS= ${PYTHON_PKGNAMEPREFIX}uranium=${PORTVERSION}:devel/py-uranium
RUN_DEPENDS=	\
	${PYTHON_PKGNAMEPREFIX}scipy>0:science/py-scipy \
	${PYTHON_PKGNAMEPREFIX}serial>0:comms/py-serial \
	${PYTHON_PKGNAMEPREFIX}uranium=${PORTVERSION}:devel/py-uranium \
	${PYTHON_PKGNAMEPREFIX}zeroconf>0:net/py-zeroconf \
	${PYTHON_SITELIBDIR}/PyQt5/QtOpenGL.so:x11/py-qt5-opengl \
	${PYTHON_SITELIBDIR}/PyQt5/QtQuick.so:x11-toolkits/py-qt5-quick \
	cura-resources-materials=${PORTVERSION}:cad/cura-resources-materials \
	cura-binary-data=${PORTVERSION}:cad/cura-binary-data \
	CuraEngine=${PORTVERSION}:cad/CuraEngine
TEST_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pytest>0:devel/py-pytest

USES=		python:3.5+ cmake pyqt:5 fortran
USE_GCC=	yes
USE_GITHUB=	yes
GH_ACCOUNT=	Ultimaker
USE_PYQT=	svg network qml opengl
INSTALL_TARGET=	install

post-install:
	${RM} -rf ${STAGEDIR}${PREFIX}/lib/cura/plugins/SliceInfoPlugin
	# XXX workaround ports/207750
	# https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=207750
	${MV} ${STAGEDIR}${PREFIX}/bin/cura ${STAGEDIR}${PREFIX}/bin/cura_app
	${CP} ${FILESDIR}/cura_wrapper ${STAGEDIR}${PREFIX}/bin/cura
	${REINPLACE_CMD} -e 's|%%_GCC_RUNTIME%%|${_GCC_RUNTIME}|' \
		-e s'|%%PREFIX%%|${PREFIX}|' \
		${STAGEDIR}${PREFIX}/bin/cura
	${CHMOD} 755 ${STAGEDIR}${PREFIX}/bin/cura

do-test:
	# XXX skip some tests that have been failing
	# https://github.com/Ultimaker/Cura/issues/2954
	#
	# "It's always a race between releasing on the deadline and delivering the
	# best code possible."
	cd ${WRKSRC} && ${PYTHON_CMD} -m pytest -v \
		-k "not TestCuraContainerRegistry and not TestExtruderStack and not TestGlobalStack"

.include <bsd.port.mk>
