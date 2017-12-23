# Created by: Tomoyuki Sakurai <y@trombik.org>
# $FreeBSD$

PORTNAME=	uranium
PORTVERSION=	3.0.3
CATEGORIES=	devel python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	y@trombik.org
COMMENT=	Python framework for building Desktop applications

LICENSE=	LGPL3
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}numpy>0:math/py-numpy@${FLAVOR}
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}numpy>0:math/py-numpy@${FLAVOR}
LIB_DEPENDS=	libArcus.so:devel/libArcus@${FLAVOR}
TEST_DEPENDS=	\
	${PYTHON_PKGNAMEPREFIX}pytest>0:devel/py-pytest@${FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}scipy>0:science/py-scipy@${FLAVOR} \
	${PYTHON_SITELIBDIR}/PyQt5/QtQml.so:lang/py-qt5-qml@${FLAVOR} \
	${PYTHON_SITELIBDIR}/PyQt5/QtQuick.so:x11-toolkits/py-qt5-quick@${FLAVOR} \
	${PYTHON_SITELIBDIR}/PyQt5/QtWidgets.so:x11-toolkits/py-qt5-widgets@${FLAVOR}

USES=		python:3.5+ cmake pyqt:5
USE_GCC=	yes
USE_PYQT=	core
USE_PYTHON=	flavors
USE_QT5=	quick quickcontrols
USE_GITHUB=	yes
GH_ACCOUNT=	Ultimaker
WRKSRC=	${WRKDIR}/Uranium-${PORTVERSION}
NO_ARCH=	yes
INSTALL_TARGET=	install

post-patch:
	${REINPLACE_CMD} -e 's|%%PYTHON_VER%%|${PYTHON_VER}|g' \
		${WRKSRC}/CMakeLists.txt

do-test:
	cd ${WRKSRC} && LD_LIBRARY_PATH=${_GCC_RUNTIME} ${PYTHON_CMD} -m pytest -v

.include <bsd.port.mk>
