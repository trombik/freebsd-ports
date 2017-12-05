# Created by: Tomoyuki Sakurai <y@trombik.org>
# $FreeBSD$

PORTNAME=	metriks
PORTVERSION=	0.9.9.8
CATEGORIES=	devel rubygems
MASTER_SITES=	RG

MAINTAINER=	y@trombik.org
COMMENT=	Threadsafe, low impact library to measure aspects of your ruby

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	rubygem-atomic>=1.0:devel/rubygem-atomic \
	rubygem-hitimes>=1.1:devel/rubygem-hitimes \
	rubygem-avl_tree>=1.2.0:devel/rubygem-avl_tree

NO_ARCH=	yes
USES=		gem
USE_RUBY=	yes

.include <bsd.port.mk>
