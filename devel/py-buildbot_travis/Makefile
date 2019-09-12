# $FreeBSD$

PORTNAME=	buildbot_travis
PORTVERSION=	0.6.4
CATEGORIES=	devel
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	y@trombik.org
COMMENT=	Adaptors to make Buildbot more like travis

LICENSE=	MIT

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}buildbot-pkg>0:devel/py-buildbot-pkg@${PY_FLAVOR}
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}buildbot-pkg>0:devel/py-buildbot-pkg@${PY_FLAVOR} \
				${PYTHON_PKGNAMEPREFIX}buildbot-www>0:devel/py-buildbot-www@${PY_FLAVOR} \
				${PYTHON_PKGNAMEPREFIX}buildbot-console-view>0:devel/py-buildbot-console-view@${PY_FLAVOR} \
				${PYTHON_PKGNAMEPREFIX}buildbot-waterfall-view>0:devel/py-buildbot-waterfall-view@${PY_FLAVOR} \
				${PYTHON_PKGNAMEPREFIX}buildbot-worker>0:devel/py-buildbot-worker@${PY_FLAVOR} \
				${PYTHON_PKGNAMEPREFIX}klein>0:devel/py-klein@${PY_FLAVOR} \
				${PYTHON_PKGNAMEPREFIX}urwid>0:devel/py-urwid@${PY_FLAVOR} \
				${PYTHON_PKGNAMEPREFIX}yaml>0:devel/py-yaml@${PY_FLAVOR} \
				${PYTHON_PKGNAMEPREFIX}txrequests>0:www/py-txrequests@${PY_FLAVOR} \
				${PYTHON_PKGNAMEPREFIX}pyjade>0:textproc/py-pyjade@${PY_FLAVOR} \
				${PYTHON_PKGNAMEPREFIX}txgithub>0:devel/py-txgithub@${PY_FLAVOR} \
				${PYTHON_PKGNAMEPREFIX}ldap3>0:net/py-ldap3@${PY_FLAVOR} \
				${PYTHON_PKGNAMEPREFIX}hyper_sh>0:devel/py-hyper_sh@${PY_FLAVOR} \
				${PYTHON_PKGNAMEPREFIX}future>0:devel/py-future@${PY_FLAVOR}

USES=		python
USE_PYTHON=	autoplist distutils

.include <bsd.port.mk>
