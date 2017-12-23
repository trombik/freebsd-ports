# Created by: Tomoyuki Sakurai <y@trombik.org>
# $FreeBSD$

PORTNAME=	zeroconf
PORTVERSION=	0.19.1
CATEGORIES=	net python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	y@trombik.org
COMMENT=	Pure python implementation of multicast DNS service discovery

LICENSE=	LGPL21

RUN_DEPENDS=	\
	${PYTHON_PKGNAMEPREFIX}netifaces>=0.10.5:net/py-netifaces@${FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}six>0:devel/py-six@${FLAVOR}

USES=		python
USE_PYTHON=	autoplist distutils

.include <bsd.port.pre.mk>

.if ${PYTHON_VER} < 3.4
RUN_DEPENDS+=	${PYTHON_PKGNAMEPREFIX}enum-compat>0:devel/py-enum-compat
.endif

.include <bsd.port.post.mk>
