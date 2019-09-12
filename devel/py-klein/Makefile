# $FreeBSD$

PORTNAME=	klein
PORTVERSION=	19.6.0
CATEGORIES=	devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	y@trombik.org
COMMENT=	Micro-framework for developing production-ready web services

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}incremental>0:devel/py-incremental@${PY_FLAVOR}
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}attrs>0:devel/py-attrs@${PY_FLAVOR} \
	${PY_ENUM34} \
	${PY_TYPING} \
	${PYTHON_PKGNAMEPREFIX}hyperlink>0:www/py-hyperlink@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}hyperlink>0:www/py-hyperlink@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}incremental>0:devel/py-incremental@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}six>0:devel/py-six@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}tubes>0:devel/py-tubes@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}twisted>=15.5:devel/py-twisted@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}werkzeug>0:www/py-werkzeug@${PY_FLAVOR} \
	${PYTHON_PKGNAMEPREFIX}zope.interface>0:devel/py-zope.interface@${PY_FLAVOR}

USES=		python
USE_PYTHON=	autoplist distutils

.include <bsd.port.mk>
