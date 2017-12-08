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

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}numpy>0:math/py-numpy
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}numpy>0:math/py-numpy
LIB_DEPENDS=	libArcus.so:devel/libArcus

USES=		python:3.5+ cmake pyqt:5
USE_PYQT=	core
USE_QT5=	quick quickcontrols
#USE_PYTHON=	autoplist distutils
USE_GITHUB=	yes
GH_ACCOUNT=	Ultimaker
WRKSRC=	${WRKDIR}/Uranium-${PORTVERSION}
NO_ARCH=	yes
INSTALL_TARGET=	install

post-patch:
	${REINPLACE_CMD} -e 's|%%PYTHON_VER%%|${PYTHON_VER}|g' \
		${WRKSRC}/CMakeLists.txt

.include <bsd.port.mk>
