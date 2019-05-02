# Created by: Tomoyuki Sakurai <y@trombik.org>
# $FreeBSD$

PORTNAME=	cura-binary-data
PORTVERSION=	4.0.0
CATEGORIES=	cad

MAINTAINER=	y@trombik.org
COMMENT=	Cura binary data for Cura

LICENSE=	AGPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

USE_GITHUB=	yes
GH_ACCOUNT=	Ultimaker
NO_BUILD=	yes

do-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/share/cura/resources
	cd ${WRKSRC}/cura/resources && ${COPYTREE_SHARE} . ${STAGEDIR}${PREFIX}/share/cura/resources

.include <bsd.port.mk>
