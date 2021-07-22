import platform

from setuptools import Extension, setup


def get_ext_modules() -> list:
    """
    获取三方模块

    Linux需要编译封装接口
    Windows直接使用预编译的pyd即可
    Mac由于缺乏二进制库支持无法使用
    """
    if platform.system() != "Linux":
        return []

    compiler_flags = [
        "-std=c++17",
        "-O3",
        "-Wno-delete-incomplete", "-Wno-sign-compare",
    ]
    extra_link_args = ["-lstdc++"]
    runtime_library_dirs = ["$ORIGIN"]

    vnttsmd = Extension(
        "vnpy_tts.api.vnttsmd",
        [
            "vnpy_tts/api/vntts/vnttsmd/vnttsmd.cpp",
        ],
        include_dirs=["vnpy_tts/api/include",
                      "vnpy_tts/api/vntts"],
        define_macros=[],
        undef_macros=[],
        library_dirs=["vnpy_tts/api/libs", "vnpy_tts/api"],
        libraries=["thostmduserapi_se", "thosttraderapi_se"],
        extra_compile_args=compiler_flags,
        extra_link_args=extra_link_args,
        runtime_library_dirs=runtime_library_dirs,
        depends=[],
        language="cpp",
    )

    vnttstd = Extension(
        "vnpy_tts.api.vnttstd",
        [
            "vnpy_tts/api/vntts/vnttstd/vnttstd.cpp",
        ],
        include_dirs=["vnpy_tts/api/include",
                      "vnpy_tts/api/vntts"],
        define_macros=[],
        undef_macros=[],
        library_dirs=["vnpy_tts/api/libs", "vnpy_tts/api"],
        libraries=["thostmduserapi_se", "thosttraderapi_se"],
        extra_compile_args=compiler_flags,
        extra_link_args=extra_link_args,
        runtime_library_dirs=runtime_library_dirs,
        depends=[],
        language="cpp",
    )

    return [vnttstd, vnttsmd]


setup(
    ext_modules=get_ext_modules(),
)
