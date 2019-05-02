# Created by: Tomoyuki Sakurai <y@trombik.org>
# $FreeBSD$

PORTNAME=	libArcus
PORTVERSION=	4.0.0
CATEGORIES=	devel

MAINTAINER=	y@trombik.org
COMMENT=	Communication library for Ultimaker software

LICENSE=	LGPL3
LICENSE_FILE=	${WRKSRC}/LICENSE

LIB_DEPENDS=	libprotobuf.so:devel/protobuf
BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}sip>0:devel/py-sip@${PY_FLAVOR}
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}sip>0:devel/py-sip@${PY_FLAVOR}

USES=	cmake python:3.4+
USE_PYTHON= flavors
USE_GITHUB=	yes
GH_ACCOUNT=	Ultimaker

.include <bsd.port.mk>
