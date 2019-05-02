# Created by: Tomoyuki Sakurai <y@trombik.org>
# $FreeBSD$

PORTNAME=	CuraEngine
PORTVERSION=	4.0.0
CATEGORIES=	cad

MAINTAINER=	y@trombik.org
COMMENT=	C++ console application for 3D printing GCode generation

LICENSE=	AGPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

LIB_DEPENDS=	libArcus.so:devel/libArcus \
	libprotobuf.so:devel/protobuf
BUILD_DEPENDS=	stb>=0:devel/stb

USES=	cmake compiler
USE_GITHUB=	yes
GH_ACCOUNT= Ultimaker
PLIST_FILES=	bin/CuraEngine
CMAKE_ARGS+=	-DStb_INCLUDE_DIRS:STRING=${LOCALBASE}/include/stb
CXXFLAGS+=	-DCMAKE_CXX_FLAGS=-D__GLIBCXX_USE_CXX11_ABI=0

.include <bsd.port.mk>
