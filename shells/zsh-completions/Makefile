# Created by: Tomoyuki Sakurai <y@trombik.org>
# $FreeBSD$

PORTNAME=	zsh-completions
PORTVERSION=	0.27.0
CATEGORIES=	shells

MAINTAINER=	y@trombik.org
COMMENT=	Additional completion definitions for Zsh

LICENSE=	ZSH
LICENSE_NAME=	ZSH license
LICENSE_FILE=	${WRKSRC}/LICENSE
LICENSE_PERMS=	dist-mirror dist-sell pkg-mirror pkg-sell auto-accept

NO_ARCH=		yes
NO_BUILD=	yes
NO_INSTALL=	yes
SUB_FILES=		pkg-message

USE_GITHUB=	yes
GH_ACCOUNT=	zsh-users

do-install:
	@${MKDIR} ${STAGEDIR}${PREFIX}/share/zsh/site-functions/
	cd ${WRKSRC}/src && ${COPYTREE_SHARE} . ${STAGEDIR}${PREFIX}/share/zsh/site-functions/ "! -name *\.bak"

.include <bsd.port.mk>
