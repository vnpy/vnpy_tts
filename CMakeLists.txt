# Author: chnzwn

# cmake version
CMAKE_MINIMUM_REQUIRED(VERSION 3.22)


PROJECT (vnttsMac)

set(CMAKE_MACOSX_RPATH TRUE)
#set(CMAKE_SKIP_BUILD_RPATH FALSE)
#set(CMAKE_BUILD_RPATH_USE_ORIGIN TRUE)


# cpp file
FILE(GLOB TD_SRC_LIST "${PROJECT_SOURCE_DIR}/vnpy_tts/api/vntts/vnttstd/vnttstd.cpp")
FILE(GLOB MD_SRC_LIST "${PROJECT_SOURCE_DIR}/vnpy_tts/api/vntts/vnttsmd/vnttsmd.cpp")

add_subdirectory(pybind11)

# include folder
INCLUDE_DIRECTORIES(${PROJECT_SOURCE_DIR}/vnpy_tts/api/include/)
# python include folder. (brew python)
INCLUDE_DIRECTORIES(
        /opt/homebrew/opt/python@3.10/Frameworks/Python.framework/Versions/3.10/include/python3.10
        )

# target output folder
SET(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/target)


find_library(THOSTAPI thostmduserapi_se.dylib ${PROJECT_SOURCE_DIR}/vnpy_tts/api/libs/arm64 )
find_library(THOSTTradeAPI thosttraderapi_se.dylib ${PROJECT_SOURCE_DIR}/vnpy_tts/api/libs/arm64 )
find_library(CRYPTO crypto ${PROJECT_SOURCE_DIR}/vnpy_tts/api/libs/ )
find_library(COMUNICATIONKEY comunicationkey ${PROJECT_SOURCE_DIR}/vnpy_tts/api/libs/ )
find_library(SSL ssl ${PROJECT_SOURCE_DIR}/vnpy_tts/api/libs/ )

# specify iconv library (xcode installed)
find_library(ICONV libiconv.tbd /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/lib/)


# vnttsmd
pybind11_add_module(vnttsmd SHARED ${MD_SRC_LIST})
# suffix
SET_TARGET_PROPERTIES(vnttsmd PROPERTIES SUFFIX ".so")

# link
TARGET_LINK_LIBRARIES(vnttsmd PRIVATE ${THOSTAPI} ${THOSTTradeAPI} ${CRYPTO} ${SSL} ${COMUNICATIONKEY}  ${ICONV})


# vnttstd
pybind11_add_module(vnttstd SHARED ${TD_SRC_LIST})
# suffix
SET_TARGET_PROPERTIES(vnttstd PROPERTIES SUFFIX ".so")
# link
TARGET_LINK_LIBRARIES(vnttstd PRIVATE ${THOSTAPI} ${THOSTTradeAPI} ${CRYPTO} ${SSL} ${COMUNICATIONKEY}  ${ICONV})
