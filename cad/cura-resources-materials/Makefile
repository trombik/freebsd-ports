# Created by: Tomoyuki Sakurai <y@trombik.org>
# $FreeBSD$

PORTNAME=	cura-resources-materials
PORTVERSION=	4.0.0
CATEGORIES=	cad

MAINTAINER=	y@trombik.org
COMMENT=	FDM Material database published by Ultimaker

LICENSE=	CC0-1.0
LICENSE_FILE=	${WRKSRC}/LICENSE

USE_GITHUB=	yes
GH_ACCOUNT=	Ultimaker
GH_PROJECT=	fdm_materials
NO_BUILD=	yes

do-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/share/cura/resources/materials
	cd ${WRKSRC} && ${COPYTREE_SHARE} . ${STAGEDIR}${PREFIX}/share/cura/resources/materials "-name *\.fdm_material"

.include <bsd.port.mk>
