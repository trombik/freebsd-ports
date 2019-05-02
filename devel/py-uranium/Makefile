# Created by: Tomoyuki Sakurai <y@trombik.org>
# $FreeBSD$

PORTNAME=	uranium
PORTVERSION=	4.0.0
CATEGORIES=	devel python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	y@trombik.org
COMMENT=	Python framework for building Desktop applications

LICENSE=	LGPL3
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}numpy>0:math/py-numpy@${FLAVOR}
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}numpy>0:math/py-numpy@${FLAVOR}
LIB_DEPENDS=	libArcus.so:devel/libArcus@${FLAVOR}

USES=		python:3.5+ cmake qt:5 pyqt:5
USE_GCC=	yes
USE_PYQT=	core
USE_PYTHON=	flavors
USE_QT=	quickcontrols
USE_GITHUB=	yes
GH_ACCOUNT=	Ultimaker
WRKSRC=	${WRKDIR}/Uranium-${PORTVERSION}
NO_ARCH=	yes
INSTALL_TARGET=	install

.include <bsd.port.mk>
