# Created by: Tomoyuki Sakurai <y@trombik.org>
# $FreeBSD$

PORTNAME=	dyndnsd
PORTVERSION=	1.6.1
CATEGORIES=	dns rubygems
MASTER_SITES=	RG

MAINTAINER=	y@trombik.org
COMMENT=	Small, lightweight and extensible DynDNS server

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	rubygem-json>=1.8.0:devel/rubygem-json \
	rubygem-rack>=1.6.0:www/rubygem-rack \
	rubygem-metriks>=0:devel/rubygem-metriks

NO_ARCH=	yes
USES=		gem
USE_RUBY=	yes
PLIST_FILES=	bin/dyndnsd
SUB_FILES=	config.yml.sample
SUB_LIST=	DYNDNSD_USER=${DYNDNSD_USER} \
			DYNDNSD_GROUP=${DYNDNSD_GROUP} \
			DYNDNSD_LOG_DIR=${DYNDNSD_LOG_DIR} \
			DYNDNSD_DB_DIR=${DYNDNSD_DB_DIR} \
			DYNDNSD_ZONE_DIR=${DYNDNSD_ZONE_DIR} \
			RUBY=${RUBY}

USE_RC_SUBR=	${PORTNAME}

DYNDNSD_USER=	dyndnsd
DYNDNSD_GROUP=	dyndnsd
DYNDNSD_LOG_DIR?=	/var/log/${PORTNAME}
DYNDNSD_DB_DIR?=	/var/db/${PORTNAME}
DYNDNSD_ZONE_DIR?=	${ETCDIR}/zones
USERS=	${DYNDNSD_USER}
GROUPS=	${DYNDNSD_GROUP}

.include <bsd.port.pre.mk>

post-patch:
	${REINPLACE_CMD} -e '/rack/ s|~> 1.6|>= 1.6.0|' \
		-e '/json/ s|~> 1.8|>= 1.8.0|' ${WRKSRC}/${GEMSPEC}

post-install:
	${INSTALL} -d ${STAGEDIR}${ETCDIR}
	${INSTALL_DATA} ${WRKDIR}/config.yml.sample \
	  ${STAGEDIR}${ETCDIR}/config.yml.sample
	${INSTALL} -d ${STAGEDIR}${DYNDNSD_LOG_DIR}
	${INSTALL} -d ${STAGEDIR}${DYNDNSD_DB_DIR}
	${INSTALL} -d ${STAGEDIR}${DYNDNSD_ZONE_DIR}

	${ECHO} "@sample ${ETCDIR}/config.yml.sample" >> ${TMPPLIST}
	${ECHO} "@dir(${DYNDNSD_USER},${DYNDNSD_GROUP},) ${DYNDNSD_LOG_DIR}" >> ${TMPPLIST}
	${ECHO} "@dir(${DYNDNSD_USER},${DYNDNSD_GROUP},) ${DYNDNSD_DB_DIR}" >> ${TMPPLIST}
	${ECHO} "@dir(${DYNDNSD_USER},${DYNDNSD_GROUP},) ${DYNDNSD_ZONE_DIR}" >> ${TMPPLIST}

.include <bsd.port.post.mk>
