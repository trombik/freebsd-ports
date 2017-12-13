# Created by: Tomoyuki Sakurai <y@trombik.org>
# $FreeBSD$

PORTNAME=	Cura
PORTVERSION=	3.0.3
CATEGORIES=	cad

MAINTAINER=	y@trombik.org
COMMENT=	3D printer / slicing GUI application

LICENSE=	LGPL3
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS= ${PYTHON_PKGNAMEPREFIX}uranium>0:devel/py-uranium
RUN_DEPENDS=	CuraEngine>0:cad/CuraEngine \
	${PYTHON_PKGNAMEPREFIX}uranium>0:devel/py-uranium \
	${PYTHON_PKGNAMEPREFIX}scipy>0:science/py-scipy \
	${PYTHON_PKGNAMEPREFIX}serial>0:comms/py-serial \
	${PYTHON_SITELIBDIR}/PyQt5/QtQuick.so:x11-toolkits/py-qt5-quick \
	${PYTHON_SITELIBDIR}/PyQt5/QtOpenGL.so:x11/py-qt5-opengl \
	${PYTHON_PKGNAMEPREFIX}zeroconf>0:net/py-zeroconf \
	cura-binary-data>0:cad/cura-binary-data

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

.include <bsd.port.mk>
