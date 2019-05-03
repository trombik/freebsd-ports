# Created by: Tomoyuki Sakurai <y@trombik.org>
# $FreeBSD$

PORTNAME=	Cura
PORTVERSION=	4.0.0
CATEGORIES=	cad

MAINTAINER=	y@trombik.org
COMMENT=	3D printer / slicing GUI application

LICENSE=	LGPL3
LICENSE_FILE=	${WRKSRC}/LICENSE

LIB_DEPENDS=	libSavitar.so:devel/libSavitar
# XXX Cura family is designed to have a matched version. all packages must use
# same version. hence, they use `=${PORTVERSION}`.
BUILD_DEPENDS= ${PYTHON_PKGNAMEPREFIX}uranium>=${PORTVERSION}:devel/py-uranium
RUN_DEPENDS=	\
	${PYTHON_PKGNAMEPREFIX}scipy>0:science/py-scipy@${FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}serial>0:comms/py-serial@${FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}uranium>=${PORTVERSION}:devel/py-uranium@${FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}zeroconf>0:net/py-zeroconf@${FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}requests>0:www/py-requests@${FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}Shapely>=0:devel/py-shapely@${FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}libCharon>=${PORTVERSION}:devel/py-libCharon@${FLAVOR} \
	${PYTHON_SITELIBDIR}/PyQt5/_QOpenGLFunctions_4_1_Core.so:x11/py-qt5-opengl@${FLAVOR} \
	${PYTHON_SITELIBDIR}/PyQt5/QtQuick.so:x11-toolkits/py-qt5-quick@${FLAVOR} \
	CuraEngine>=${PORTVERSION}:cad/CuraEngine \
	cura-resources-materials>=${PORTVERSION}:cad/cura-resources-materials \
	cura-binary-data>=${PORTVERSION}:cad/cura-binary-data

USES=		python:3.5+ cmake qt:5 pyqt:5 fortran desktop-file-utils shared-mime-info shebangfix
USE_PYTHON=	flavors
USE_QT=	core \
		quickcontrols \
		quickcontrols2 \
		graphicaleffects \
		opengl

USE_GITHUB=	yes
GH_ACCOUNT=	Ultimaker
INSTALL_TARGET=	install
NO_ARCH=	yes
python_OLD_CMD=	"/usr/bin/env python3"
SHEBANG_FILES=	cura_app.py
USE_PYQT=	svg network qml opengl
DATADIR=	${PREFIX}/share/cura

post-patch:
	${REINPLACE_CMD} -e 's|%%URANIUM_DATA%%|${LOCALBASE}/share/uranium|g' \
		-e 's|%%PORTVERSION%%|${PORTVERSION}|g' \
		${WRKSRC}/CMakeLists.txt

.include <bsd.port.mk>
