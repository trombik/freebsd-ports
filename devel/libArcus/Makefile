# Created by: Tomoyuki Sakurai <y@trombik.org>
# $FreeBSD$

PORTNAME=	libArcus
PORTVERSION=	3.0.3
CATEGORIES=	devel

MAINTAINER=	y@trombik.org
COMMENT=	Communication library for Ultimaker software

LICENSE=	LGPL3
LICENSE_FILE=	${WRKSRC}/LICENSE

LIB_DEPENDS=	libprotobuf.so:devel/protobuf
BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}sip>0:devel/py-sip@${FLAVOR}
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}sip>0:devel/py-sip@${FLAVOR}

USE_PYTHON= flavors
USE_GITHUB=	yes
GH_ACCOUNT=	Ultimaker
USES=	cmake python:3.4+

post-patch:
	${REINPLACE_CMD} 's|%%PYTHON_VER%%|${PYTHON_VER}|g' ${WRKSRC}/cmake/FindSIP.py

.include <bsd.port.mk>
